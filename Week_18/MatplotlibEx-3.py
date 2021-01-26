#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Add a plot title and labels for the x- and y-axis
import numpy as np
import matplotlib.pyplot as plt

x = np.array(['8/5/2020','9/5/2020','10/5/2020','11/5/2020','12/5/2020','13/5/2020','14/5/2020'])
y = np.array([24,24,23,26,27,27,29])

plt.plot(x, y)

plt.title("FTSE100 Stock")
plt.xlabel("date")
plt.ylabel("stock price")

#Add grid lines to the plot
plt.grid()
plt.show()


# In[ ]:




