import json

a =  '{ "name":"ali", "age":30, "job":"accountant","salary":24000}'

# parse x:
b = json.loads(a)

# the result is a Python dictionary:
print(b)
print(b["job"])