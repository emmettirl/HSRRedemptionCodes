# code_redeemer.py
import os
import requests
import logging
import re
from datetime import datetime
import time

# Constants
URL = "https://public-operation-hkrpg.hoyoverse.com/common/apicdkey/api/webExchangeCdkeyRisk"

class CodeRedeemer:
    def __init__(self, headers, cookies, redeemed_codes_dir='code_redemption/redeemed_codes'):
        self.headers = headers
        self.cookies = cookies
        self.redeemed_codes_dir = redeemed_codes_dir
        os.makedirs(self.redeemed_codes_dir, exist_ok=True)
        self.uid = os.getenv("UID")
        self.region = os.getenv("REGION")
        self.platform = os.getenv("PLATFORM")


    def is_expired(self, expiry_date):
        if expiry_date is None:
            return False
        return datetime.strptime(expiry_date, "%Y-%m-%d") < datetime.now()

    def redeem_code(self, code):
        payload = {
            "t": int(time.time() * 1000),  # Current timestamp
            "lang": "en",
            "game_biz": "hkrpg_global",
            "uid": self.uid,
            "region": self.region,
            "cdkey": code["code"],
            "platform": self.platform,
            "device_uuid": os.getenv("MHYUUID")
        }
        try:
            response = requests.post(URL, headers=self.headers, cookies=self.cookies, json=payload)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            logging.error(f"Failed to redeem code {code['code']}: {e}")
            return None

    def handle_response_message(self, code, message):
        logging.info(f"Code {code['code']} is invalid. Reason: {message}")
        self.write_code_to_message_file(code["code"], message)

    def read_redeemed_codes(self):
        redeemed_codes = set()
        for file_name in os.listdir(self.redeemed_codes_dir):
            file_path = os.path.join(self.redeemed_codes_dir, file_name)
            with open(file_path, 'r') as file:
                redeemed_codes.update(line.strip() for line in file)
        return redeemed_codes

    def write_redeemed_code(self, code):
        file_path = os.path.join(self.redeemed_codes_dir, 'redeemed_codes.txt')
        with open(file_path, 'a') as file:
            file.write(f"{code}\n")
            file.flush()
            os.fsync(file.fileno())

    def clean_message(self, message):
        return re.sub(r'[^\w\s-]', '', message).strip().replace(' ', '_')

    def write_code_to_message_file(self, code, message):
        cleaned_message = self.clean_message(message)
        file_name = f"{cleaned_message}.txt"
        file_path = os.path.join(self.redeemed_codes_dir, file_name)
        with open(file_path, 'a') as file:
            file.write(f"{code}\n")
            file.flush()
            os.fsync(file.fileno())