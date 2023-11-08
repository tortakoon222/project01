import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules

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