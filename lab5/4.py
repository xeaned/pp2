import re
l = '/Users/rapiyatleukhan/Desktop/pp2/lab5/row.txt'

with open(l, 'r') as file:
    text = file.read()

pattern = r'[A-Z][a-z]+'
matches = re.findall(pattern, text)

if matches:
    print(f"Matches: {matches}")
else:
    print("No match found.")