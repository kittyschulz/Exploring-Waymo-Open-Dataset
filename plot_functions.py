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

def plot_obj_pc(object_type, color='b', alpha=0.1):
	ax = plt.axes()

	xdata = object_type['location_x']
	ydata = object_type['location_y']
	ax.scatter(xdata, ydata, c=color, alpha=alpha)

	waymo_y = 0
	waymo_x = 0
	ax.scatter(waymo_x, waymo_y, c='k');

