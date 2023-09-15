


import math
import time
run = True

while run == True:
    polygon = int(input("Hur många hörn?\n"))
    hörn = polygon
    bredd = int(input("Bredd?\n"))/2
    höjd = int(input("Höjd?\n"))/2
    x = 0
    y = 0
    ordning = 1
    while hörn > 0:
        print("Hörn ",ordning," (",x,(","),y,")",sep='')
        x = x - 2*bredd*math.cos(hörn*2*math.pi/polygon)
        y = y - 2*höjd*math.sin(hörn*2*math.pi/polygon)
        hörn = hörn - 1
        ordning = ordning + 1
    resp = input('Done? (y/n)\n')
    if resp == 'y':
        run = False
    else:
        print("\n")
