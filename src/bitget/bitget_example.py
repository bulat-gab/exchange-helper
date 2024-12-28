# bg = bitget.BitgetClient(api_key, api_secret, passphrase, proxy)
# assets = bitget_client.get_assets()
# if assets:
#     file_utils.write_json(assets, './output/assets.json')

# resp = requests.get("https://api.bitget.com/api/v2/spot/public/coins?coin=BNB")
# r = resp.json()
# file_utils.write_json(r, './output/coin_info.json')

# fee = 0.0002
# amount = 0.012
# total = str(fee + amount)
# withdraw_response = bg.withdraw('', total)
# file_postfix = f'{int(time.time())}'
# file_utils.write_json(withdraw_response, f'./output/withdraw_{file_postfix}.json')