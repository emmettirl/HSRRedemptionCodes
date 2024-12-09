import os
import requests
import zipfile

url = "https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.87/win64/chromedriver-win64.zip"

def download_and_extract_chromedriver(extract_to='drivers'):
    # Ensure the directory exists
    os.makedirs(extract_to, exist_ok=True)

    # Define the path for the downloaded zip file
    zip_path = os.path.join(extract_to, 'chromedriver.zip')

    # Check if the driver already exists
    for root, dirs, files in os.walk(extract_to):
        if 'chromedriver.exe' in files:
            driver_path = os.path.join(root, 'chromedriver.exe')
            print(f"ChromeDriver already exists at {driver_path}\n")
            return driver_path

    # Download the zip file
    print(f"Downloading ChromeDriver from {url}...")
    response = requests.get(url)
    with open(zip_path, 'wb') as file:
        file.write(response.content)

    # Extract the zip file
    print(f"Extracting ChromeDriver to {extract_to}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    # Clean up the zip file
    os.remove(zip_path)

    # Search for the chromedriver.exe file in the extracted contents
    for root, dirs, files in os.walk(extract_to):
        if 'chromedriver.exe' in files:
            driver_path = os.path.join(root, 'chromedriver.exe')
            print(f"ChromeDriver downloaded and extracted to {driver_path}\n")
            return driver_path

    raise FileNotFoundError("chromedriver.exe not found in the extracted zip file")

if __name__ == "__main__":
    # Download and extract the ChromeDriver
    driver_path = download_and_extract_chromedriver()