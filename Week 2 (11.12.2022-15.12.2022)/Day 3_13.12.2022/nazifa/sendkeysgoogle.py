from selenium import webdriver

from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://www.google.com")

print("Application title is ", driver.title)
driver.find_element(By.NAME, 'q').send_keys("naveen automationlabs")


time.sleep(60)
driver.quit()

