'''
create a 2d array with 4 rows, each row containing 6 random integers from 0 to 50

'''

from numpy import random

arr = random.randint(50, size=(4, 6))

print(arr)

