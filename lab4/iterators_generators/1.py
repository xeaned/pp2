def gen_seq(lim):
    cur=1
    while cur<=lim:
        yield cur
        cur+=1

n = int(input("Enter a number: "))
seq=gen_seq(n)
for x in seq:
    print(x)