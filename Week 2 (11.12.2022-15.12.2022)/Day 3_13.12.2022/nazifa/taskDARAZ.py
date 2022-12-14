from selenium import webdriver

from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.daraz.com.bd/")

driver.find_element(By.NAME, 'q').send_keys("mouse")
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="topActionHeader"]/div/div[2]/div/div[2]/form/div/div[2]/button').click()

price= driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/span')

print("The price is : ")
print(price.text)
driver.close()
time.sleep(10)
