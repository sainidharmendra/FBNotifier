from selenium import webdriver
from time import sleep
from getpass import getpass
from notify_run import Notify

notify = Notify()
print("Enter Login Credentials :")
userName = input("Enter Email/Phone: ")
passWord = getpass("Enter Password: ")
friendId = input("Enter User Profile ID/UserName: ")
chrome_options = webdriver.ChromeOptions()  
chrome_options.headless = True 
driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
driver.get('https://www.facebook.com')
print("Opening Facebook Webpage")
userNameInputBox = driver.find_element_by_id('email')
passWordInputBox = driver.find_element_by_id('pass')
userNameInputBox.send_keys(userName)
passWordInputBox.send_keys(passWord)
print("Input UserName and Password Success")
loginBtn = driver.find_element_by_id('loginbutton')
loginBtn.click()
print("Login Success")
driver.get('https://www.facebook.com/messages/t/'+friendId)
while True:
    statusCheck = driver.find_elements_by_xpath("//div[contains(text(), 'Active on ')]")
    if len(statusCheck) > 0 :
        notify.send('Your Friend is Online')
        driver.quit()
        print("Notification Sent, Your Friend is Online")
        exit(1)
    else :
        print("User Not Online, Rechecking in 10 secs")
        driver.refresh()
        sleep(10)







