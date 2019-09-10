import os
import itertools
import tensorflow as tf
import pandas as pd
import numpy as np
import re

def extract_frame_data(frame):
  frame_data = {                     
       'time_of_day': frame.context.stats.time_of_day,
       'location': frame.context.stats.location,
       'weather': frame.context.stats.weather
    }
  object_counts = {object_type_name(x.type): x.count for x in frame.context.stats.laser_object_counts}
  frame_data.update(object_counts)
  
  object_count = collections.Counter([object_type_name(x.type) for x in frame.laser_labels])
  print(object_count)
  
  return frame_data


frame_df = pd.DataFrame()
FILENAME = '/content/waymo-od/tutorial/frames'
dataset = tf.data.TFRecordDataset(FILENAME, compression_type='')
for data in dataset:
    frame = open_dataset.Frame()
    print('Parsing frame')
    frame.ParseFromString(bytearray(data.numpy()))
    frame_data = extract_frame_data(frame)
    frame_df = frame_df.append(frame_data, ignore_index=True)

frame_df.head()


def object_type_name(x):
  return label_pb2.Label.Type.Name(x)
