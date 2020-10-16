 #a Python program to print the numbers of a  list after removing odd numbers from it
num = [9,7, 20, 22, 50, 13, 14,15,17,90]
num = [i for i in num if i%2==0]
print(num)