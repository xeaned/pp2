import math
n = float(input("Input number of sides: "))
a = float( input("Input the length of a side: "))
degree = (math.pi*(n-2))/(2*n)
area = math.tan(degree)* (a*a/4)
print(round(area*n))