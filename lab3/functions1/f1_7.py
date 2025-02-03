def has_33(n):
    for i in range(len(n)-1):
        if n[i] == n[i+1] and n[i]==3:
            return True
    return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))