# Day 46 Project - Musical Time Machine
import requests
import config
import spotipy
from pprint import pprint
from bs4 import BeautifulSoup

billboard_url = "https://www.billboard.com/charts/hot-100/"


def spot_authorisation():
    sp = spotipy.Spotify(
        auth_manager=spotipy.oauth2.SpotifyOAuth(
            client_id=config.SPOTIFY_CLIENT_ID,
            client_secret=config.SPOTIFY_CLIENT_SECRET,
            redirect_uri=config.SPOTIFY_REDIRECT_URL,
            scope="playlist-modify-private",
            cache_path="token.txt"))

    return sp


def get_song_names(date):
    response = requests.get(f"{billboard_url}/{user_date}")
    webpage = response.text

    soup = BeautifulSoup(webpage, "html.parser")
    # print(soup.prettify())

    titles = soup.select(selector="li h3")
    song_names = [title.getText().strip('\n\n\t\n\t\n\t\t\n\t\t\t\t\t') for title in titles[:100]]

    artists = soup.select(selector=".c-label.a-no-trucate")
    song_artists = [artist.getText().strip('\n\t\n\t') for artist in artists]

    return song_names, song_artists


def create_playlist(playlist_name, uri_list):
    playlist = sp.user_playlist_create(user_id, playlist_name, public=False)
    sp.playlist_add_items(playlist['id'], uri_list)


user_date = input("What date would you like to travel to? YYYY-MM-DD: ")
song_details = get_song_names(user_date)

sp = spot_authorisation()
user_id = sp.current_user()["id"]

song_uris = []

for i in range(len(song_details[0])):
    track = sp.search(q=f"{song_details[0][i]} artist: {song_details[1][i]}", type="track", limit=1)
    try:
        uri = track['tracks']['items'][0]['uri']
    except IndexError:
        print(f"{song_details[0][i]} can't be found in spotify")
    else:
        #print(f"{song_details[0][i]} successfully found in spotify")
        song_uris.append(uri)

#pprint(song_uris)

create_playlist(f"{user_date} Billboard 100", song_uris)
