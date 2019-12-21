# FBNotifier
A simple python script to let you know whenever your friend is online on Facebook.


#Requirements
1. Python3
2. Selenium
3. Notify-run

#Setup Guide

This script make use of Chrome Webdriver. Make sure use have installed latest Chrome Browser.

Install ChromeDriver :-

Open terminal and execute the commands one by one.
1. sudo apt-get install unzip
2. wget -N http://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_linux64.zip
3. unzip chromedriver_linux64.zip
4. chmod +x chromedriver
5. sudo mv -f chromedriver /usr/local/share/chromedriver
6. sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
7. sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

Install Python3 :-

1. sudo apt install python3

Install Pip3 :-

1. sudo apt install python3-pip

Install Selenium and Notify-Run using pip3:-

1. pip3 install selenium

2. pip3 install notify-run

How to use the Script:-

1. First of all create and register a channel for Notify-Run
 
Open Terminal and Execute the following command:

notify-run register

After this a QR code will display on the terminal. Scan the QR code and open the Url in the Chrome Browser.

Click Subscribe in the Add Subscription tab and Allow Notifications.

2. Now we can execute the Python script.

python3 FBNotifier.py

->Enter FB Email/Phone
->Enter Password
->Enter your facebook friend username/id.

And let the script do the job.












