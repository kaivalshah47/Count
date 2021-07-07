# -*- coding: utf-8 -*-
"""
Created on Thu May 27 15:21:13 2021

@author: kaivals
"""
from datetime import datetime
import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

st.title('AQA- FTP Files Name and Count')

st.markdown(""" 
      This app performs day-wise counting of  files and Bar Chart.  
      """
      )



df = pd.read_csv ('count.csv')


# df["Date"]=pd.to_datetime(df["Date"])
df=df.sort_values(by="Date",ascending=False)
st.write(df)

st.title('Bar Chart')

df1=df.iloc[:35,:]
plt.figure(figsize=(50,25), dpi=100)

fig,b1=plt.subplots()
b1.bar(df1['Date'], df1['Count'], width=0.5)
for i, val in enumerate(df1['Count'].values):
   plt.text(i, val, int(val), horizontalalignment='center',rotation=60, verticalalignment='bottom', fontdict={'fontweight':200, 'size':6})
plt.gca().set_xticklabels(df1['Date'],rotation=60, horizontalalignment= 'right',fontsize=6)
plt.title("AQA FTP Files Day-wise counting", fontsize=12)
plt.ylabel('Counts of Files',fontsize=8)

st.pyplot(fig)


