import logging
from configuration.env_config import EnvConfig
from web_scraping.harvester import Harvester  # Import the Harvester
from code_redemption.code_redeemer import CodeRedeemer  # Import the CodeRedeemer
from code_redemption.redemption_handler import RedemptionHandler  # Import the RedemptionHandler

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
env = EnvConfig()

# Constants
HEADERS = env.HEADERS
COOKIES = env.COOKIES

# Main function
def main():
    harvester = Harvester()
    code_redeemer = CodeRedeemer(HEADERS, COOKIES)
    redemption_handler = RedemptionHandler(harvester, code_redeemer)
    redemption_handler.process_codes()
    return 0

# Entry point
if __name__ == "__main__":
    main()