# Exploratory Analysis of the Waymo Open Dataset

## Presentation and Notes

%%fill in with presentaion and notes after complete

[Waymo Open Dataset GitHub](https://github.com/waymo-research/waymo-open-dataset)

[Dataset Tutorial - Colab](https://colab.research.google.com/github/waymo-research/waymo-open-dataset/blob/r1.0/tutorial/tutorial.ipynb)

[Dataset in Google Cloud (Must Request Access)](https://console.cloud.google.com/storage/browser/waymo_open_dataset_v_1_0_0)

## Abstract

[Waymo](link-to-waymo-site) recently released their [Open Dataset](link-to-waymo-dataset). The dataset contains lidar and camera data gathered from Waymo self-driving cars. All segments are pre-labeled with all 3D annotations, and 100 of these segments have additional 2D annotations. 

This work serves to perform a high-level exploratory analysis of the labeled 3D data. Our goal is to better understand the data gathered by the Waymo self-driving cars by analyzing 3D labels and testing three (3) simple hypotheses about object distributions. 

A major focus of this analysis was on visualizing the distribution of object and frame attributes. We have also explored the relationship between environmental factors, such as location, weather, and time of day, and the distribution and amount of object types in each scene. Finally, we inspected the position of objects in respect to the Waymo car using the 3D coordinates of each bounding box and their headings. 

Ultimately, this work presents three (3) hypotheses which serve to demonstrate similiarity of the scenes in this dataset to real-world traffic conditions:

1. The majority of Vehicle class object instances have headings which lie either **parallel** or **orthogonal** to the Waymo Car. 

2. The headings Vehicle class objects are more likely to lie either **parallel** or **orthogonal** to the Waymo Car than Pedestrian class objects. 

3. Vehicle class objects are wider and longer than Pedestrian class objects.

## Motivation

After working with the KITTI dataset as an undergraduate research assistant, I became interested in the discipline of computer vision and its applications to autonomous vehicles. Waymo's recent release of a large and (relatively) diverse open dataset provides a great opportunity to explore real-world 3D and 2D scenes for autonomous vehicles. 

I wanted to perform this exploratory analysis to better understand the data contained in the Waymo Open Dataset, and to familiarize myself with the datastructures used by Google. I hope to further explore the Waymo dataset at a deeper level, including with future ML and AI projects. 

## Data Collection

The data has been packaged into a total of forty (40) '\*.tar' files, and split into a training and validation set, which contain 32 and 8 files, respectively. The total size of the compressed files is approximately 1TB. 

Each segment is stored in a [TensorFlow Record](https://www.tensorflow.org/tutorials/load_data/tf_records). Within this record are [protocol buffers](https://developers.google.com/protocol-buffers/) for each segment. Protocol buffers seriealize data in a language-agnostic way, but share some similar features to Python dictionaries. 

The files are accessed through a [Google Cloud bucket](link-to-cloud). Given the size of the data, we chose to begin the analysis on a small subset of the data, for a total of 1,000 frames, and then scale.

To collect these frames, we built a scalable pipline to download the compressed files to a virtual machine, unpack the compressed files in a bash script, read the TensorFlow Records in Python, and extract data from the protocol buffers of each frame into a Python dictionary. Each dictionary was then appended to a Pandas DataFrame for easy visualization and manipulation. 

You can access the scripts for the pipeline [here](link-to-scripts-in-github). Before running them you will need to request access to the Waymo Open Dataset storage bucket. A link to the bucket has been provided in the notes.


## Data Analysis

The data was ultimately split into two (2) Pandas DataFrames: The first includes the attributes of each scene (i.e., weather, location, time of day, and object counts). The second DataFrame contains data about each object instance (i.e., the object counts and the location and heading of each instance). Below is a portion of each Pandas DataFrame:

[INSERT SNIPPET OF PANDAS DF]

We began our analysis on 1,000 frames and then scaled to a representative sample of 8,000 frames. Within these 8,000 frames were approximately 500,000 object instances. For the purposes of this EDA, it was not necessary to scale our analysis to the entire dataset, and choosing the smaller, representative sample saved time and memory.

### Scene Data

The scene data we explored includes the attributes of weather, location, time of day, and object counts. We first vizualized the distribution of these attributes over the frames in a histogram.

![Figure 1 (a), (b), (c): Histogram of Scene Attributes](plots/time-location-weather.png)

The majority of the data were gathered in either Pheonix or San Francisco, as shown in Figure 1(b). Likely in large part to location, the weather is nearly always Sunny. Most scenes take place during the day, with only about 25 percent occuring at night or dawn/dusk combined. 

The distribution of the object counts over out sample frames is as follows:

![Figure 2: Histogram of Object Class Counts per Frame](plots/object_dist.png)

We'll explore individual object instances further, but its important to first to understand how many objects of each class we can expect in a frame. From the histograms above, it appears that we may have many frames with Pedestrian and Cyclist coutns of zero and that vehicle class objects are the most numerous, with a mean somwhere around 30 instances per frame.

Table 1: Mean, Median, and Maximum Count of Instances per Frame for Object Classes

| Object Class | Mean | Median | Max |
|:------------:|:----:|:------:|:---:|
|    Vehicle   |  30  |   27   | 163 |
|  Pedestrian  |  14  |   27   | 192 |
|    Cyclist   |   0  |    0   |  11 |
|      All     |  45  |   33   | 234 |

From the Mean, Median, and Maximum counts of the object class instances, we can see that Cyclist class objects are indeed most rare, with most frames containing no cyclists. Vehicle Class objects also have the highest *average* count, but in at least one frame there are more Pedestrian Class Objects than Vehicles!

As Waymo expands to more cities, it will be intersting to see how the distribution of object instances change; if we went to Denver, would we see more Cyclist Class Objects? If we drove around New York City, could we see an increase in the number of pedestrians? And what would the highest object counts be in the most densly-populated cities?

### Object Data




## Hypothesis Testing

## Conclusions

## Next Steps





