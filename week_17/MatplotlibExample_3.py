#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Mark each point with a star
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([11, 15, 9, 17,19,22])

plt.plot(ypoints, '*:b')
plt.show()
# Set the color of both the edge and the face to green and size of the markers to 20
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 10, mec = 'g', mfc = 'g')
plt.show()


# In[ ]:




