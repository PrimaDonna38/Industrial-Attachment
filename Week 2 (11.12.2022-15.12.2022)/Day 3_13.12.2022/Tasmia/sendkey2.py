from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()

driver.implicitly_wait(6)
driver.maximize_window()

driver.get("https://www.google.com/")
print(driver.title)
driver.find_element(By.NAME, 'q').send_keys("naveen automationlabs")
optionsList=driver.find_elements(By.CSS_SELECTOR, 'ul.G43f7e li span')
print(len(optionsList))

for ele in optionsList:
    print(ele.text)
    if ele.text == 'naveen automationlabs youtube':
        ele.click()
        break

time.sleep(10)
driver.quit()