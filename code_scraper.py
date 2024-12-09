from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

import time

class CodeScraper:
    def __init__(self, url):
        self.url = url
        self.driver_path = 'C:/Users/emmet/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'  # Update this path to your WebDriver

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
        print(f"Found {len(rows)} rows with data-index attribute")  # Debugging statement
        for row in rows:
            code_tag = row.find("td").find("strong")
            if code_tag:
                code = code_tag.text
                rewards_tag = row.find_all("td")[1].text.strip()
                status_tag = row.find_all("td")[2].text.strip()
                codes.append({"code": code, "rewards": rewards_tag, "status": status_tag})
        return codes

    def get_codes(self):
        html_content = self.fetch_page()
        print(f"Fetched HTML content: {html_content[:500]}")  # Debugging statement
        return self.parse_codes(html_content)

def main():
    url = "https://www.rockpapershotgun.com/honkai-star-rail-codes-list"
    scraper = CodeScraper(url)
    codes = scraper.get_codes()
    for code in codes:
        print(code)

if __name__ == "__main__":
    main()