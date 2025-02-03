def is_prime(num):
    cnt=0
    if num<2: 
        return False
    for i in range(2, num):
        if num%i==0:
            return False
    return True

def filter_prime(numbers):
    list = []
    for i in numbers: 
        if is_prime(i):
            list.append(i)
    return list

n = int(input("n= "))
list = []
for j in range(n):
    num = int(input())
    list.append(num)
print(filter_prime(list))
