from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.ilovepdf.com/word_to_pdf")
time.sleep(10)
driver.find_element(By.ID, 'html5_1gka0d2ss1qh02o91chq1i5s1g154').send_keys("C://Users/DELL/Documents/07.-Cover-Page-for-Assignments.docx")
time.sleep(10)
driver.quit()