import re
text = "AStringToSplit"
result = re.sub(r'(?<!^)([A-Z])', r' \1', text)
print(result)