import os
import itertools
import math
import tensorflow as tf
import pandas as pd
import numpy as np
import re
import collections

from waymo_open_dataset.utils import range_image_utils
from waymo_open_dataset.utils import transform_utils
from waymo_open_dataset.utils import frame_utils
from waymo_open_dataset import dataset_pb2 as open_dataset
from waymo_open_dataset import label_pb2

def extract_frame_data(frame):
  frame_data = {                     
       'time_of_day': frame.context.stats.time_of_day,
       'location': frame.context.stats.location,
       'weather': frame.context.stats.weather
    }
  object_counts = {object_type_name(x.type): x.count for x in frame.context.stats.laser_object_counts}
  frame_data.update(object_counts)
  object_count = collections.Counter([object_type_name(x.type) for x in frame.laser_labels])
  #print(object_count)
  return frame_data

def import_frames(path, FILENAMES):
  frame_df = pd.DataFrame()
  for file in FILENAMES:
    dataset = tf.data.TFRecordDataset(path+file, compression_type='')
    for data in dataset:
      frame = open_dataset.Frame()
      print('Parsing frame ' + str(data) + ' of ' + file)
      frame.ParseFromString(bytearray(data.numpy()))
      frame_data = extract_frame_data(frame)
      frame_df = frame_df.append(frame_data, ignore_index=True)

def object_type_name(x):
  return label_pb2.Label.Type.Name(x)

def get_tf_files(path):

  files = []
  # r=root, d=directories, f = files
  for r, d, f in os.walk(path):
    for file in f:
      if '.tfrecord' in file:
        files.append(os.path.join(r, file))
        
  return files