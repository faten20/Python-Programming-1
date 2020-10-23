#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Python program to find maximun and minimum element of array and find the maximum element in array rows and columns 
import numpy as np 
  
arr = np.array([[1, 14, 16,17], 
                [12, 13, 22,18], 
                [20, 21, 9,23]]) 
  
# maximum element of array 
print ("largest element is:", arr.max())
print ("smallest element is:", arr.min())

# maximum element of array in rows and column
print ("array maximum elements in a row:", 
                    arr.max(axis = 1)) 
 
print ("array maximum elements in a column ", 
                        arr.max(axis = 0)) 


# In[ ]:




