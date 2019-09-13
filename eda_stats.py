#OBJECT ATTRIBUTES PLOTS
import numpy as np
import os
import tensorflow as tf
import math
import pandas as pd
import itertools
import collections
import scipy.stats as sts

def utest(obj_a, obj_b, attribute):
	res_lst = []
	for i in range(100):
		res = sts.mannwhitneyu(obj_a[attribute].sample(100), obj_b[attribute].sample(100))
		res_lst.append(res.pvalue)
	return np.mean(np.array([res_lst]))

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), sts.sem(a)
    h = se * sts.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h