# harvester.py
from web_scraping.rockpapershotgun_scraper import RockPaperShotgunScraper

class Harvester:
    def __init__(self):
        self.scrapers = [RockPaperShotgunScraper()]

    def collect_codes(self):
        unique_codes = set()
        for scraper in self.scrapers:
            print(f"Scraping with {scraper.to_string()}")
            codes = scraper.scrape()
            for code in codes:
                unique_codes.add(code["code"])

        print(f"Found {len(unique_codes)} unique codes\n")
        return list(unique_codes)