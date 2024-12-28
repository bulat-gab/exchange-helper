from src.utils import logger

from okx.Funding import FundingAPI


ONCHAIN_WITHDRAWL_DEST = 4

class OkxClient:
    

    def __init__(self, api_key: str, api_secret: str, passphrase: str, proxy: str = None):
        # self.host = 'https://api.bitget.com'
        self.api_key = api_key
        self.api_secret = api_secret
        self.passphrase = passphrase
        self.proxies = None
        if proxy:
            self.proxies = {
                "http": proxy,
                "https": proxy
            }
        
        self._funding_api = FundingAPI(api_key, api_secret, passphrase, proxy=proxy,  flag='0')


    def get_chain_name(self, currency: str):
        resp: dict = self._funding_api.get_currencies(ccy=currency)
        data: list[dict] = resp.get('data')
        chain = data[0].get('chain')
        logger.info(f"The chain for currency '{currency}' is '{chain}'")
        return chain
    
    def withdraw(self, currency: str, chain: str, to_address: str, amount: float) -> bool:
        resp = self._funding_api.withdrawal(ccy=currency, amt=amount, dest=ONCHAIN_WITHDRAWL_DEST, toAddr=to_address, chain=chain)
        if resp and resp.get('code') == '0':
            logger.success(f"Withdrawl successful. {resp}")
            return True
        else:
            logger.error(f"Withdrawl failed. {resp}")
            return False
    
    def validate_address(self, address: str, chain: str) -> bool:
        pass