import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup
from datetime import datetime  
import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
# Değişken adını ve değerini belirle
 
# Add your Spotify API credentials here
client_id = os.environ.get("SPOTIPY_CLIENT_ID") 
client_secret =  os.environ.get("SPOTIPY_CLIENT_SECRET") 
redirect_uri =  os.environ.get("SPOTIPY_REDIRECT_URI")  
    
print(client_id)
  
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
print(user_id) 

# year_input = input("Enter the year you would like to travel to (YYYY-MM-DD format): ")
year_input="2023-01-01"
URL = f"https://www.billboard.com/charts/hot-100/{year_input}"

print(URL)

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
# all_h3 = soup.find_all( "h3", id="title-of-a-story"  )
title_text = soup.select('li ul li h3') 

top_100 = [h3.get_text(strip=True) for h3 in title_text ]
 
date = year_input
song_names = top_100

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris) 