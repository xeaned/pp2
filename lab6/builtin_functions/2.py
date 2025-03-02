my_string=str(input())
u=0
l=0
for i in my_string:
    if i.isupper():
        u+=1
    if i.islower():
        l+=1
print('lower case:', l)
print('upper case', u)