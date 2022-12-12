from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://www.facebook.com")

print("Application tiyle is ", driver.title)
print("Application url is ", driver.current_url)

driver.quit()

