import cred
import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
	auth_manager = SpotifyOAuth(
	client_id=cred.client_id,
   	client_secret=cred.client_secret,
   	redirect_uri=cred.redirect_uri,
   	scope='user-library-read'))

columns = [
	'artist','album','track_name',
	'track_id','popularity','danceability',
	'energy','key','loudness','mode',
	'speechiness','instrumentalness',
	'liveness','valence','tempo',
	'duration_ms','time_signature'
]

def pull():
	r = sp.user_playlist_tracks(
		'Spotify', 
		'3wLg8O1LOBDOL72pDIDf5g')
	data = r['items']
	while r['next']:
		r = sp.next(r)
		data.extend(r['items'])
	return data

def playlist():
	tracks = pull()
	playlist = []
	playlist_df = pd.DataFrame(columns=columns)
	for track in tracks:
		t = {}
		t['artist'] = track['track']['album']['artists'][0]['name']
		t['album'] = track['track']['album']['name']
		t['track_name'] = track['track']['name']
		t['track_id'] = track['track']['id']
		t['popularity'] = track['track']['popularity']
		audio_features = sp.audio_features(track['track']['id'])[0]
		for feature in columns[5:]:
			t[feature] = audio_features[feature]
		track_df = pd.DataFrame(t, index=[0])
		playlist_df = pd.concat([playlist_df, track_df], ignore_index=True)
	return playlist_df	

def save(playlist):
	playlist.to_csv('inf/my_playlist_unclean.csv')
		
save(playlist())







