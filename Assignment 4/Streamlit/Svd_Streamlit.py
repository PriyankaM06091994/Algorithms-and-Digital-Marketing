# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 22:11:48 2020

@author: Priyanka Malpekar
"""

import sys
import pandas as pd
from PIL import Image
import streamlit as st
import time

st.markdown("<h1 style='text-align: center; color: blue;'>Universal Yums!!</h1>", unsafe_allow_html=True)

    
image = Image.open('YumYum.png')

st.image(image,use_column_width=True)

def get_dataset(userID):
    serverURL="http://127.0.0.1:8000/docs#/default/read_item_SVD_recommendation_get" + userID
    req = requests.get(serverURL)
    return req.json()

st.markdown("<h1 style='text-align: left; color: blue;'>UserID</h1>", unsafe_allow_html=True)
title = st.number_input('User ID',min_value = 0,max_value=1000,value = 0,step =1)


st.markdown("<h1 style='text-align: left; color: blue;'>Choose Snack Type</h1>", unsafe_allow_html=True)
Type = st.selectbox(
        "Choose Snack Type",["India", "Thailand","America","Japan"])


if st.button('Login'):
     data = pd.read_csv(Type+".csv")  
     df1 =  data['userId']==title
     df2 =data[df1]
     if df2.empty:
         #st.write('No User Found')
         image = Image.open('UserNotFound.jpeg')
         st.image(image,use_column_width=True)
     else:
         #image = Image.open('InSnack.jpeg')
         #st.image(image,use_column_width=True)
         st.write(data[df1])
 
st.markdown("<h1 style='text-align: center; color: white;'>Customer Reviews</h1>", unsafe_allow_html=True)   
video_file = open('videoUniversalYums.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)



def get_data():
    return pd.read_csv('streamlit.csv',header=None)


st.markdown('<style>body{background-color: #FFFFFF;}</style>',unsafe_allow_html=True)
    





