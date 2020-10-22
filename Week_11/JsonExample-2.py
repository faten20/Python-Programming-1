import json
x = '{"car":"IBM", "year":2019,"country":"USA"}'
#parse a JSON string using json.loads()
dict1 = json.loads(x)

print(dict1)
print(type(x))
