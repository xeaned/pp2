def unique(list):
    list_unique = []
    for i in list:
        if i not in list_unique:
            list_unique.append(i)
    return list_unique

list = []

n = int(input("n: "))
for i in range(n):
    num = int(input())
    list.append(num)
print(unique(list))