import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sys
sys.stdout.reconfigure(encoding='utf-8')

# year_input = input("Enter the year you would like to travel to (YYYY-MM-DD format): ")
year_input="2022-09-29"
URL = f"https://www.billboard.com/charts/hot-100/{year_input}"

print(URL)

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
# all_h3 = soup.find_all( "h3", id="title-of-a-story"  )
title_text = soup.select('li ul li h3') 

top_100 = [h3.get_text(strip=True) for h3 in title_text ]
print(top_100) 
 
    
with open("movie.txt", "w", encoding="utf-8") as file:
    for movie in top_100:
        file.write(movie + "\n")

 