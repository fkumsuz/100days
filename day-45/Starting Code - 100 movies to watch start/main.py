import requests
from bs4 import BeautifulSoup
import sys

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
sys.stdout.reconfigure(encoding='utf-8')
# Make the HTTP request and parse the content with BeautifulSoup
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# Find all <h3> elements
all_h3 = soup.find_all("h3")

# Print the text of each <h3> element
top_100=[h3.get_text() for h3 in all_h3 ]
top_100 = top_100[::-1]
print(top_100)


    
with open("movie.txt", "w", encoding="utf-8") as file:
    for movie in top_100:
        file.write(movie + "\n")