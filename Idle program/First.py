import time
import math
times = input("How many numbers do you want?\n")
if times == "oändligt":
    times = math.inf
else:
    times = int(times)
loop = times - 2
print("\n")
wait = float(input("Sleep time?\n"))
x = 1
ny = 1
v = 1
i = 2
print("\n")
print(x)
print(ny)
while loop > 0:
    v = ny
    ny = x + ny
    x = v
    i = i + 1
    print(ny)
    loop = loop - 1
    time.sleep(wait)
    if ny >= 10**4299:
        loop = 0
        times = i

if loop == 0:
    print("The ",times,"th number is ",ny,sep='')