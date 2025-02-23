import re

l = '/Users/rapiyatleukhan/Desktop/pp2/lab5/row.txt'

with open(l, 'r') as file:
    text = file.read()

x = re.search('ab*', text)

if x:
    print(f"Match : {x.group()}")
else:
    print("No match found.")