from selenium import webdriver
import time

# Specifying the path of my Chrome driver
browser = webdriver.Chrome("C:\Program Files\chromedriver\chromedriver.exe")

# # Getting to Free Chegg.com Website
url = "https://techlacarte.com/how-to-get-chegg-answers-for-free/"
browser.get(url)
time.sleep(8)

userNamePath =
questionLinkPath =
emailAddressPath =
sendButtonPath = 

while True:
    userName = input("What is your name? ")
    questionLink = input(f"Dear, {userName} Please paste your Chegg question link and click enter: ")
    emailAddress = input(f"Dear, {userName} please write your email address where the answer will be sent: ")
    time.sleep(1)
    print("Working on it...")
    for i in range(5):
        print("Working on it" + i*".")

