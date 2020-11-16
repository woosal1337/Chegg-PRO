from selenium import webdriver
import time

# Specifying the path of my Chrome driver
browser = webdriver.Chrome("C:\Program Files\chromedriver\chromedriver.exe")

# # Getting to Chegg.com
url = "https://www.chegg.com"
browser.get(url)
time.sleep(5)

# Logging into the account
f = open("account.password", "r")
loginPassword = f.readline().split(";")
accountLogin = loginPassword[0]
accountPassword = loginPassword[1]

# Button placement on the website
signInPath = browser.find_element_by_xpath("//*[@id='eggshell-15']/a")
                                           #//*[@id="eggshell-14"]/a
signInPath.click()
time.sleep(3)

# Email and Password Sign-in
emailPath = browser.find_element_by_xpath('//*[@id="emailForSignIn"]')
passwordPath = browser.find_element_by_xpath('//*[@id="passwordForSignIn"]')
signInAccountPath = browser.find_element_by_xpath('//*[@id="eggshell-8"]/form/div/div/div/footer/button')
emailPath.send_keys(accountLogin)
passwordPath.send_keys(accountPassword)
time.sleep(1)
signInAccountPath.click()
time.sleep(5)

