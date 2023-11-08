import json
import time
import requests
import streamlit as st
import pandas as pd

import streamlit as st

def main():
    # ส่วนของเรนเดอร์ของกรอบสีเหลี่ยม
    st.markdown(
        """
        <style>
        .rectangle {
            height: 100px;
            width: 200px;
            background-color: #4e98c4;
            border: 2px solid #1f4251;
            border-radius: 10px;
            text-align: center;
            color: white;
            font-size: 24px;
            line-height: 100px;
        }
        </style>
        """
    )

    # ส่วนของเนื้อหาในกรอบสีเหลี่ยม
    st.markdown(
        """
        <div class="rectangle">
        นี่คือกรอบสีเหลี่ยม
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    main()


st.header("Show Data Index Price")
df=pd.read_csv("data/stock_index_price-2.csv")
st.write(df.head(10))

chart_data = pd.read_csv("data/stock_index_price-2.csv")


st.header("Show chart")
st.line_chart(
   chart_data, x="stock_index_price", y=["interest_rate", "unemployment_rate"], color=["#FF0000", "#0000FF"]  # Optional
)