'''
creating 1d 2d and 3d array using Numpy

'''

import numpy as np
 
arr1d = np.array([10, 11, 12, 13, 14, 15,16])
arr2d = np.array([[10, 11, 12], [13, 14, 15]])
arr3d = np.array([[[ 10,  11,  12],
                 [ 13,  14,  15],
                 [ 16,  17,  18]],

                [[ 19, 20, 21],
                 [22, 23, 24],
                 [25, 26, 27]],

                [[28, 29, 30],
                 [31, 32, 33],
                [34, 35, 36]]])
 
print(arr1d)
 
print("*" * 22)
print(arr2d)
print("*" * 22)
print(arr3d)
