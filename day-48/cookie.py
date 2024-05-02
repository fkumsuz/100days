from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import time
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)
driver= webdriver.Chrome(options=chrome_option)

driver.get("https://orteil.dashnet.org/experiments/cookie/")   
 
 
game_is_on=True
def countdown(seconds):
    global game_is_on
    for i in range(seconds, 0, -1):
        print(f"Kalan süre: {i} saniye", end="\r")
        time.sleep(1)
        game_is_on=True
    print("Süre doldu!")
    game_is_on=False
    return game_is_on
 
store_divs = driver.find_elements(By.XPATH,value="/html/body/div[3]/div[5]/div/div[*]/b") 
store= []
for i in store_divs:
    try:
        result = int(i.text.replace(",", "").replace("\n", "").split("-", 1)[-1].strip()) 
        store.append(result)
    except ValueError:
        pass
print(store)
cookie= driver.find_element(By.XPATH,value='//*[@id="cookie"]') 
store_divs = driver.find_elements(By.ID,value="store") 
# store_div içindeki tüm div öğelerini bul
  
nested_divs = []
for store_div in store_divs:
    nested_divs.extend(store_div.find_elements(By.TAG_NAME, "div"))
print(nested_divs)
while game_is_on:  
    
    cookie.click() 

    cookie_score= driver.find_element(By.XPATH,value='//*[@id="money"]') 
    # print(cookie_score.text)


 

    

# store_divs = driver.find_elements(By.ID,value="store") 
# # store_div içindeki tüm div öğelerini bul
  
# nested_divs = []
# for store_div in store_divs:
#     nested_divs.extend(store_div.find_elements(By.TAG_NAME, "div"))
    

# for div in nested_divs:
#     try: 
#         result = div.text
#         result = int(result.replace("\n", "").split("-", 1)[-1].strip()) 
#     except ValueError:
#         pass
#     print(result )  
#     //*[@id="buyCursor"]/b
#     //*[@id="buyGrandma"]/b
#     <div id="buyCursor" onclick="Buy('Cursor');" style="background-image:url(cursoricon.png);" class=""><b>Cursor - <moni></moni> 15</b>Autoclicks every 5 seconds.</div>
# while game_is_on:
 
  


