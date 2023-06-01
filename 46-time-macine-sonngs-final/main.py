import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import find_dotenv, load_dotenv
from pprint import pprint
import json

with open("token.txt", "r") as x:
    contents = x.read()
    token = json.loads(contents)["access_token"]

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URL = os.getenv("REDIRECT_URL")

date = input("Which year do you want to travel to? Type the dat in this format YYYY-MM-DD: ")
# date = '2000-08-12'
billboard_endpoint = f"https://www.billboard.com/charts/hot-100/{date}/"

data = requests.get(billboard_endpoint)
# print(data.text)
soup = BeautifulSoup(data.text, 'html.parser')
songs_title_html = soup.select(".c-title.a-no-trucate")
songs_artist_html = soup.select(".c-label.a-no-trucate")
# print(songs_artist_html)
songs_list = []
artist_list = []
[songs_list.append(i.text.strip()) for i in songs_title_html]
[artist_list.append(i.text.strip()) for i in songs_artist_html]

# print(songs_list)
# print(artist_list)
# dsf.


## Authenticate and save the playlist to spotify

scope = 'playlist-modify-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URL,
                                               scope=scope,
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               ))

# Checking if there is already a playlist with that name
playlists = sp.user_playlists(user=sp.me()["id"])
for playlist in playlists["items"]:
    if playlist["name"] == f"{date} Billboard 100":
        print("There is already a playlist for this date please enter a different date")
        quit()

## Create a spotify playlist and add songs to the playlist

sp.user_playlist_create(
    user=sp.me()["id"],
    name=f"{date} Billboard 100",
    public=True,
    description=f"These are the songs on billboard on the date {date}. Ans this is generated via python."
)

## Get spotify playlist id
playlists = sp.user_playlists(user=sp.me()["id"])
for playlist in playlists["items"]:
    if playlist["name"] == f"{date} Billboard 100":
        print(playlist["name"])
        playlistId = playlist["id"]
        print(playlistId)
        break

uri_code_list = []
for song in songs_list:
    song_info = sp.search(q=song, type="track", limit=1)
    uri = song_info["tracks"]["items"][0]["uri"]
    # sp.user_playlist_add_tracks(user=sp.me()["id"], playlist_id=playlistId, tracks=uri, position=count)
    uri_code_list.append(uri)

sp.playlist_add_items(playlist_id=playlistId, items=uri_code_list)
# print(uri_code_list)
