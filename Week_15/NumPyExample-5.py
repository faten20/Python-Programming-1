'''

numpy example to demonstrate array reshape
'''
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])

arr1 = arr.reshape(2, 6)

print(arr1)
print('*'*30)
arr2 = arr.reshape(3, 4)
print(arr2)


