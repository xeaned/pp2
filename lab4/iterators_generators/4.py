def squares(a, b):
    while a <= b:
        yield a**2
        a += 1

a = int(input("start (a): "))
b = int(input("end (b): "))

for square in squares(a, b):
    print(square)