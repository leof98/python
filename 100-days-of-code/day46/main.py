# Day 46
# Web Scraping
# Working with APIs
# Project day 46 - Creating a spotify playlist with a top 100 songs from billboard

import spotipy
from spotipy import SpotifyOAuth
from bs4 import BeautifulSoup
import requests

# Spotify API
CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URI = "http://example.com"

# Web Scraping
date = input("Choose a year (YYYY-MM-DD): ")

URL = f"https://www.billboard.com/charts/hot-100/{date}/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}

response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.text, "html.parser")

# Target the parent container for each song
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]


# Spotify Authorization

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="playlist-modify-private",
))

sp.current_user()
user = sp.current_user()["id"]

# Getting each track on spotify and creating a list
songs_uri = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_uri.append(uri)
    except IndexError:
        print(f"{song} doesn't exist.")

# Creating the playlist
playlist = sp.user_playlist_create(user, f"{date} Billboard 100", public=False, description="")

# Add the songs to the playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uri)
