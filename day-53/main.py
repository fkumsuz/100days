
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import time
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)
driver= webdriver.Chrome(options=chrome_option)

 
sys.stdout.reconfigure(encoding='utf-8')


import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sys
sys.stdout.reconfigure(encoding='utf-8')
 
URL = f"https://appbrewery.github.io/Zillow-Clone/"  #44 ilan olması gerekiyor

print(URL)

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser") 
list_links=[]
list_prices=[]
list_address=[]

links = soup.find_all(attrs={"data-test": "property-card-link"},class_="property-card-link")
for l in links: 
    list_links.append(l['href']) 
    # Print the links and their href attributes
# print( list_links )

prices = soup.find_all(attrs={"data-test": "property-card-price"},class_="PropertyCardWrapper__StyledPriceLine")
for p in prices: 
    price=p.text
    list_prices.append(price.replace('/mo', '').replace('+ 1bd', '').replace('+ 1 bd', '').replace('+', '')) 
    # Print the links and their href attributes
# print( list_prices ) 
 

adresses = soup.find_all("address")
for a in adresses:  
    address=a.text 
    list_address.append(address.replace('\n                                ', '').replace(' | ',' ').replace('  ',' ').lstrip())
    # Print the links and their href attributes
# print(  list_address ) 
 
my_dict={}
for i in range(44):
    my_dict[i]=[list_address[i],list_prices[i], list_links[i]] 
    
print(len(my_dict))


 
SURVEY_LINKS='https://docs.google.com/forms/d/e/1FAIpQLSdQPu8XaRFcd3wA87Q-BERL5Zu1ib4GgTRELGINCWlOVQXlKQ/viewform'



driver.get(SURVEY_LINKS)    

for x in range (len(my_dict)):
    input_box = driver.find_elements (By.CSS_SELECTOR,'input.whsOnd.zHQkBf[jsname="YPqjbf"]')
    gonder_button= driver.find_element (By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span') 
    for i,value in enumerate(input_box): 
        value.click()  
        value.send_keys(my_dict[x][i] ) 
        
    gonder_button.click() 
    another_answer_link= driver.find_element (By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_answer_link.click() 

print("All Done!")
