# Honkai Star Rail Promo Code Scraping and Redemption

## About
This is a Python program built using Selenium and BeautifulSoup4 to scrape promotional redemption codes from numerous sources for Honkai Star Rail, and redeem them in-game.


## How to use
### Method 1: Single Run on local machine
1. Download the latest 
[Release](https://github.com/emmettirl/HSRRedemptionCodes/releases) and run the executable.


2. After running the program for the first time, a .env file will be generated. 
   - You will need to manually fill the .env file with your account information. 
   - You can find this by visiting the [web Redemption page](https://hsr.hoyoverse.com/gift)
   - Log in to your Hoyoverse account. 
   - Inspect the page, check storage to find your cookie, and copy all fields into .env.
   - Then enter a code and submit (For example: ```STARRAILGIFT```)
   - Check the Network tab to see the API request your browser sent to Hoyoverse, and copy the request information into the .env file.
 

3. Run the executable again. The program will open a Chrome window and start scraping for codes. It will then attempt to redeem them in-game, waiting about a minute (with slight random variations) between codes.

---

### Method 2: Automated daily run using GitHub Actions

1. Fork this repository.


2. Find your Cookie and Header information:
   - Visit the [web Redemption page](https://hsr.hoyoverse.com/gift) and log in to your Hoyoverse account.
   - Inspect the page, check storage to find your cookie. 
   - Enter a code and submit (For example: ```STARRAILGIFT```)
   - Check the Network tab to see the API request your browser sent to Hoyoverse.

3. Set up repositroy secrets.
   -  Go to the Settings tab of your forked repository and navigate to the Secrets section.
   - Add the following secrets, with the values you found in step 2:

   **Cookie details:**
   
   ```
     - ACCOUNT_ID_V2
     - ACCOUNT_MID_V2
     - COOKIE_TOKEN_V2
     - LTMID_V2
     - LTOKEN_V2
     - LTUID_V2
   ```
   **Request Headers:**
   ```
     - PLATFORM
     - REGION
     - UID
   ```
   

4. Enable GitHub Actions.
   - Go to the Actions tab of your forked repository and enable actions, specifically the workflow named "Run Latest Release".
   - The program will run every day at Midnight UTC.

---

## Notes
I have not designed this to be used by anyone other than myself. It is not user-friendly. Feel free to use it, fork it, etc., but in its current state I won't be providing support for it and offer no guarantees or warranties.


I have no idea if Hoyoverse will ban you for using this program. Use at your own risk. 


The program will not attempt to redeem codes more than once. If you want to redeem a code that has already been redeemed (for example if you want to run the program with a second account), you will need to manually remove it from the `redeemed_codes` directory. Alternatively just copy the program into another folder and run it from there with its own .env file. 


The program is built to be run on a Windows machine. It will not work on a Mac or Linux machine, as it downloads the Chrome WebDriver for Windows. I may add support for Mac and Linux in the future.


Releases are generated on each push to main. There is no "stable".


If you want to fork this project to continue development, you will want to create a GitHub access token to allow automated releases on your forked repository. This is not required for running the program, either locally or using GitHub Actions.


1. Fork this repository.
2. Set up a GitHub token
    - Go to your GitHub account settings and generate a new [personal access token](https://github.com/settings/tokens?type=beta).
    - Scope the token to "Only Select Repositories" and select the forked repository.
    - Add the Scope "Contents"

   - Take this token and add it as a secret to your forked repository called:```MY_GITHUB_TOKEN ```
3. Enable GitHub Actions.
4. Push a change to the main branch. This will trigger the workflow to run and create a release.

---

## Contributiion Guidelines

I welcome contributions, but please note that this is a personal project and I may not have time to review or merge pull requests. If you would like to contribute, please follow these guidelines:

- Fork the repository.
- Create a new branch.
- Make your changes.
- Test your changes.
- Create a pull request to the main branch of this repository.
- I will review the pull request when I have time.
- If I do not merge your pull request, please do not take it personally. I may not have time to review it, or it may not fit with the direction I want to take the project. Feel free to fork the project and continue development on your own.

Especially welcome are contributions that add new sources for scraping codes.

If you know of a source but do not want to implement it yourself, please open an issue with the source and I will consider adding it in the future.

---
## Acknowledgements

### Promo code sources

- Rock Paper Shotgun: https://www.rockpapershotgun.com/honkai-star-rail-codes-list
- HSR Wiki: https://honkai-star-rail.fandom.com/wiki/Redemption_Code
- Hum Bao's GitHub Repository: https://github.com/Hum-Bao/honkai-star-rail-codes/

### Libraries

- [Selenium](https://www.selenium.dev/)
- [BeautifulSoup4](https://beautiful-soup-4.readthedocs.io/en/latest/)

---

## Planned Features: 
- Add support for Mac and Linux
- Add support for more sources
- Automatic Cookie and Request scraping
- Sanitize codes before redeeming

(no timeline or promises)