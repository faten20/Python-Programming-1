#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Parsing the HTML content using BeautifulSoup library
#pip install requests
#pip install html5lib
#pip install bs4
import requests 
from bs4 import BeautifulSoup 
  
URL = "http://www.bbc.com/news"
a = requests.get(URL) 
  
soup = BeautifulSoup(a.content) # If this line causes an error, run 'pip install html5lib' or install html5lib 
print(soup.prettify())


# In[ ]:





# In[ ]:




