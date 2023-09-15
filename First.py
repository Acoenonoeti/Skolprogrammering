import time
times = int(input("How many numbers do you want?\n"))
loop = times - 2
print("\n")
x = 1
ny = 1
v = 1
print(x)
print(ny)
while loop > 0:
    v = ny
    ny = x + ny
    x = v
    print(ny)
    loop = loop - 1
    time.sleep(.1)

if loop == 0:
    print("The ",times,"th number is ",ny,sep='')


    

    
