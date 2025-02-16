def gen(start):
    while start>=0:
        yield start
        start-=1
start=int(input("number N: "))
nums=gen(start)
for num in nums:
    print(num)