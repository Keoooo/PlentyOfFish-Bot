from selenium import webdriver
import time
import Config

# Import Config for your username and password
user = Config.DATACOUP_USERNAME
psw = Config.DATACOUP_PASSWORD
url = r'https://www.pof.com/meetme.aspx'

driver = webdriver.Chrome()
driver.get(url)

time.sleep(10)
username = driver.find_element_by_id("logincontrol_username")
password = driver.find_element_by_id("logincontrol_password")

username.send_keys(user)
password.send_keys(psw)

driver.find_element_by_css_selector(".logincontrol_button").click()

time.sleep(5)

for x in range(0, 1000):
    time.sleep(1)
    driver.find_element_by_css_selector(".meetme-yes-button").click()
    if x == 200:
        break
