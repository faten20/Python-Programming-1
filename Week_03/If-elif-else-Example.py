#!/usr/bin/env python
# coding: utf-8

# In[9]:


#python program to ask the user to enter a number and check if the entered number is one digit,two digit,three digit,or 4 digit

num = int(input("Enter a number: "))
if num<=9:
    print("one digit number")  
elif 9 < num < 99:
    print("Two digit number")
elif 99 < num < 999:
    print("Three digit number")
elif 999 < num < 9999:
    print("Four digit number")
else:
    print("enter number between 0 and 9999")


# In[ ]:




