from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
#driver.implicitly_wait(5)
driver.maximize_window()
time.sleep(5)
driver.get("https://www.daraz.com.bd/catalog/?spm=a2a0e.home.search.1.735212f7bQ0TOY&q=mouse&_keyori=ss&from=search_history&sugg=mouse_0_1")
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div').click()