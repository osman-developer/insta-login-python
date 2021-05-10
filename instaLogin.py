from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('D:/Programming/python login insta/chromedriver.exe')
driver.get('https://www.instagram.com/')
sleep(1)

# to open in max size
driver.maximize_window()
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

driver.find_element_by_name("username").send_keys('your username')
sleep(1)

driver.find_element_by_name("password").send_keys('your password')
sleep(1)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()

