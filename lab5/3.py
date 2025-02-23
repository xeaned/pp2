import re

l = '/Users/rapiyatleukhan/Desktop/pp2/lab5/row.txt'
with open(l, 'r') as file:
    text = file.read()

pattern = r'\b[a-z]+_[a-z]+\b'
matches = re.findall(pattern, text)

if matches:
    print(f"Matches: {matches}")
else:
    print("No match found.")