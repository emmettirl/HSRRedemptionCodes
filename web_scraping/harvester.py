# harvester.py
import logging

from web_scraping.github_scraper import GithubScraper
from web_scraping.rockpapershotgun_scraper import RockPaperShotgunScraper
from web_scraping.hsrwiki_scraper import HsrWikiScraper

class Harvester:
    def __init__(self):
        self.scrapers = [RockPaperShotgunScraper(), HsrWikiScraper(), GithubScraper()]

    def collect_codes(self):
        unique_codes = set()
        for scraper in self.scrapers:
            logging.info(f"Scraping with {scraper.to_string()}")
            codes = scraper.scrape()
            for code in codes:
                unique_codes.add(code)

        logging.info(f"Found {len(unique_codes)} unique codes across all scrapers.\n")
        return list(unique_codes)