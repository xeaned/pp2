import math

def grams_to_ounces(grams):
    ounces = grams/28.3495231
    return ounces

def F_to_C(F):
    C =(5/9)*(F-32)
    return C



def solve(heads, legs):
    r = int((legs-(2*heads))/2)
    ch = int(heads-r)

    print("Rabbits:", r)
    print("Chickens:", ch)



def permute(s, l=''):
    if len(s) == 0:
        print(l)
    else:
        for i in range(len(s)):
            remaining = s[:i] + s[i+1:]
            permute(remaining, l + s[i])



def has_33(n):
    for i in range(len(n)-1):
        if n[i] == n[i+1] and n[i]==3:
            return True
    return False



def spy_game(n):
    list = []
    for i in n:
        if i == 0 or i == 7:
            list.append(i)
    for i in range(len(list)-2):
        if list[i] == 0 and list[i + 1] == 0 and list[i + 2] == 7: 
            return True
    return False



def v(r):
    return (4/3) * math.pi * pow(r, 3)

r = int(input('r: '))
print(v(r))



def palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False
    


def histogram(list):
    for num in list:
        print('*' * num)


print(grams_to_ounces(1000)) 
print(F_to_C(444))  
solve(35, 94)  
permute("rappi") 
print(has_33([1, 3, 3]))  
print(spy_game([1, 2, 4, 0, 0, 7, 5])) 
print(v(5))
print(palindrome("kayak"))  
histogram([5, 4, 4])  
