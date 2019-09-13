#OBJECT ATTRIBUTES PLOTS
import numpy as np
import os
import tensorflow as tf
import math
import pandas as pd
import itertools
import collections
import scipy.stats as sts

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.cbook import get_sample_data

def getImage(path):
    return OffsetImage(plt.imread(path))

def plot_obj_pc(object_type, title, legend_labels, img, alpha=0.5):
	#'Point Cloud of Object Types over 10,000 Instances'
	#("Vehicle", "Pedestrian", "Cyclist")
	#'waymo_top.png'
    
    fig, ax = plt.subplots(figsize=(10,10))
    
    for each in object_type:
        xdata = each['location_x']
        ydata = each['location_y']
        ax.scatter(xdata, ydata, alpha=alpha, s=5)
        ax.legend(loc='best')
    ax.legend(legend_labels, loc='best')
    x = 0
    y = 0
    ax.scatter(x, y) 
    ax.set_title(title)
    ab = AnnotationBbox(getImage(img), (x, y), frameon=False)
    ax.add_artist(ab)
    ax.axis('off')

def plot_obj_pc_multi(object_type, labels, img, alpha=0.25):
    #labels=['Vehicle', 'Pedestrian', 'Cyclist']
    #'waymo_top.png'
    fig, ax = plt.subplots(1, 3, figsize=(10,3))
    
    color = ['blue','orange','green','red','yellow']
    
    for i, each in enumerate(object_type):
        xdata = each['location_x']
        ydata = each['location_y']
        ax[i].scatter(xdata, ydata, alpha=alpha,s=0.25, color=color[i])
        ax[i].set_title(labels[i])
        x = 0
        y = 0
        ax[i].scatter(x, y) 
    
        ab = AnnotationBbox(getImage(img), (x, y), frameon=False)
        ax[i].add_artist(ab)
        ax[i].axis('off')

def plot_subgroup_hist(df, sub_a, sub_b):
    '''
    Displays information of 2 sub groups of a data set 
    '''
    
    fig, axs = plt.subplots(1,3, figsize=(15, 3))
    for col_name, ax in zip(df.columns, axs.flatten()):
        bins = np.linspace(df[col_name].min(), df[col_name].max(), 30)
        height, binz = np.histogram(sub_a[col_name], bins=bins, density=True)
        bp1 = ax.bar(bins[:-1], height, .5*(bins[1]-bins[0]),
                     alpha=0.5, label=sub_a, color='g')
        height, binz = np.histogram(sub_b[col_name], bins=bins, density=True)
        bp2 = ax.bar(bins[:-1]+.5*(bins[1]-bins[0]), height,
                     .5*(bins[1]-bins[0]), color='b', alpha=.5)
        ax.set_title(str(col_name).split('_', 1)[-1].title())
        ax.legend((bp1[0], bp2[0]), ("Pedestrian", "Vehicle"), loc='best')

    plt.tight_layout()

    return fig, ax

def plot_subgroup_multi_hist(df, subs, labels):
    num_subs = len(subs)
    bp = []
    fig, axs = plt.subplots(1,3, figsize=(15, 3))
    for col_name, ax in zip(df.columns, axs.flatten()):
        bins = np.linspace(df[col_name].min(), df[col_name].max(), 30)
        
        for sub in subs:
            height, binz = np.histogram(sub[col_name], bins=bins, density=True)
            bp.append(ax.bar(bins[:-1], height, .5*(bins[1]-bins[0]),
                     alpha=0.75, label=sub))
        
        ax.set_title(str(col_name).replace('_', ': ').title())
        label = tuple(i for i in labels)
        bp_leg = tuple(i[0] for i in bp)
        ax.legend(bp_leg, label, loc='best')

    plt.tight_layout()

    return fig, ax

def polar_hist(head_column, title):
	#'Histogram of Pedestrian-Type Object Headings'
	#pedestrians['heading']
	heights, angles, bars = plt.hist(head_column, bins=180);
	plt.close()
	angles_rad = np.radians(angles)[:180]

	fig, axs = plt.subplots(1,1, figsize=(10, 10))
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
		ax.set_title(title)

	plt.show()


def heading_dist(object_df):

	object_df['dist'] = object_df['heading']/90 - (object_df['heading']/90).round(0)

	fig, ax = plt.subplots(1,1, figsize=(10, 5))
	ax.hist(object_df['dist'], bins=180)
	ax.axvline(np.std(object_df['dist']), color='red', linestyle='--')
	ax.axvline(-np.std(object_df['dist']), color='red', linestyle='--')
	ax.axvline(np.mean(object_df['dist']), color='black', linestyle='--');


def one_dim_scatterplot(data, title, jitter=0.2, **options):
    #"One-Dimensional Scatterplot of Vehicle Headings with Respect to Waymo Car"
    fig, ax = plt.subplots(1, figsize=(16, 2))
    if jitter:
        jitter = np.random.uniform(-jitter, jitter, size=data.shape)
    else:
        jitter = np.repeat(0.0, len(data))
    ax.scatter(data, jitter, **options)
    ax.yaxis.set_ticklabels([])
    ax.set_ylim([-1, 1])
    ax.set_title(title);

def plot_heading_distributions(object_df, title, loc_h0=0, loc_ha=0.06, rejection=1, power=1):
	#"$H_0$ and $H_a$: Distribution of Vehicle Heading Orientation in Respect to Waymo Car"
	fig, ax = plt.subplots(figsize=(12, 4))

	h_std_error = heading_std_error(object_df)
	h0 = h0_dist(object_df)
	ha = ha_dist(object_df)

	t = np.linspace(loc_ha - 15*h_std_error, loc_ha + 15*h_std_error, num=250)
	ax.plot(t, h0.pdf(t))
	ax.plot(t, ha.pdf(t))

	if rejection == 1:
		plot_rejection_reigons(object_df, loc_h0, loc_ha)

	if power == 1:
		plot_power_reigons(object_df, loc_h0, loc_ha)

	ax.set_title()


def plot_rejection_reigons(object_df, loc_h0=0, loc_ha=0.06):
	#$H_0$ and $H_a$: Distribution of Vehicle Heading Orientation in Respect to Waymo Car"
	h_std_error = heading_std_error(object_df)
	h0 = h0_dist(object_df, loc_h0)
	ha = ha_dist(object_df, loc_ha)

	critical_value_right = h0.ppf(1 - 0.1)
	critical_value_left = h0.ppf(0.1)
    
	t = np.linspace(0 - 10*h_std_error, 0 + 10*h_std_error, num=250)

	ax.axvline(critical_value_left, color="grey", linestyle="--")
	ax.axvline(critical_value_right, color="grey", linestyle="--")

	tpos = t[t >= critical_value_right]
	ax.fill_between(tpos, 0, h0.pdf(tpos), alpha=0.2, label=r"$\alpha$")

	tneg = t[t <= critical_value_left]
    
	ax.axvline(np.mean(object_df), color='black', linewidth=2, linestyle="--")

	ax.fill_between(tneg, 0, h0.pdf(tneg), alpha=0.2, label=r"$\alpha$")
	plt.show()

def plot_power_reigons(object_df, loc_h0=0, loc_ha=0.06):
	h_std_error = heading_std_error(object_df)
	h0 = h0_dist(object_df, loc_h0)
	ha = ha_dist(object_df, loc_ha)

	critical_value_right = h0.ppf(1 - 0.1)
	critical_value_left = h0.ppf(0.1)

	t = np.linspace(np.mean(object_df) - 10*h_std_error, np.mean(object_df) + 10*h_std_error, num=250)

	ax.axvline(critical_value_left, color="grey", linestyle="--")
	ax.axvline(critical_value_right, color="grey", linestyle="--")

	tpos = t[t >= critical_value_right]
	ax.fill_between(tpos, 0, ha.pdf(tpos), alpha=0.2, label=r"$\alpha$")

	tneg = t[t <= critical_value_left]
	ax.fill_between(tneg, 0, ha.pdf(tneg), alpha=0.2, label=r"$\alpha$")
	plt.show()

def heading_std_error(object_df):
	return np.std(object_df['dist']) / np.sqrt(object_df['dist'].shape[0]) * 500

def h0_dist(object_df, loc=0):
	h_std_error = heading_std_error(object_df)
	return sts.norm(loc=loc, scale=h_std_error)

def ha_dist(object_df, loc=0.06):
	h_std_error = heading_std_error(object_df)
	return sts.norm(loc=loc, scale=h_std_error)

def H0_plot(object_df, title, loc=0):
	#"$H_0$: Distribution of Vehicle Heading Orientation in Respect to Waymo Car"
	h_std_error = heading_std_error(object_df)
	h0 = h0_dist(object_df, loc)

	fig, ax = plt.subplots(figsize=(12, 4))

	t = np.linspace(loc - 15*h_std_error, loc + 15*h_std_error, num=250)
	ax.plot(t, h0.pdf(t))
	ax.set_title(title)

