def gen(lim):
    cur = 0
    while cur <= lim:
        if cur % 3 == 0 and cur % 4 == 0:
            yield cur
        cur += 1
n = int(input("N: "))
nums = gen(n)
for num in nums:
    print(num)
