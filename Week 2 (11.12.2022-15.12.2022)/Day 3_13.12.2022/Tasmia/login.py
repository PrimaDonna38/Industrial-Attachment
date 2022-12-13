from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver= webdriver.Chrome()
driver.maximize_window()
driver.get('https://bup.edu.bd/')
driver.find_element(By.XPATH, "/html/body/header/div/div/div/ul/li[1]/a").click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="UserId"]').send_keys("2054901014")
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="Password"]').send_keys("Bismillah@14")
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/form/div[2]/button').click()
time.sleep(5)
driver.close()