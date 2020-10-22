'''

 search for string and returns found if the search is successful 
 and string not found if search unuccessful

'''

import re

str1 = "I live in London"


found = re.search('live', str1)

if found:
  print("string found")
else:
  print("string not found")
