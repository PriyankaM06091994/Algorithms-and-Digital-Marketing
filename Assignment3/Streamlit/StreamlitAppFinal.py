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


global content 
global filename 

def stringToRGB(base64_string):
    imgdata = base64.b64decode(base64_string)
    image = Image.open(io.BytesIO(imgdata))
    return np.array(image)

def cosineSim(a1,a2):
    sum = 0
    suma1 = 0
    sumb1 = 0
    for i,j in zip(a1, a2):
        suma1 += i * i
        sumb1 += j*j
        sum += i*j
    cosine_sim = sum / ((sqrt(suma1))*(sqrt(sumb1)))
    return cosine_sim


def main():
    #"""Run this function to display the Streamlit app"""
   # st.info(__doc__)
    #st.markdown(STYLE, unsafe_allow_html=True)
    st.title("Visual Search")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Search 10 Similar Images </h2>
    </div>
"""
    st.markdown(html_temp,unsafe_allow_html=True)

    
    FILE_TYPES = ["csv", "py", "png", "jpg"]
    file = st.file_uploader("Upload file", type=FILE_TYPES)
    show_file = st.empty()
    if not file:
        show_file.info("Please upload a file of type: " + ", ".join(FILE_TYPES))
        return
    content = file.getvalue()
    st.write("-----------")
    #st.write(file)
    #st.write(content)
    filename = "result.jpg"
    with open("result.jpg", "wb") as f:
      f.write(content)
    # IMAGE INTO VECTOR
    helper = TensorVector(FileName='result.jpg')
    vector = helper.process()
    
    res = base64.b64encode(content)
    base64data = res.decode("UTF-8")
    
    a1_vector=vector
    a1_image = base64data
    IMAGE_VECTOR = vector
    
    fig, ax = plt.subplots(2, figsize=(18,10))
    ax[0].imshow(stringToRGB(a1_image))
    st.pyplot()
    
    counter = 0
    IMG   = []
    FILE  = []
    VEC   = []

    for vector in df.iterrows():
      FileName =  vector[1][0] # Grabs the Filename of the image
      Vector_ = vector[1][1] # Grabs the vector of the image
      Vector_ = ast.literal_eval(Vector_) # Converting a String into list
      Image = vector[1][2] # Image is basically a Base data of that image

      sim = cosineSim(Vector_,IMAGE_VECTOR) # For each Image..we are computing Cosine Similarity

      if (float(sim) > 0.72):
       counter = counter + 1 # to track..the count of images
       IMG.append(Image)
       VEC.append(Vector_)
       FILE.append(FileName)
      
      if counter ==10: #displaying 10 images
        break 
    fig, ax = plt.subplots(10, figsize=(20,30),dpi = 80)

    for i in range(0,10):
       ax[i].imshow(stringToRGB(IMG[i]), interpolation='nearest')
    st.pyplot()

    if st.button("About"):
       st.text("Developers-Jui and Priyanka")
       st.text("Built with Streamlit")
    
main()








