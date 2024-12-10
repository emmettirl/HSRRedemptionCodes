# Honkai Star Rail Promo Code Scraping and Redemption

## About
This is a python program built in Selenium to scrape Honkai Star Rail promotional redemption codes from numerous sources, and redeem them in-game.

Note I have not designed this to be used by anyone other than myself. It is not user-friendly. Feel free to use it, fork it, etc., but in its current state I won't be providing support for it and offer no guarantees or warranties.

I have no idea if Hoyoverse will ban you for using this program. 
Use at your own risk. 

## How to use
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

## Notes
The program will not attempt to redeem codes that have already been redeemed. If you want to redeem a code that has already been redeemed (for example if you want to run the program with a second account), you will need to manually remove it from the `redeemed_codes` directory. Alternatively just copy the program into another folder and run it from there. 

The program is built to be run on a Windows machine. It will not work on a Mac or Linux machine, as it downloads the Chrome WebDriver for Windows. I may add support for Mac and Linux in the future.

Releases are generated on each push to main. There is no "stable".

## Planned Features: 
- Add support for Mac and Linux
- Add support for more sources
- Automatic Cookie and Request scraping

(no timeline or promises)