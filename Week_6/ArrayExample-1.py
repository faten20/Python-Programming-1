# python program to change 4th to 6th element of array
import array as arr1

num = arr1.array('i', [2,2,2,2,2,2,2,2,2])

num[3:5] = arr1.array('i', [6, 7, 8])   
print(num)    