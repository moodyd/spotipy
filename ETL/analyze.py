import pandas as pd
import scipy.stats as sc
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
from load import *

columns = [
	'artist','album','track_name',
	'track_id','popularity','danceability',
	'energy','key','loudness','mode',
	'speechiness','instrumentalness',
	'liveness','valence','tempo',
	'duration_m','time_signature'
]

class Stats:

	def __init__(self, x):
		self.x = x[columns]
	
	def max(self, m):
		return self.x[m].max()

	def min(self, m):
		return self.x[m].min()

	def mean(self, m):
		return self.x[m].mean()
		
	def median(self, m):
		return self.x[m].median()
		
	def stdev(self, m):
		return sc.tstd(self.x[m])

def stats(df, metric):
	a = Stats(df)
	mx = a.max(metric)
	mn = a.min(metric)
	mea = a.mean(metric)
	med = a.median(metric)
	std = a.stdev(metric)
	return [mx, mn, mea, med, std]

def match(df1, df2):
	a = artists(df1)
	b = artists(df2)
	return list(set(a).intersection(b))	

def 	(df, m1, m2):
	metrics = columns[5:]
	if ((m1 and m2) in metrics) and (m1 != m2) :
		corr = sc.pearsonr(m1,m2)
		return corr
	else:
		print('Please choose two different metrics.')









































