import requests
import hmac
import base64
import json
import time

from src import bitget
from src.utils import file_utils, logger, my_utils
from src.config import settings

from src.okx.okx_client import OkxClient as MyOkx

from src.okx.okx_example import send_ton_from_okx_to_wallets_from_file


send_ton_from_okx_to_wallets_from_file()