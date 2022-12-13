from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
from selenium.webdriver.common.by import By
driver.maximize_window()

driver.get("https://bup.edu.bd/")

driver.find_element(By.XPATH,"/html/body/header/div/div/div/ul/li[1]/a" ).click()

time.sleep(5)
driver.close()