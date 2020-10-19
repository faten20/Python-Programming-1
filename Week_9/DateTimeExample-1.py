# Print the current year, month and day
from datetime import date
today = date.today() 
print(" day:", today.day)
print("month:", today.month)
print("year:", today.year)

#print current time
from datetime import datetime

now = datetime.now()

t = now.strftime("%H:%M:%S")
print("time:", t)


