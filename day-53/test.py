
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
    my_dict[i]=[list_links[i],list_prices[i],list_address[i] ] 
    
print(len(my_dict))
