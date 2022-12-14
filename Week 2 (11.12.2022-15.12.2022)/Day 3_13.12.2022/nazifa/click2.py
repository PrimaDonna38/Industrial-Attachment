
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://bup.edu.bd/')
driver.find_element(By.CSS_SELECTOR, 'body > header > div > div > div > ul > li:nth-child(1) > a').click()
time.sleep(5)
driver.quit()
