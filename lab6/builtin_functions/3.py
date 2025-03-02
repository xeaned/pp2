string = input()
new= string.lower()
if new == ''.join(reversed(new)):
    print("palindrome")
else:
    print("not a palindrome")
