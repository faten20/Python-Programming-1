#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Draw two scatter plots on the same figure
import matplotlib.pyplot as plt
import numpy as np

#first set:
x = np.array([3,5,2,1,8,19,20,3,2,15,10])
y = np.array([23,27,40,45,30,22,19,29,20,37,38])
plt.scatter(x, y)
plt.scatter(x, y, color = 'blue')
#second set:
x = np.array([4,6,3,4,9,21,22,6,1,17,12])
y = np.array([25,25,36,40,33,23,20,30,21,38,30])
plt.scatter(x, y)
plt.scatter(x, y, color = 'red')
plt.show()

# add a colormap for the points
import matplotlib.pyplot as plt
import numpy as np

x = np.array([3,6,13,19,24,27,26,32,23,29,30])
y = np.array([53,12,40,44,56,57,57,58,59,54,52])
colors = np.array([5,10,15,20,25,30,35,40,45,50,55])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.colorbar()

plt.show()


# In[ ]:





# In[ ]:




