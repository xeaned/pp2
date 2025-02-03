def spy_game(n):
    list = []
    for i in n:
        if i == 0 or i == 7:
            list.append(i)
    for i in range(len(list)-2):
        if list[i] == 0 and list[i + 1] == 0 and list[i + 2] == 7: 
            return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))