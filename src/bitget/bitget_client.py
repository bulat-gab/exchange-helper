import requests
import hmac
import base64
import json
import time

from src.utils import logger

ON_CHAIN_TRANSFER_TYPE = 'on_chain'

def get_timestamp():
  return int(time.time() * 1000)


def sign(message, secret_key):
  mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
  d = mac.digest()
  return base64.b64encode(d)


def pre_hash(timestamp, method, request_path, body):
  return str(timestamp) + str.upper(method) + request_path + body


def parse_params_to_str(params):
    params = [(key, val) for key, val in params.items()]
    params.sort(key=lambda x: x[0])
    url = '?' + toQueryWithNoEncode(params)
    if url == '?':
        return ''
    return url

def toQueryWithNoEncode(params):
    url = ''
    for key, value in params:
        url = url + str(key) + '=' + str(value) + '&'
    return url[0:-1]

class BitgetClient:
    def __init__(self, api_key: str, api_secret: str, passphrase: str, proxy: str = None):
        self.host = 'https://api.bitget.com'
        self.api_key = api_key
        self.api_secret = api_secret
        self.passphrase = passphrase
        self.proxies = None
        if proxy:
            self.proxies = {
                "http": proxy,
                "https": proxy
            }
    
    def _create_headers(self, method: str, request_path: str, body: str = ''):
        timestamp = get_timestamp()
        sign_message = pre_hash(timestamp, method, request_path, str(body))
        signature = sign(sign_message, self.api_secret)

        headers = {
                "ACCESS-KEY": self.api_key,
                "ACCESS-SIGN": signature,
                "ACCESS-PASSPHRASE": self.passphrase,
                "ACCESS-TIMESTAMP": str(timestamp),
                "Locale": "en-US",
                "Content-Type": "application/json"
        }
        return headers
    
    def get_assets(self):
            method = 'GET'
            request_path = '/api/v2/spot/account/assets'
            
            headers = self._create_headers(method, request_path)
            url = self.host + request_path 
            response = requests.get(url, headers=headers, proxies=self.proxies)
            if response.status_code == 200:
                logger.info(f"Request get_assets success")
                data = response.json()
                print("Response:", data)
                return data
            else:
                logger.warning(f'Request get_assets failed. Code: {response.status_code}. {response.text}')
                return None
            
    def withdraw(self, address: str, amount: str):
        logger.info(f'Withdraw {amount} to address "{address}".')
        method = 'POST'
        request_path = '/api/v2/spot/wallet/withdrawal'

        body = {
            'coin': 'BNB',
            'transferType': ON_CHAIN_TRANSFER_TYPE,
            'address': address,
            'chain': 'BEP20',
            'size': amount # BNB min is 0.01
        }
        headers = self._create_headers(method, request_path,  json.dumps(body))
        url = self.host + request_path 

        response = requests.post(url, headers=headers, proxies=self.proxies, json=body)
        if response.status_code == 200:
            logger.info(f"Request withdraw success")
            data = response.json()
            logger.info("Response:", data)
            return data
        else:
            logger.warning(f'Request withdraw failed. Code: {response.status_code}. {response.text}')
            return None