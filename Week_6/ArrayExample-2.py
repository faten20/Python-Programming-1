# python program to concatenate two arrays then remove 4th element of the output array

import array as arr

arr1 = arr.array('i', [1, 2, 3])
arr2 = arr.array('i', [4, 5, 6])

num = arr.array('i')   # creating empty array of integer
num = arr1 + arr2
del num[3]  # removing 4th element

print(num)