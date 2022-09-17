import pandas as pd
import numpy as np

def songs(df, artist):
	c = ['artist','track_name']
	return list(df[c][df[c[0]] == artist][c[1]])

def popularity(df, artist):
	c = ['artist','track_name','popularity']
	p = df[c][df[c[0]] == artist][c[2]]
	return sum(p)/len(p)

def popularity_percentage(df):
	pop = list(df['popularity'].values)
	p1 = quartile(pop,0,25)
	p2 = quartile(pop,25,50)
	p3 = quartile(pop,50,75)
	p4 = quartile(pop,75,100)
	return [p1,p2,p3,p4]

def quartile(metric, lower, upper):
	q = []
	for p in metric:
		if (p >= lower and p < upper):
			q.append(p)
	return len(q)/len(metric)*100	

def tempo_percentage(df):
	tempo = list(df['tempo'].values)
	p1 = quartile(tempo, 39.497, 81.08425)
	p2 = quartile(tempo, 81.08425, 122.6715)
	p3 = quartile(tempo, 122.6715, 164.25875)
	p4 = quartile(tempo, 164.25875, 205.846)
	return [p1,p2,p3,p4]

def artists(df, year=None):
	if (year and df.equals(top50)):
		dfs = np.array_split(df, 4)
		return list(dfs[int(year)-2017]['artist'].unique())
	else:
		return list(df['artist'].unique())

def artists_count(year): #dataframe
	dfs = np.array_split(read()[1], 4)
	return dfs[int(year)-2017]['artist'].value_counts()
	
def match_by_year(year1, year2):
	return list(set(year1).intersection(year2))	

def match_by_playlist(df1, df2):
	return list(set(artists(df1)).intersection(artists(df2)))		

def sort(df, column):
	return df.sort_values(by=[column], ascending=False)


























# def more_likely_than_not(): #danceability and valence 
# 	c =['artist','track_name','danceability','valence']
# 	heat = read()[0]
# 	d = heat[c][heat[c[2]] > .5]
# 	v = heat[c][heat[c[3]] > .5]
# 	dd = len(d)/len(heat)
# 	vv = len(v)/len(heat)
# 	return [dd,vv]

