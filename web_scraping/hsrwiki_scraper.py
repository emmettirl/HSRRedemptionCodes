# hsrwiki_scraper.py
import requests
from bs4 import BeautifulSoup

from web_scraping.scraper_interface import ScraperInterface


class HsrWikiScraper(ScraperInterface):
    def __init__(self):
        self.url = "https://honkai-star-rail.fandom.com/wiki/Redemption_Code"

    def to_string(self):
        return "HsrWikiScraper"

    def scrape(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        codes = []

        # Find all table rows containing redemption codes
        rows = soup.select('table tbody tr')
        for row in rows:
            code_element = row.select_one('td code')
            validity_element = row.select_one('td:last-child')
            if code_element and validity_element and "expired" not in validity_element.text.lower():
                code = code_element.text.strip()
                codes.append(code)

        print(f"Found {len(codes)} codes\n")
        return codes

if __name__ == "__main__":
    scraper = HsrWikiScraper()
    codes = scraper.scrape()
    print(f"Fetched {len(codes)} codes:\n{codes}")