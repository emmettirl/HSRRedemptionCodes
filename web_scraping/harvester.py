# harvester.py
from web_scraping.rockpapershotgun_scraper import RockPaperShotgunScraper
from web_scraping.hsrwiki_scraper import HsrWikiScraper

class Harvester:
    def __init__(self):
        self.scrapers = [RockPaperShotgunScraper(), HsrWikiScraper()]

    def collect_codes(self):
        unique_codes = set()
        for scraper in self.scrapers:
            print(f"Scraping with {scraper.to_string()}")
            codes = scraper.scrape()
            for code in codes:
                unique_codes.add(code["code"])

        print(f"Found {len(unique_codes)} unique codes across all scrapers.\n")
        return list(unique_codes)