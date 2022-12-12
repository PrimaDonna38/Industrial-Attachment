from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('http://www.google.com')
driver.find_element(By.NAME, 'q').send_keys("youtube")

time.sleep(5)
driver.quit()