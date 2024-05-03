import requests
from bs4 import BeautifulSoup
import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth
 

# Add your Spotify API credentials here
client_id = "aa9a520cb26845a49981471e365706ec"
client_secret = "0765170ac29e493fbcca95b908234099"
redirect_uri = "http://example.com" 

SPOTIPY_CLIENT_ID=client_id
SPOTIPY_CLIENT_SECRET=client_secret
SPOTIPY_REDIRECT_URI=redirect_uri

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
        
        
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username="furkan.kumsuz1997", 
    )
)
user_id = sp.current_user()["id"]

song_names = top_100

song_uris = []
year = year_input="2022-09-29".split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")