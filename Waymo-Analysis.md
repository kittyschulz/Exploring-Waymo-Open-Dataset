# Exploratory Analysis of the Waymo Open Dataset

## Presentation and Notes

%%fill in with presentaion and notes after complete

[Waymo Open Dataset GitHub]()

[Dataset Tutorial - Colab]()

## Abstract

[Waymo](link-to-waymo-site) recently released their [Open Dataset](link-to-waymo-dataset). The dataset contains lidar and camera data gathered from Waymo self-driving cars. This data is pre-labeled with all 3D annotations and 2D annotations on 100 segments. 

This work serves to perform a high-level exploratory analysis of the labeled 3D data. A major focus of this analysis was on the relationship between environmental factors, such as location, weather, and time of day, and the distribution and amounts of object types in each scene.

The location of objects in respect to the Waymo car was also examined in an attempt 

Ultimately, this work presents three (3) hypotheses which serve to explore the similiarity of the scenes contained in this dataset to how we as humans typically percieve traffic behaviour. 

## Motivation

After working with the KITTI dataset as an undergraduate research assistant, I became interested in the discipline of computer vision and its applications to autonomous vehicles. Waymo's recent release of a large and diverse open dataset provides a great opportunity to explore real-world 3D and 2D scenes for autonomous vehicles. 

I wanted to perform this exploratory analysis to better understand the data contained in the Waymo Open Dataset, and to familiarize myself with the datastructures used by Google. I hope to further explore the Waymo dataset at a deeper level, including with future ML and AI projects. 

## Data Collection

The data has been packaged into a total of forty (40) '\*.tar' files, and split into a training and validation set, containing 32 files and 8 files, respectively. The total size of the **compressed** files is approximately 1 terebyte. 

Each frame is stored in a TensorFlow Record. Within this record, [protocol buffers]() store the data for each frame in a language-agnostic way.  

The files are access through a [Google Cloud bucket](link-to-cloud). Given the size of the data, I chose to begin my analysis on a small subset of the data, for a total of 1,000 frames.

To collect these frames, I built a scalable pipline to unzip(?) the compressed files, read the TensorFlow Records, and extract the 'Stats' data from the protocol buffers of each frame in a Python dictionary. Each dictionary was then appended to a Pandas DataFrame for easy visualization. 

## Data Analysis

Each of the protocol buffers is very large, and I ultimately chose only a small subset of the data contained within each of them to explore. 

This EDA 








