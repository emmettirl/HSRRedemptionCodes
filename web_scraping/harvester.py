# harvester.py
import logging

from configuration.env_config import EnvConfig
from web_scraping.rockpapershotgun_scraper import RockPaperShotgunScraper
from web_scraping.hsrwiki_scraper import HsrWikiScraper
from web_scraping.github_scraper import GithubScraper
from web_scraping.hoyolab_scraper import HoyolabScraper
from web_scraping.twitter_scraper import TwitterScraper


class Harvester:
    def __init__(self):
        self.scrapers = [RockPaperShotgunScraper(), HsrWikiScraper(), GithubScraper(), HoyolabScraper()]
        env = EnvConfig()

        if env.twitter_bearer_token:
            self.scrapers.append(TwitterScraper(env.twitter_bearer_token))
        else:
            logging.warning("\nTwitter credentials not found. Skipping Twitter scraping.\n")

    def collect_codes(self):
        unique_codes = set()
        for scraper in self.scrapers:
            logging.info(f"Scraping with {scraper.to_string()}")
            codes = scraper.scrape()
            for code in codes:
                unique_codes.add(code)

        logging.info(f"Found {len(unique_codes)} unique codes across all scrapers.\n")
        return list(unique_codes)

if __name__ == "__main__":
    harvester = Harvester()
    codes = harvester.collect_codes()
    logging.info(f"Collected {len(codes)} unique codes:\n{codes}")