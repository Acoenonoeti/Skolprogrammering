prime = 5
nämnare = 3
i = 1
run = True
typ = input("Specifik? (y/n)\n")
if typ == "y":
    run = False
import time
if run == True:
    sleep = float(input("Tid?\n"))
    limit = int(input("Gräns?\n"))
    while run == True:
        while nämnare < prime:
            if prime % nämnare != 0:
                i = i + 2
            nämnare = nämnare + 2
            if i == prime - 2:
                print(prime)
                time.sleep(sleep)
        if prime > limit:
            run = False
        prime = prime + 2
        nämnare = 3
        i = 1
if run == False and typ == "y":
    prime = int(input("Vilket tal?\n"))
    print("\n")
    if prime % 2 == 0:
        print("Ej primtal, jämnt\n")
        run = True
    nämnare = 3
    i = 1
    while run == False:
        while nämnare < prime:
            if prime % nämnare == 0:
                print("Delbart med",nämnare,"\n")
                run = True
                nämnare = nämnare + 2
            else:
                i = i + 2
                nämnare = nämnare + 2
        if i == prime - 2:
            print("Primtal\n")
            run = True
        else:
            print("Ej Primtal\n")
            run = True
            