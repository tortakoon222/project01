import json
import time
import requests
import streamlit as st
import pandas as pd

st.header("Show Data Index Price")
df=pd.read_csv("c:\Users\ACER\Downloads\stock_index_price-2.csv")
st.write(df.head(10))
