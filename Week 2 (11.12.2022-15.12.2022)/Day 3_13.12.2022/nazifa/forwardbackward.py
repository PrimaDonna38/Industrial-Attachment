from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
from selenium.webdriver.common.by import By
driver.maximize_window()

driver.get("https://bup.edu.bd/admission")

driver.find_element(By.XPATH, "//a[contains(text(),'On Campus')]" ).click()
time.sleep(2)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.quit()