#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Draw a line in a diagram for the positions (5, 7),(6, 30),(7, 33),(8, 38),and (9,44)
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([5, 6, 7, 8,9])
ypoints = np.array([7, 30, 33, 38,44])

plt.plot(xpoints, ypoints)
plt.show()


# In[ ]:


#

