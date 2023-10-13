import time
import math
import sys
sys.set_int_max_str_digits(10000)
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
print("number 1:",x)
print("number 2:",ny)
while loop > 0:
    v = ny
    ny = x + ny
    x = v
    i = i + 1
    print("number ",i,": ",ny,"\n",sep='')
    loop = loop - 1
    time.sleep(wait)

if loop == 0:
    print("The ",times,"th number in the fibonacci sequence is ",ny,sep='')