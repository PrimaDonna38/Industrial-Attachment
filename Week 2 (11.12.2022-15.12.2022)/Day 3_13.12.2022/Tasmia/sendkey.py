from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('http://www.youtube.com')
driver.find_element(By.NAME, 'search_query').send_keys("python")
optionList= driver.find_elements(By.CSS_SELECTOR, 'ul.sbsb_b li div div')

print(len(optionList))
for ele in optionList:
    print(ele.text)
    if ele.text== 'python tutorial':
        ele.click()
        break
time.sleep(10)
driver.quit()