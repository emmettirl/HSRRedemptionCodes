# Honkai Star Rail Redemption Code Scraping and Redemption

## Introduction
This is a python program built in Selenium to scrape Honkai Star Rail promotional redemption codes from numerous sources, and redeem them in-game. 

The program is built to be run on a Windows machine. It will not work on a Mac or Linux machine, as it downloads the Chrome WebDriver for Windows. I may add support for Mac and Linux in the future.

Note I have not designed this to be used by anyone other than myself. It is not user-friendly. Feel free to use it, fork it, etc., but in its current state I won't be providing support for it and offer no guarantees or warranties.

I have no idea if Hoyoverse will ban you for using this program. 
Use at your own risk. 

## Requirements
- Python 3.13 (older versions may work, but I have not tested them)
- Selenium
- BeautifulSoup
- Chrome WebDriver (downloaded automatically by the program)

## How to use
Download the repository and run the `main.py` file. The program will open a Chrome window and start scraping for codes. It will then attempt to redeem them in-game, waiting a random amount of time between codes.

After running the program for the first time, a .env file will be generated. You will need to manually fill the .env file with your account information. You can find this by visiting the web Redemption page:

https://hsr.hoyoverse.com/gift

While inspecting the page, check storage to find your cookie, and copy all fields into .env. 

Then enter a code and submit.
For example: ```STARRAILGIFT```

Check the Network tab, and copy the request information into the .env file.

The program will not attempt to redeem codes that have already been redeemed. If you want to redeem a code that has already been redeemed, you will need to manually remove it from the `redeemed_codes` directory.

## ToDo:
- Add support for Mac and Linux
- Add support for more sources
- Automatic Cookie and Request scraping
- Scheduling / github actions