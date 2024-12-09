import os
import requests
import time
import logging
import random
import re

from datetime import datetime
from env_config import EnvConfig
from code_scraper import CodeScraper  # Import the CodeScraper

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
env = EnvConfig()

# Constants
URL = "https://public-operation-hkrpg.hoyoverse.com/common/apicdkey/api/webExchangeCdkeyRisk"
HEADERS = env.HEADERS
COOKIES = env.COOKIES
REDEEMED_CODES_DIR = 'redeemed_codes'

# Ensure the directory exists
os.makedirs(REDEEMED_CODES_DIR, exist_ok=True)

# Check if the code is expired
def is_expired(expiry_date):
    if expiry_date is None:
        return False
    return datetime.strptime(expiry_date, "%Y-%m-%d") < datetime.now()

# Attempt to redeem a code
def redeem_code(code):
    payload = {
        "t": int(time.time() * 1000),  # Current timestamp
        "lang": "en",
        "game_biz": "hkrpg_global",
        "uid": "703387880",
        "region": "prod_official_eur",
        "cdkey": code["code"],
        "platform": "4",
        "device_uuid": os.getenv("MHYUUID")
    }
    try:
        response = requests.post(URL, headers=HEADERS, cookies=COOKIES, json=payload)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        logging.error(f"Failed to redeem code {code['code']}: {e}")
        return None

# Handle response messages
def handle_response_message(code, message):
    logging.info(f"Code {code['code']} is invalid. Reason: {message}")
    write_code_to_message_file(code["code"], message)

# Read redeemed codes from all files in the directory
def read_redeemed_codes():
    redeemed_codes = set()
    for file_name in os.listdir(REDEEMED_CODES_DIR):
        file_path = os.path.join(REDEEMED_CODES_DIR, file_name)
        with open(file_path, 'r') as file:
            redeemed_codes.update(line.strip() for line in file)
    return redeemed_codes

# Write a redeemed code to file
def write_redeemed_code(code):
    file_path = os.path.join(REDEEMED_CODES_DIR, 'redeemed_codes.txt')
    with open(file_path, 'a') as file:
        file.write(f"{code}\n")
        file.flush()
        os.fsync(file.fileno())

# Clean message to be safe for file names
def clean_message(message):
    return re.sub(r'[^\w\s-]', '', message).strip().replace(' ', '_')

# Write code to a file named after the cleaned message
def write_code_to_message_file(code, message):
    cleaned_message = clean_message(message)
    file_name = f"{cleaned_message}.txt"
    file_path = os.path.join(REDEEMED_CODES_DIR, file_name)
    with open(file_path, 'a') as file:
        file.write(f"{code}\n")
        file.flush()
        os.fsync(file.fileno())

# Main function
def main():
    url = "https://www.rockpapershotgun.com/honkai-star-rail-codes-list"
    scraper = CodeScraper(url)
    codes = scraper.get_codes()
    redeemed_codes = read_redeemed_codes()

    for code in codes:
        if code["code"] in redeemed_codes or is_expired(code.get("expiry_date")):
            continue  # Skip already redeemed or expired codes

        logging.info(f"Trying code: {code['code']}")
        response = redeem_code(code)
        if response and response.status_code == 200:
            response_json = response.json()
            if response_json.get("retcode") == 0:
                logging.info(f"Code {code['code']} redeemed successfully!")
                write_redeemed_code(code["code"])
            else:
                message = response_json.get("message", "Unknown")
                handle_response_message(code, message)
        else:
            logging.error(f"Failed to process code {code['code']}. HTTP Status: {response.status_code if response else 'N/A'}")

        # Wait 1 minute plus a random amount of time before the next attempt
        sleep_time = 60 + random.uniform(5, 15)
        logging.info(f"Waiting {sleep_time:.2f} seconds before the next attempt...")
        time.sleep(sleep_time)

# Entry point
if __name__ == "__main__":
    main()