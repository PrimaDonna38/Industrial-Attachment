from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()

phone_email= input("Enter Your phone number or email: ")
password= input("Enter Your Password: ")

time.sleep(10)
driver.get("https://www.daraz.com.bd/")
driver.find_element(By.XPATH, "//a[contains(text(),'Signup / Login')]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//body/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/input[1]").send_keys(phone_email)
time.sleep(2)
driver.find_element(By.XPATH, "//body/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/input[1]").send_keys(password)
time.sleep(2)
driver.find_element(By.XPATH,"//button[contains(text(),'LOGIN')]").click()
time.sleep(5)
driver.quit()