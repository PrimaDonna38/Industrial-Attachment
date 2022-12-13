from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://www.google.com")
print("Application title is ", driver.title)

driver.find_element()


driver.quit(By.NAME, 'q').send_keys("naveen automationlabs")
time.sleep(3)
optionsList = driver.find_elements(By.CSS_SELECTOR, 'ul. erkvQe li span')
for s in optionsList:
    print(s.text)