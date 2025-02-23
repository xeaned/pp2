import re

text = "Today is Sunday"
result = re.sub(r'[ ,.]', ':', text)
print(result)