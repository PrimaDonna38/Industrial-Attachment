from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver= webdriver.Chrome()
driver.maximize_window()
time.sleep(10)
driver.get("https://www.sodapdf.com/word-to-pdf/")
time.sleep(10)
driver.find_element(By.ID, "choose-file").send_keys("F://Industrial Attachment/week 2/day 4 (14.12.2022)/doc.docx")
time.sleep(10)
driver.quit()