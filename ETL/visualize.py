import matplotlib.pyplot as plt
from analyze import *

def view(df, metric):
	x = ['max','min','mean','median','std']
	y = stats(df, metric)
	plt.bar(x,y)
	plt.title('Playlist Stats')
	plt.xlabel('metric')
	plt.ylabel(metric)
	plt.show()

def view_percent_popularity(percetages):
	lbls = ['0-25%','25-50%','50-75%','75-100%']
	plt.pie(percetages, labels=lbls)
	plt.title('Song Popularity')
	plt.show()

def view_percent_tempo(percetages):
	lbls = ['39-81','81-122','122-164','164-205']
	plt.pie(percetages, labels=lbls)
	plt.title('Tempo Percentage (bpm)')
	plt.show()
