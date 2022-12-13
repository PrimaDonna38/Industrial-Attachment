from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver= webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.daraz.com.bd/')
driver.find_element(By.NAME, "q").send_keys("mouse")
driver.find_element(By.CSS_SELECTOR, "#topActionHeader > div > div.lzd-logo-bar > div > div.lzd-nav-search > form > div > div.search-box__search--2fC5 > button").click()
""" driver.find_element(By.CLASS_NAME, "ant-select-arrow").click()
element=driver.find_element(By.CLASS_NAME, "ant-select-lg select--Vohwf ant-select ant-select-enabled")
drp=Select(element)
drp.select_by_index('Price high to low') """
driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div[1]/div/a/img").click()
price=driver.find_element(By.XPATH, "//*[@id='module_product_price_1']/div/div/span")
print(price.text)
time.sleep(10)
driver.quit()