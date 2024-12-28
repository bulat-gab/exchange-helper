from src.okx.consts import TON_CURRENCY
from src.utils import logger, my_utils
from src.config import settings
from src.okx.okx_client import OkxClient as MyOkx
import random
import time

def send_ton_from_okx_to_wallets_from_file():
    addrs = []
    with open('withdraw-address.txt', 'r') as file:
        for line in file:
            addrs.append(line.strip())

    logger.info(f"File contains {len(addrs)} addresses.")

    myokx = MyOkx(settings.OKX_API_KEY, settings.OKX_API_SECRET, settings.OKX_API_PASSPHRASE, settings.PROXY_STR)
    chain_name = myokx.get_chain_name(currency=TON_CURRENCY)

    successful_requests_count = 0
    for to_addr in addrs:
        delay = random.randint(1, 10)
        logger.info(f"Processing address: '{to_addr}'. Sleeping for {delay} seconds before start.")
        time.sleep(delay)

        # Send between 0.3 and 0.4 TON
        random_amount = my_utils.random_float_with_step(start=0.3, end=0.4, step=0.01)
        resp = myokx.withdraw(TON_CURRENCY, chain_name, to_addr, random_amount)
        if resp:
            successful_requests_count += 1

    
    if successful_requests_count == len(addrs):
        logger.success(f"All '{len(addrs)}' addresses processed successfully.")
    else:
        logger.warning(f"{successful_requests_count} out of {len(addrs)} requests were successful")