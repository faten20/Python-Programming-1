'''

Numpy example to demonstrate numpy data type
'''
#Change data type from integer to float
import numpy as np

arr = np.array([0,1,2,3,4,5,6])

farr = arr.astype('f')

print(farr)
print(farr.dtype)
print('*'*20)

# Change data type from integer to boolean
barr = arr.astype(bool)

print(barr)
print(barr.dtype)

