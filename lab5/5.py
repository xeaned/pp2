import re

l = '/Users/rapiyatleukhan/Desktop/pp2/lab5/row.txt'

with open(l, 'r') as file:
    text = file.read()

pattern = r'a.*b'

match = re.search(pattern, text)

if match:
    print(f"Match: {match.group()}")  
else:
    print("No match found.")