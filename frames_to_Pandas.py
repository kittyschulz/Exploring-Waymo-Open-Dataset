import os
import itertools
import tensorflow as tf
import pandas as pd
import numpy as np

def frames_to_Pandas(waymo_frame):
  """
  inputs: takes single waymo Frame proto.
  outputs: adds rows to existing Pandas DataFrame

  """
  frame_string = frame_string[frame_string.find('stats')+5:].replace(' ','').replace('\n','')
  pass
  

