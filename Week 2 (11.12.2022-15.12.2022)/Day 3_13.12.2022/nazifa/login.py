from selenium import webdriver

from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.coursera.org/professional-certificates/facebook-social-media-marketing?adgroupid=1220458377857116&adpostion=&authMode=login&campaignid=415265990&creativeid=&device=c&devicemodel=&hide_mobile_promo&keyword=coursera+social+media+management&matchtype=b&msclkid=6c107b25e038126af96c18bda3bc58a7&network=o&utm_campaign=08-SocialMediaMktg-FB-ROW&utm_content=08-SocialMediaMktgPC-FB-ROW&utm_medium=sem&utm_source=bg&utm_term=coursera+social+media+management")

print("Application title is ", driver.title)
driver.find_element(By.NAME, 'email').send_keys("nazifaafroz18@gmail.com")
driver.find_element(By.NAME, 'password').send_keys("18NACucam")
time.sleep(10)
driver.find_element(By.CSS_SELECTOR, 'body > div._1widl7g > div > div > section > section > div:nth-child(2) > form > button').click()
time.sleep(10 )
driver.close()