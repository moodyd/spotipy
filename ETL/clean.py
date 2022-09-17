import pandas as pd
import numpy as np

columns = [
	'artist','album','track_name',
	'track_id','popularity','danceability',
	'energy','key','loudness','mode',
	'speechiness','instrumentalness',
	'liveness','valence','tempo',
	'duration_ms','time_signature'
]

df0 = pd.read_csv('inf/dirty/my_playlist_unclean.csv', index_col=0)
df1 = pd.read_csv('inf/dirty/toptracks2018.csv', index_col=0)
df2 = pd.read_csv('inf/dirty/toptracks2019.csv', index_col=0)
df3 = pd.read_csv('inf/dirty/toptracks2020.csv', index_col=0)
df4 = pd.read_csv('inf/dirty/toptracks2021.csv', index_col=0)

def clean_df1(df):
	df = df.rename(columns={
			'id':'track_id',
			'name':'track_name',
			'artists':'artist'})
	df = df.drop(['acousticness'], axis=1)
	df = df.reindex(columns=columns)
	return df.head(50)

def clean_df2(df):
	df = df.rename(columns={
			'title':'track_name',
			'dnce':'danceability',
			'dB':'loudness',
			'nrgy':'energy',
			'pop':'popularity',
			'spch':'speechiness',
			'live':'liveness',
			'val':'valence',
			'bpm':'tempo',
			'dur':'duration_ms'})
	df = df.drop(['top genre','acous','added','country'],axis=1)
	df = df.reindex(columns=columns)
	return df.head(50)
	
def clean_df3(df):
	df = df.drop(['genre'], axis=1)
	return df.reindex(columns=columns).head(50)	

def clean_df4(df):
	df = df.rename(columns={'artist_name':'artist'})
	df = df.drop(['acousticness'], axis=1)
	return df.reindex(columns=columns)

def dups(df):
	c = ['artist','track_name']
	d1 = df[df[c].duplicated(subset=c, keep=False)][c]
	d2 = d1.drop_duplicates()
	i1 = list(d1.index.values)
	i2 = list(d2.index.values)
	for i in i1:
		if i in i2:
			i1.remove(i)
	return i1

def clean_my_playlist(df):
	df.drop(dups(df), axis=0, inplace=True)
	df['duration_ms'] = df['duration_ms']/60000
	return df.rename(columns={'duration_ms':'duration_m'})
	
def clean_top50():
	top50 = pd.concat([clean_df1(df1),clean_df2(df2),clean_df3(df3),clean_df4(df4)]).fillna(np.nan)
	top50['duration_ms'] = top50['duration_ms']/60000
	return top50.rename(columns={'duration_ms':'duration_m'})

def save():
	clean_my_playlist(df0).to_csv('inf/clean/my_playlist.csv', index=False)
	clean_top50().to_csv('inf/clean/top50.csv', index=False)

save()

###########################################################################################################

#iteration 2.0 pull genre and album

# d = data_pull('3wLg8O1LOBDOL72pDIDf5g')
# track = d[41]['track']
# # artist = sp.artist(track["artists"][0]["external_urls"]["spotify"])
# album = sp.album(track["album"]["external_urls"]["spotify"])
# print(album)

###########################################################################################################






