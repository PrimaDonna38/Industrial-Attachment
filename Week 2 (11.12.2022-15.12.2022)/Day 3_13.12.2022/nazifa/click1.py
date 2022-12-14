
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://webportal.bup.edu.bd/Account/Login')
driver.find_element(By.CSS_SELECTOR, 'body > div > div > div > div.col-md-5.col-sm-12.login-right > span > a:nth-child(1)').click()
time.sleep(5)
driver.quit()
