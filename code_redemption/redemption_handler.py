# redemption_handler.py
import logging
import random
import time

class RedemptionHandler:
    def __init__(self, harvester, code_redeemer):
        self.harvester = harvester
        self.code_redeemer = code_redeemer

    def process_codes(self):
        unique_codes = self.harvester.collect_codes()
        redeemed_codes = self.code_redeemer.read_redeemed_codes()

        for index, code in enumerate(unique_codes):
            if code in redeemed_codes:
                print(f"Code {code} has already been redeemed, Skipping.")
                continue  # Skip already redeemed codes

            logging.info(f"Trying code: {code}")
            response = self.code_redeemer.redeem_code({"code": code})
            if response and response.status_code == 200:
                response_json = response.json()
                if response_json.get("retcode") == 0:
                    logging.info(f"Code {code} redeemed successfully!")
                    self.code_redeemer.write_redeemed_code(code)
                else:
                    message = response_json.get("message", "Unknown")
                    self.code_redeemer.handle_response_message({"code": code}, message)
            else:
                logging.error(f"Failed to process code {code}. HTTP Status: {response.status_code if response else 'N/A'}")

            # Wait 1 minute plus a random amount of time before the next attempt, if there are more codes to process
            if index < len(unique_codes) - 1:
                sleep_time = 60 + random.uniform(5, 15)
                logging.info(f"Waiting {sleep_time:.2f} seconds before the next attempt...")
                time.sleep(sleep_time)