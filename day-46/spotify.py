import spotipy
from spotipy.oauth2 import SpotifyOAuth
 

# Add your Spotify API credentials here
client_id = "aa9a520cb26845a49981471e365706ec"
client_secret = "0765170ac29e493fbcca95b908234099"
redirect_uri = "http://example.com" 
   

import spotipy
from spotipy.oauth2 import SpotifyOAuth

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

# Search for tracks
results = sp.search("Runaway", limit=10, type='track')

# Display search results
print("Search Results:")
for idx, track in enumerate(results['tracks']['items']):
    artists = ', '.join([artist['name'] for artist in track['artists']])
    print(f"{idx+1}. {artists} - {track['name']}")