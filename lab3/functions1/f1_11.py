def palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False
    
str = input('string: ')
print(palindrome(str))