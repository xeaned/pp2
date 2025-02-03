def solve(heads, legs):
    r = int((legs-(2*heads))/2)
    ch = int(heads-r)

    print("Rabbits:", r)
    print("Chickens:", ch)

heads=int(input("heads: "))
legs=int(input("legs: "))
solve(heads, legs)