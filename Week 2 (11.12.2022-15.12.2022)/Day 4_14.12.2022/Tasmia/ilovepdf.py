from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver= webdriver.Chrome()
driver.maximize_window()
time.sleep(5)
driver.get("https://www.ilovepdf.com/word_to_pdf")
time.sleep(10)
driver.find_element(By.ID, "html5_1gk7r0qjh4gaiu81n4416ku172k4").send_keys("F://Industrial Attachment/week 2/day 4 (14.12.2022)/doc.docx")
time.sleep(20)
driver.quit()