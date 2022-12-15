from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://member.daraz.com.bd/user/login")

username=input("Enter Username: ")
driver.find_element(By.XPATH, "//*[@id='container']/div/div[2]/form/div/div[1]/div[1]/input").send_keys(username)
time.sleep(10)
password=input("Enter Password: ")
driver.find_element(By.XPATH, "//*[@id='container']/div/div[2]/form/div/div[1]/div[2]/input").send_keys(password)
time.sleep(10)
driver.find_element(By.CSS_SELECTOR, "#container > div > div:nth-child(2) > form > div > div.mod-login-col2 > div.mod-login-btn > button").click()
time.sleep(10)

driver.quit()

