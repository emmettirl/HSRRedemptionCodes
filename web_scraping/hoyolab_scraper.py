# hoyolab_scraper.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from web_scraping.scraper_interface import ScraperInterface
from drivers.chrome_driver import ChromeDriverSingleton
from web_scraping.code_validator import CodeValidator

import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()

class HoyolabScraper(ScraperInterface):
    def __init__(self):
        self.url = "https://www.hoyolab.com/topicDetail/298842"
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
        divs = soup.find_all("div")
        for div in divs:
            text = div.get_text()
            codes.update(CodeValidator.extract_and_validate(text))
        logger.info(f"Found {len(codes)} unique codes\n")
        return codes

    def scrape(self):
        html_content = self.fetch_page()
        return self.parse_codes(html_content)

    def to_string(self):
        return "HoyolabScraper"

if __name__ == "__main__":
    scraper = HoyolabScraper()
    codes = scraper.scrape()
    logger.info(f"Fetched {len(codes)} unique codes:\n{codes}")