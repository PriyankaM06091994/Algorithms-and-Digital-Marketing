# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 14:49:41 2020

@author: Priyanka Malpekar
"""

# In[ ]:
try:

    import streamlit as st
    from IPython import get_ipython
    from PIL import Image
    import io
    import matplotlib.pyplot as plt
    from math import sqrt
    import pandas as pd
    import ast
    import base64
    import numpy as np
    import os
    import os
    import streamlit as st
    import tensorflow as tf
    import tensorflow_hub as hub
    import numpy as np
    import os
    #get_ipython().run_line_magic('matplotlib', 'inline')
except Exception as e:
    pass

df = pd.read_csv("/Users/Priyanka Malpekar/Desktop/Project_Demo/finalData.csv")
df = df.drop("Unnamed: 0", axis=1)


# STep 1:
# Read the image
# Store image on computer
# result.jog
# Convert image into Vector
# base 64

global embed
embed = hub.KerasLayer(os.getcwd())

class TensorVector(object):

    def __init__(self, FileName=None):
        self.FileName = FileName

    def process(self):
        img = tf.io.read_file(self.FileName)
        img = tf.io.decode_jpeg(img, channels=3)
        img = tf.image.resize_with_pad(img, 224, 224)
        img = tf.image.convert_image_dtype(img,tf.float32)[tf.newaxis, ...]
        features = embed(img)
        feature_set = np.squeeze(features)
        return list(feature_set)
