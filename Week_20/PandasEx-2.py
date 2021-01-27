#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Remove all rows with NULL values
import pandas as pd

df = pd.read_csv('AirPassengers.csv')

df.dropna(inplace = True)

print(df.to_string())


# In[ ]:




