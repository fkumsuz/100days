from selenium import webdriver

from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)
driver= webdriver.Chrome(options=chrome_option)

# driver.get("https://www.amazon.com.tr/gp/product/B07W6JL85W/ref=ox_sc_saved_image_1?smid=A1UNQM1SR2CHM&psc=1")
# price_lira = driver.find_element(By.CLASS_NAME,value="a-price-whole").text
# price_kurus= driver.find_element(By.CLASS_NAME,value="a-price-fraction").text

# print(f"The price is {price_lira},{price_kurus} lira.")

driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME,value="q") 
print(search_bar.tag_name)
 
donate_button = driver.find_element(By.CLASS_NAME,value="donate-button") 
print(donate_button.text)
print(donate_button.size)
  

documentation_link = driver.find_element(By.CSS_SELECTOR,value=".documentation-widget a")  
print(documentation_link.text)
 

submit_website = driver.find_element(By.XPATH,value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')  
print(submit_website.text)
driver.quit()


