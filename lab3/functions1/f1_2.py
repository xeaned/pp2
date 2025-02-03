
def F_to_C(F):
    C =(5/9)*(F-32)
    return C

F=int(input())
C=F_to_C(F)
print(f"{F} degrees Fahrenheit = {C:.2f} degrees Celsius")
    
