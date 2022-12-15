from selenium import webdriver

from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.daraz.com.bd/")

driver.find_element(By.NAME, 'q').send_keys("mouse")
driver.find_element(By.XPATH, '//*[@id="topActionHeader"]/div/div[2]/div/div[2]/form/div/div[2]/button').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div').click()
driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/ul/li[3]/div').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div[1]/div/a/img').click()
price= driver.find_element(By.XPATH, '//*[@id="module_product_price_1"]/div/div/span')

time.sleep(5)
print("The price is : ")
print(price.text)

time.sleep(10)
