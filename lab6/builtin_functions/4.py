import time
import math
num = int(input())
t = int(input())
msec=t/1000
time.sleep(msec)
print(f"Square root of {num} after {t} miliseconds is {math.sqrt(num)}")