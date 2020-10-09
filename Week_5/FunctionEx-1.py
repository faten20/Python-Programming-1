#!/usr/bin/env python
# coding: utf-8

# In[22]:


#Python function to find the Min of four numbers
def min_of_two( x, y ):
    if x < y:
        return x
    return y
def min_of_three( x, y, z ):
    return min_of_two( x, min_of_two( y, z ) )
def min_of_four( x, y, z,n ):
    return min_of_two( x, min_of_three( y, z ,n) )

print(min_of_four(3, 2, 5,1))


# In[ ]:





# In[ ]:





# In[ ]:




