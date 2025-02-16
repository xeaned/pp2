def gen(lim):
    cur=0
    while cur<=lim:
        yield cur
        cur+=1

n = int(input("Enter N: "))
seq=gen(n)
print(", ".join(str(x) for x in seq if x % 2 == 0))