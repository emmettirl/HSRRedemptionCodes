# rockpapershotgun_scraper.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

from web_scraping.code_validator import CodeValidator
from web_scraping.scraper_interface import ScraperInterface
from drivers.chrome_driver import ChromeDriverSingleton

import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()

class RockPaperShotgunScraper(ScraperInterface):
    def __init__(self):
        self.url = "https://www.rockpapershotgun.com/honkai-star-rail-codes-list"
        self.driver_path = ChromeDriverSingleton().driver_path

    def fetch_page(self):
        options = Options()
        options.headless = True
        service = Service(self.driver_path)
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(self.url)
        time.sleep(5)  # Wait for the page to load
        html_content = driver.page_source
        driver.quit()
        return html_content

    def parse_codes(self, html_content):
        soup = BeautifulSoup(html_content, "html.parser")
        codes = set()
        rows = soup.find_all("tr", {"data-index": True})
        for row in rows:
            code_tag = row.find("td").find("strong")
            if code_tag:
                text = code_tag.text
                codes.update(CodeValidator.extract_and_validate(text))
        logger.info(f"Found {len(codes)} codes\n")
        return codes

    def scrape(self):
        html_content = self.fetch_page()
        return self.parse_codes(html_content)

    def to_string(self):
        return "RockPaperShotgunScraper"

if __name__ == "__main__":
    scraper = RockPaperShotgunScraper()
    codes = scraper.scrape()
    logger.info(f"Fetched {len(codes)} unique codes:\n{codes}")