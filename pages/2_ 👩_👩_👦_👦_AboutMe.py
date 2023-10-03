import json
import time
import requests
import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

st.header("Show data index Price")
df=pd.read_csv('c:\Users\ACER\Downloads\stock_index_price-2.csv')

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/d2db8988-54be-44ed-8b65-90e808b07086/lIEFX25x4k.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello, key="hello")

