'''
Generate a 2-D array that consists of the following values (2, 4, 6, and 8):

'''
from numpy import random

x = random.choice([2, 4, 6, 8], size=(3, 4))

print(x)