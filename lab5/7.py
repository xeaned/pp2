import re

text = 'snake_text'

def camel_case(match):
    return match.group(1).upper()

x = re.sub('_([a-z])', camel_case, text)

print(x)