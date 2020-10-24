
# Python program to sort the element in array then find the number of nonzero array elements 
import numpy as np 
  
a = np.array([3,1,20,12, 4, 2,0]) 
  
# array sort 
print ("Array elements in sorted order:\n", 
                    np.sort(a, axis = None))
print('*'*25)

# number of non zero elements
c=np.count_nonzero(a)

 
print("Number of nonzero elements is :",c)
