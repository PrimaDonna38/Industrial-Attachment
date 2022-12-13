from selenium import webdriver

from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.facebook.com/login.php/")

print("Application title is ", driver.title)
driver.find_element(By.NAME, 'email').send_keys("") #enter email
driver.find_element(By.NAME, 'pass').send_keys("") #enter password
time.sleep(10)
driver.find_element(By.NAME, 'login').click()
time.sleep(10 )
driver.close()