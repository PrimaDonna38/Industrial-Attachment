from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.facebook.com")
print("Application title is ", driver.title)
print("Application url is ", driver.current_url)
driver.quit