# This is implemented, but has a limitation set in MAX_RESULTS of fetching only 5 tweet.
# Twitter API limitations are very strict at 100 tweets per month.
# Just incase twitter relaxes their limitations, I'll leave this code as is.

import requests
import logging
import os
from dotenv import load_dotenv
from web_scraping.code_validator import CodeValidator
from web_scraping.scraper_interface import ScraperInterface

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()

MAX_RESULTS = 5
TWITTER_USERNAMES = ['hsrcodes']

class TwitterScraper(ScraperInterface):

    def to_string(self):
        return "TwitterScraper"

    def __init__(self, bearer_token):
        self.bearer_token = bearer_token

    def create_headers(self):
        headers = {"Authorization": f"Bearer {self.bearer_token}"}
        return headers

    def get_user_id(self, username):
        url = f"https://api.twitter.com/2/users/by/username/{username}"
        headers = self.create_headers()
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Request returned an error: {response.status_code} {response.text}")
        user = response.json()
        return user['data']['id']

    def fetch_tweets(self, username):
        try:
            user_id = self.get_user_id(username)
            url = f"https://api.twitter.com/2/users/{user_id}/tweets?max_results={MAX_RESULTS}"
            headers = self.create_headers()
            response = requests.get(url, headers=headers)
            if 400 <= response.status_code < 600:
                logger.error(f"Request returned an error: {response.status_code} {response.text}")
                return []
            tweets = response.json()
            return [tweet['text'] for tweet in tweets['data']]
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            return []

    def parse_codes(self, tweets):
        codes = set()
        for tweet in tweets:
            codes.update(CodeValidator.extract_and_validate(tweet))
        logger.info(f"Found {len(codes)} unique codes\n")
        return codes

    def scrape(self):
        codes = set()
        for username in TWITTER_USERNAMES:
            tweets = self.fetch_tweets(username)
            codes.update(self.parse_codes(tweets))
        return codes



if __name__ == "__main__":
    # Load credentials from .env
    load_dotenv()
    BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

    scraper = TwitterScraper(BEARER_TOKEN)
    codes = scraper.scrape()
    logger.info(f"Fetched {len(codes)} unique codes:\n{codes}")