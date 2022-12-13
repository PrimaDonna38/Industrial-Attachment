from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://bup.edu.bd/')
driver.find_element(By.XPATH, "/html/body/header/div/div/div/ul/li[1]/a").click()
time.sleep(5)
driver.quit()