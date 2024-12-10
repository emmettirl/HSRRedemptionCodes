import os
import subprocess
import requests
import zipfile
import logging


url = "https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.87/win64/chromedriver-win64.zip"

class ChromeDriverSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ChromeDriverSingleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'driver_path'):
            self.driver_path = self.download_and_extract_chromedriver()

    def download_and_extract_chromedriver(self, extract_to='drivers'):
        project_root = self.get_project_root()
        extract_to = os.path.join(project_root, 'drivers')
        os.makedirs(extract_to, exist_ok=True)
        zip_path = os.path.join(extract_to, 'chromedriver.zip')

        for root, dirs, files in os.walk(extract_to):
            if 'chromedriver.exe' in files:
                driver_path = os.path.join(root, 'chromedriver.exe')
                logging.info(f"ChromeDriver already exists at {driver_path}")
                return driver_path

        logging.info(f"Downloading ChromeDriver from {url}...")
        response = requests.get(url)
        with open(zip_path, 'wb') as file:
            file.write(response.content)

        logging.info(f"Extracting ChromeDriver to {extract_to}...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)

        os.remove(zip_path)

        for root, dirs, files in os.walk(extract_to):
            if 'chromedriver.exe' in files:
                driver_path = os.path.join(root, 'chromedriver.exe')
                logging.info(f"ChromeDriver downloaded and extracted to {driver_path}")
                return driver_path

        raise FileNotFoundError("chromedriver.exe not found in the extracted zip file")

    def get_project_root(self):
        return subprocess.run(['git', 'rev-parse', '--show-toplevel'], capture_output=True, text=True).stdout.strip()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    chrome_driver = ChromeDriverSingleton()