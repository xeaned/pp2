#Search the string to see if it starts with "The" and ends with "Spain":

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)



import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)



text = "Сегодня Мы Учим Regex В Python"
pattern = r'\b[A-ZА-Я][a-zа-я]*'
result = re.findall(pattern, text)
print(result)  # ['Сегодня', 'Мы', 'Учим', 'Regex', 'В', 'Python']

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

parts = re.split(r'\d+', 'abc123def456')
print(parts)  # Вывод: ['abc', 'def', '']

result = re.sub(r'\d+', 'X', 'abc123def456')
print(result)  # Вывод: abcXdefX

matches = re.findall(r'\d+', 'abc123def456')
print(matches)  # Вывод: ['123', '456']

result = re.search(r'\d+', 'abc123def112')
if result:
    print('Совпадение:', result.group())  # Вывод: 123
'''
Function	Description
findall	    Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
split	    Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string
'''


'''
Character	Description	                                Example	
[]	        A set of characters	                        "[a-m]"	
\	        Signals a special sequence              	"\d"	
.	        Any character (except newline character)	"he..o"	
^	        Starts with	                                "^hello"	
$	        Ends with	                                "planet$"	
*	        Zero or more occurrences	                "he.*o"	
+	        One or more occurrences	                    "he.+o"	
?	        Zero or one occurrences	                    "he.?o"	
{}	        Exactly the specified num of occurrences	"he.{2}o"	
|	        Either or	                                "falls|stays"
'''


'''
Set         Description	
[arn]	    Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	    Returns a match for any lower case character, alphabetically between a and n	
[^arn]	    Returns a match for any character EXCEPT a, r, and n	
[0123]	    Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	    Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	        In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string'''