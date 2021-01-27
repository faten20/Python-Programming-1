#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Load the CSV into a DataFrame and then print the entire dataframe
import pandas as pd

df = pd.read_csv('AirPassengers.csv')
# use to_string() to print the entire DataFrame

print(df.to_string())

#print part of dataframe

df = pd.read_csv('AirPassengers.csv')

print(df)


# In[ ]:




