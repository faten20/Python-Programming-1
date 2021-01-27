#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Replace any empty values in the table with a MEAN value after calculating it .
import pandas as pd

df = pd.read_csv('AirPassengers.csv')

x = df["Passengers"].mean()

df["Passengers"].fillna(x, inplace = True)
print(df.to_string())


# In[ ]:




