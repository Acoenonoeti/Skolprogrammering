import math
import time
run = True

while run == True:
    polygon = input("Hur många hörn?\n")
    if polygon == "infinity":
        polygon = math.inf
    else:
       polygon = int(polygon)
    if polygon <= 0:
        print("Jävla unge")
        run = False
    if run == True:
        fråga = True
        specifik = 0
        while fråga == True:
            specifik = input("Specifikt hörn eller alla hörn?\n")
            if specifik == "Alla":
                hörn = 0
                fråga = False
            if specifik == "Specifikt":
                hörn = polygon - int(input("\nVilket?\nHörn nr: "))
                fråga = False
        bredd = float(input("Bredd?\n"))/2
        höjd = float(input("Höjd?\n"))/2
        x = 0
        y = 0
        ordning = 1
        while hörn < polygon:
            if specifik == "Specifikt":
                if hörn == polygon - 1:
                    print("Hörn ",ordning," (",x,",",y,")",sep='')
            elif specifik == "Alla":
                print("Hörnt ",ordning," (",x,",",y,")",sep='')            
            x = x - 2*bredd*math.cos(hörn*math.tau/polygon)
            y = y - 2*höjd*math.sin(hörn*math.tau/polygon)
            hörn = hörn + 1
            if polygon == math.inf:
                run = False
            ordning = ordning + 1
        resp = input('Done? (y/n)\n')
        if resp == 'y':
            run = False
    print("\n")