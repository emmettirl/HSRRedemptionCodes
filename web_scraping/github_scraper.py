# github_scraper.py
import requests
import logging

from web_scraping.scraper_interface import ScraperInterface

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()

# https://github.com/Hum-Bao/honkai-star-rail-codes/tree/main

class GithubScraper(ScraperInterface):
    def __init__(self):
        self.url = "https://raw.githubusercontent.com/Hum-Bao/honkai-star-rail-codes/main/codes_RAW.txt"

    def scrape(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            scraped_codes = response.text.splitlines()
            logger.info(f"Found {len(scraped_codes)} codes\n")
            return scraped_codes
        else:
            response.raise_for_status()

    def to_string(self):
        return "GithubScraper"

# Example usage
if __name__ == "__main__":
    scraper = GithubScraper()
    codes = scraper.scrape()
    logger.info(f"Fetched {len(codes)} codes:\n{codes}")