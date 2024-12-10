# rockpapershotgun_scraper.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from web_scraping.scraper_interface import ScraperInterface
from drivers.download_and_extract_chromedriver import download_and_extract_chromedriver

import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()

class RockPaperShotgunScraper(ScraperInterface):
    def __init__(self):
        self.url = "https://www.rockpapershotgun.com/honkai-star-rail-codes-list"
        self.driver_path = download_and_extract_chromedriver()

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
        codes = []
        rows = soup.find_all("tr", {"data-index": True})
        for row in rows:
            code_tag = row.find("td").find("strong")
            if code_tag:
                code = code_tag.text
                codes.append(code)
        logger.info(f"Found {len(codes)} codes\n")
        return codes

    def scrape(self):
        html_content = self.fetch_page()
        return self.parse_codes(html_content)

    def to_string(self):
        return "RockPaperShotgunScraper"
