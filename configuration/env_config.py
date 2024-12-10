# env_config.py
import logging
import os
from dotenv import load_dotenv
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()

class EnvConfig:
    def __init__(self):
        self.env_file = '.env'
        self.create_env_file_if_not_exists()
        load_dotenv()
        self.cookie_token_v2 = os.getenv("COOKIE_TOKEN_V2")
        self.account_mid_v2 = os.getenv("ACCOUNT_MID_V2")
        self.account_id_v2 = os.getenv("ACCOUNT_ID_V2")
        self.ltoken_v2 = os.getenv("LTOKEN_V2")
        self.ltmid_v2 = os.getenv("LTMID_V2")
        self.ltuid_v2 = os.getenv("LTUID_V2")
        self.uid = os.getenv("UID")
        self.region = os.getenv("REGION")
        self.platform = os.getenv("PLATFORM")

        self.HEADERS = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Content-Type": "application/json;",
            "Origin": "https://hsr.hoyoverse.com",
            "DNT": "1",
            "Connection": "keep-alive",
            "Referer": "https://hsr.hoyoverse.com/"
        }

        self.COOKIES = {
            "cookie_token_v2": self.cookie_token_v2,
            "account_mid_v2": self.account_mid_v2,
            "account_id_v2": self.account_id_v2,
            "ltoken_v2": self.ltoken_v2,
            "ltmid_v2": self.ltmid_v2,
            "ltuid_v2": self.ltuid_v2,
}

        self.validate_env_variables()

    def create_env_file_if_not_exists(self):
        if not os.path.exists(self.env_file):
            with open(self.env_file, 'w') as file:
                file.write("# .env file for sensitive cookie information\n\n")
                file.write("# Cookie Fields\n")
                file.write("COOKIE_TOKEN_V2=\n")
                file.write("ACCOUNT_MID_V2=\n")
                file.write("ACCOUNT_ID_V2=\n")
                file.write("LTOKEN_V2=\n")
                file.write("LTMID_V2=\n")
                file.write("LTUID_V2=\n")
                file.write("\n")
                file.write("# Request Fields\n")
                file.write("UID=\n")
                file.write("REGION=\n")
                file.write("PLATFORM=\n")


    def validate_env_variables(self):
        required_vars = [
            "COOKIE_TOKEN_V2", "ACCOUNT_MID_V2", "ACCOUNT_ID_V2",
            "LTOKEN_V2", "LTMID_V2", "LTUID_V2",
            "UID", "REGION", "PLATFORM"
        ]
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        if missing_vars:
            logger.error(f"The following environment variables are missing in the .env file: {', '.join(missing_vars)}")
            logger.error("Please fill out the .env file with the required information and try again.")
            sys.exit(1)