from selenium import webdriver
import time

# Not displaying the browser
option = webdriver.ChromeOptions()
option.add_argument("headless")

# Specifying the path of my Chrome driver
browser = webdriver.Chrome("C:\Program Files\chromedriver\chromedriver.exe")

# Getting to Free Chegg.com Website
url = "https://techlacarte.com/how-to-get-chegg-answers-for-free/"
browser.get(url)
time.sleep(8)

# Declaring the path of the needed elements
userNamePath = browser.find_element_by_xpath('//*[@id="wpforms-13116-field_1"]')
questionLinkPath = browser.find_element_by_xpath('//*[@id="wpforms-13116-field_4"]')
emailAddressPath = browser.find_element_by_xpath('//*[@id="wpforms-13116-field_2"]')
sendButtonPath = browser.find_element_by_xpath('//*[@id="wpforms-submit-13116"]')

userName = input("What is your name? ")
emailAddress = input(f"Dear, {userName} please write your email address where the answer will be sent: ")

while True:
    # Asking for the question link from the user
    questionLink = input(f"Dear, {userName} Please paste your Chegg question link and click enter: ")

    # Sending the input one-by-one
    time.sleep(1)
    userNamePath.send_keys(userName)
    time.sleep(0.25)
    questionLinkPath.send_keys(questionLink)
    time.sleep(0.25)
    emailAddressPath.send_keys(emailAddress)
    time.sleep(0.25)

    # Finally sending all the result, and waiting for the answer
    sendButtonPath.click()

    for i in range(6):
        print("Working on it" + i*".")
        time.sleep(1)

    print("Please check your main within 15-45 minutes to get your answer!")
    print("Made by Vusal with the help of TchLaCarte <3")
    browser.refresh()
