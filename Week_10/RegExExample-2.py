'''

Replace every digit character with the number 0

'''

import re

txt = "my address is NW44UJ"
x = re.sub("\d", "0", txt)
print(x)
