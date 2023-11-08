import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules

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


df = pd.read_csv("/content/GroceryStoreDataSet.csv", names = ['products'], sep = ',')
df.head()

df.shape

data = list(df["products"].apply(lambda x:x.split(",") ))
data

#Let's transform the list, with one-hot encoding
from mlxtend.preprocessing import TransactionEncoder
a = TransactionEncoder()
a_data = a.fit(data).transform(data)
df = pd.DataFrame(a_data,columns=a.columns_)
df = df.replace(False,0)
df

df = apriori(df, min_support = 0.2, use_colnames = True, verbose = 1)
df

#Let's view our interpretation values using the Associan rule function.
df_ar = association_rules(df, metric = "confidence", min_threshold = 0.7)
df_ar