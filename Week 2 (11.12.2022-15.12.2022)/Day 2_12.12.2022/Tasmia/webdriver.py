from selenium import webdriver
driver= webdriver.Chrome()
driver.maximize_window()

driver.get('http://www.google.com')
print("The title is: ", driver.title)
print("The url is: ", driver.current_url)
driver.quit()