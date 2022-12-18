from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://member.daraz.com.bd/user/login")
time.sleep(5)

uname=input("Enter Username : ")
passw=input("Enter password : ")

driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/form/div/div[1]/div[1]/input').send_keys(uname)
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/form/div/div[1]/div[2]/input').send_keys(passw)
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/form/div/div[2]/div[1]/button').click()
time.sleep(10)

driver.quit()