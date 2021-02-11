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
	plt.title(group_column_title)
	plt.show;

def plot_hist_counts(df, hist_column, bins=10):
	hist_column_title = hist_column.replace('_', ' ').title()

	fig, ax = plt.subplots()
	hist = df[hist_column].hist(bins)
	plt.title('Histogram of ' + hist_column_title + ' Distribution')
	plt.xlabel(hist_column_title)
	plt.show;

def getImage(path):
    return OffsetImage(plt.imread(path))

def plot_obj_pc(object_type, alpha=0.5):
    
    fig, ax = plt.subplots(figsize=(10,10))
    
    for each in object_type:
        xdata = each['location_x']
        ydata = each['location_y']
        ax.scatter(xdata, ydata, alpha=alpha, s=5)
        ax.legend(loc='best')
    ax.legend(("Vehicle", "Pedestrian", "Cyclist"), loc='best')
    x = 0
    y = 0
    ax.scatter(x, y) 
    ax.set_title('Point Cloud of Object Types over 10,000 Instances')
    ab = AnnotationBbox(getImage('waymo_top.png'), (x, y), frameon=False)
    ax.add_artist(ab)
    ax.axis('off')

def plot_obj_pc_multi(object_type, alpha=0.25):
    
    fig, ax = plt.subplots(1, 3, figsize=(10,3))
    
    color = ['blue','orange','green']
    labels =['Vehicle', 'Pedestrian', 'Cyclist']
    
    for i, each in enumerate(object_type):
        xdata = each['location_x']
        ydata = each['location_y']
        ax[i].scatter(xdata, ydata, alpha=alpha,s=0.25, color=color[i])
        ax[i].set_title(labels[i])
        x = 0
        y = 0
        ax[i].scatter(x, y) 
    
        ab = AnnotationBbox(getImage('waymo_top.png'), (x, y), frameon=False)
        ax[i].add_artist(ab)
        ax[i].axis('off')

def plot_subgroup_hist(df, subs):
    num_subs = len(subs)
    bp = []
    fig, axs = plt.subplots(1,3, figsize=(15, 3))
    for col_name, ax in zip(df.columns, axs.flatten()):
        bins = np.linspace(df[col_name].min(), df[col_name].max(), 30)
        
        for sub in subs:
        	height, binz = np.histogram(sub[col_name], bins=bins, density=True)
        	bp.append(ax.bar(bins[:-1], height, .5*(bins[1]-bins[0]),
                     alpha=0.5, label=sub, color='g'))
        
        #height, binz = np.histogram(sub_b[col_name], bins=bins, density=True)
        #bp2 = ax.bar(bins[:-1]+.5*(bins[1]-bins[0]), height,
        #            .5*(bins[1]-bins[0]), color='b', alpha=.5)
        ax.set_title(col_name)
        ax.legend((i[0] for i in bp), (sub for sub in subs), loc='best')

    plt.tight_layout()

    return fig, ax

def polar_hist(df_column):
	heights, angles, bars = plt.hist(objects_df['heading'], bins=180)
	plt.close() #because we don't want to display this lame-o histogram!

	fig, axs = plt.subplots(1,1, figsize=(10, 10))
	angles_rad = np.radians(angles)[:180] #it gives us both -pi and pi so we have to hack one off!
	N = 180
	bottom = 1

	theta = angles_rad
	radii = (heights)**(1/np.pi)
	width = (2*np.pi) / N

	ax = plt.subplot(111, polar=True)
	bars = ax.bar(theta, radii, width=width, bottom=bottom)

	# Use custom colors and opacity
	for r, bar in zip(radii, bars):
    	bar.set_facecolor(plt.cm.jet(r / 10.))
    	bar.set_alpha(0.8)

	plt.show()
