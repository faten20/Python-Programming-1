#!/usr/bin/env python
# coding: utf-8

# In[8]:


#draw multiple plots in one figure

import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([10, 20, 40, 60])
y = np.array([2, 3, 4, 5])

plt.subplot(2, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([10, 11, 12, 13])
y = np.array([20, 15, 22, 23])
plt.subplot(2, 2, 2)
plt.plot(x,y)

#plot 3:
x = np.array([9, 8, 7, 6])
y = np.array([11, 2, 3, 5])
plt.subplot(2, 2, 3)
plt.plot(x,y)

#plot 4:

x = np.array([10, 11, 12, 13])
y = np.array([11, 30, 40, 70])
plt.subplot(2, 2, 4)
plt.plot(x,y)


plt.show()


# In[ ]:




