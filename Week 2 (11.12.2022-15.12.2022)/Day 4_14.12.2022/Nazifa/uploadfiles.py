from selenium import webdriver

from selenium.webdriver.common.by import By

import time
driver=webdriver.Chrome()
#driver.implicitly_wait(5)
driver.maximize_window()
time.sleep(5)
driver.get("https://www.adobe.com/acrobat/online/pdf-to-word.html")
time.sleep(15)

driver.find_element(By.ID, 'fileInput').send_keys("C://Users/88018/Pictures/test.pdf")
time.sleep(100)
