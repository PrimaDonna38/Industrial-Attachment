from selenium import webdriver
import time
driver= webdriver.Chrome()

driver.get('https://bup.edu.bd/')
time.sleep(5)
print(driver.title)
driver.get('https://bup.edu.bd/on_campus/campus-life')
time.sleep(5)
print(driver.title)
driver.back()
time.sleep(5)
print(driver.title)
driver.forward()
time.sleep(5)
print(driver.title)
driver.quit()