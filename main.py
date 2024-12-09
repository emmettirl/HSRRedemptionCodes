import logging
from env_config import EnvConfig
from WebScraping.harvester import Harvester  # Import the Harvester
from CodeRedemption.code_redeemer import CodeRedeemer  # Import the CodeRedeemer
from CodeRedemption.redemption_handler import RedemptionHandler  # Import the RedemptionHandler

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

# Entry point
if __name__ == "__main__":
    main()