from matplotlib import pyplot as plt
import pandas as pd 
import numpy as np
import math
import itertools
import os

def plot_bar_counts(df, group_column, count_column):
	counts = df.groupby(group_column).count()

	count_column_title = count_column.replace('_', ' ').title()
	group_column_title = group_column.replace('_', ' ').title()

	fig, ax = plt.subplots()
	counts[count_column].plot(kind='bar')
	plt.title(count_column_title + ' per ' + group_column_title)
	plt.show;

def plot_hist_counts(df, hist_column, bins=10):
	hist_column_title = hist_column.replace('_', ' ').title()

	fig, ax = plt.subplots()
	hist = df[hist_column].hist(bins)
	plt.title('Histogram of ' + hist_column_title + ' Distribution')
	plt.xlabel(hist_column_title)
	plt.show;

#histograms/bar charts of things like weather, time of day, location
#plot counts of classes
#plot counts of classes based on time of day
#get orientation of bounding boxes?
