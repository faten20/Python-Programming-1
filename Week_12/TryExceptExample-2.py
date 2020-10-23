'''
value error handle using try and axcept 

'''

try:
    x = int(input("Enter the first number"))
    y = int(input("Enter the second number "))
    z = (x * y)
except :
    print (" value error you must enter an integer")
else:
    print ("multiply of two numbers = ", z)
  

