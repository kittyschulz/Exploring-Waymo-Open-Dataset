# Exploratory Analysis of the Waymo Open Dataset

## Presentation and Notes

%%fill in with presentaion and notes after complete

[Waymo Open Dataset GitHub]()

[Dataset Tutorial - Colab]()

## Abstract

[Waymo](link-to-waymo-site) recently released their [Open Dataset](link-to-waymo-dataset). The dataset contains lidar and camera data gathered from Waymo self-driving cars. All segments are pre-labeled with all 3D annotations, and 100 of these segments have additional 2D annotations. 

This work serves to perform a high-level exploratory analysis of the labeled 3D data. Our goal is to better understand the data gathered by the Waymo self-driving cars by analyzing 3D labels and testing three (3) simple hypotheses about object distributions. 

A major focus of this analysis was on visualizing the distribution of object and frame attributes. We have also explored the relationship between environmental factors, such as location, weather, and time of day, and the distribution and amount of object types in each scene. Finally, we inspected the position of objects in respect to the Waymo car using the 3D coordinates of each bounding box and their headings. 

Ultimately, this work presents three (3) hypotheses which serve to demonstrate similiarity of the scenes in this dataset to real-world traffic conditions:

1. 

2.

3. 

## Motivation

After working with the KITTI dataset as an undergraduate research assistant, I became interested in the discipline of computer vision and its applications to autonomous vehicles. Waymo's recent release of a large and (relatively) diverse open dataset provides a great opportunity to explore real-world 3D and 2D scenes for autonomous vehicles. 

I wanted to perform this exploratory analysis to better understand the data contained in the Waymo Open Dataset, and to familiarize myself with the datastructures used by Google. I hope to further explore the Waymo dataset at a deeper level, including with future ML and AI projects. 

## Data Collection

The data has been packaged into a total of forty (40) '\*.tar' files, and split into a training and validation set, which contain 32 and 8 files, respectively. The total size of the compressed files is approximately 1TB. 

Each segment is stored in a TensorFlow Record. Within this record, [protocol buffers]() store the data for each frame in a language-agnostic way.

The files are access through a [Google Cloud bucket](link-to-cloud). Given the size of the data, we chose to begin the analysis on a small subset of the data, for a total of 1,000 frames, and then scale.

To collect these frames, we built a scalable pipline to unpack the compressed files, read the TensorFlow Records, and extract data from the protocol buffers of each frame into a Python dictionary. Each dictionary was then appended to a Pandas DataFrame for easy visualization and manipulation. 

The pipeline consists of a bash script to download and unpack the tarballs and a Python script to extract data from protocol buffers to a dictionary and ultimately a Pandas dataframe. You can access the scripts for this process [here](link-to-scripts-in-github). Before running them you will need to request access to the Waymo Open Dataset storage bucket.

## Data Analysis

A small subset of the data within each protocol buffer was selected for this analysis. The data was split into two (2) Pandas DataFrames. The first includes environmental data about each scene (i.e., weather, location, and time of day). The second DataFrame contains data about each object type and object instance (i.e., the object counts and the location and heading of each instance). Below is a portion of each Pandas DataFrame:

[INSERT SNIPPET OF PANDAS DF]

### Scene Data

The scene data we explored includes environmental data such as weather, location, and time of day. We first vizualized the distribution of attributes over the frames.

[ENVIRONMENT PLOTS]

The majority of the data were gathered in either Pheonix or San Francisco, as shown in Figure 1(a). Likely in large part to location, the distribution of we

### Object Data








