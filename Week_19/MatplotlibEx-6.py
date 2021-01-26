#!/usr/bin/env python
# coding: utf-8

# In[11]:


# draw bar graphs
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["1/2/2020", "2/2/2020", "3/2/2020", "4/2/2020","5/2/2020","6/2/2020"])
y = np.array([23, 45, 34, 56,70,82])

plt.bar(x,y)
plt.show()

#random distributions for weights of 200 people


x = np.random.normal(300, 1, 200)

plt.hist(x)
plt.show()


# In[ ]:




