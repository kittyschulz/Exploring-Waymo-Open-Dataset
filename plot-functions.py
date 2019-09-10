from matplotlib import pyplot as plt
import pandas as pd 
import numpy as np
import math
import itertools
import os

def plot_counts_bar(df, group_column, count_column):
	counts = df.groupby(group_column).count()

	count_column_title = count_column.replace('_', ' ').title()
	group_column_title = group_column.replace('_', ' ').title()

	fig, ax = plt.subplots()
	counts[count_column].plot(kind='bar')
	plt.title(count_column_title + ' per ' + group_column_title)
	plt.show


