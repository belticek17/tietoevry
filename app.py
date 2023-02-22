from flask import Flask, render_template
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__, template_folder='template')
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="your_client_id",
                                                   client_secret="your_client_secret"))
def get_artist_id(artist_name):
    results = sp.search(q=artist_name, type='artist')
    return results['artists']['items'][0]['id']

def get_top_tracks(artist_id):
    top_tracks = sp.artist_top_tracks(artist_id)
    return top_tracks['tracks'][:10]

def get_album_info(album_id):
    album = sp.album(album_id)
    album_name = album['name']
    album_genres = album['genres']
    # if you want to print those values, even though it's an empty string use the line of code below
    # album_genres = ', '.join(album['genres'])
    album_cover_url = album['images'][0]['url'] if album['images'] else None
    return album_name, album_genres, album_cover_url

@app.route('/')
def index():
    artist_id = get_artist_id('Ed Sheeran')
    top_tracks = get_top_tracks(artist_id)

    table_data = []
    i = 1
    for track in top_tracks:
        album_id = track['album']['id']
        album_name, album_genres, album_cover_url = get_album_info(album_id)
        table_data.append((i, track['name'], track['id'], track['popularity'], album_name, album_cover_url, album_genres))
        i += 1

    return render_template('index.html', table_data=table_data)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=int(5000), debug=True)