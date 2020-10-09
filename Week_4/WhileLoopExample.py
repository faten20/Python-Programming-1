#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Prints all letters in the string "I learn python" except the letter 'I'  
i = 0
str = 'I learn python'

while i < len(str): 
	if str[i] == 'I': 
		i += 1
		continue
	print('printing Letter :', str[i]) 
	i += 1


# In[ ]:




