#!/usr/bin/env python
# coding: utf-8

# In[5]:


#pie chart with a header
import matplotlib.pyplot as plt
import numpy as np

y = np.array([40, 20, 30, 10])
mylabels = ["fruit", "protien", "vegetables", "dairy"]

plt.pie(y, labels = mylabels)
plt.legend(title = "recommended diet")
plt.show()


# In[ ]:




