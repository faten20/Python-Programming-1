#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Python program to print the odd numbers from a given list
def isodd(list):
    num = []
    for a in list:
        if a % 2 == 1:
            num.append(a)
    return num
print(isodd([1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12]))


# In[ ]:




