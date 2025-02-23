import re

l = '/Users/rapiyatleukhan/Desktop/pp2/lab5/row.txt'

with open(l, 'r') as file:
    text = file.read()

x = re.findall('[a-z]+_', text)

if x:
    print(f"Match : {x}")
else:
    print("No match found.")