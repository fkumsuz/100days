
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.common.keys import Keys
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)
driver= webdriver.Chrome(options=chrome_option)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_number = driver.find_element(By.CSS_SELECTOR,value='#articlecount a')  

print(article_number.text) 
article_number.click() 
search = driver.find_element(By.XPATH,value='//*[@id="p-search"]/a/span[1]') 
search.click()
search_bar = driver.find_element(By.CLASS_NAME,value='cdx-text-input__input') 
search_bar.send_keys("Python",Keys.ENTER) 
 
 