def prime(a):
    i = 3
    t = 3
    listname = []
    if a % 2 == 0:
        return False
    else:
        while t < a:
            if a % t != 0:
                i = i + 2
            else:
                listname.append(t)
            t = t + 2
        if i == t:
            return True
        else:
            return listname

test = int(input("Vilket tal?\n"))
isehg = prime(test)
if isehg == True:
    print("Primtal")
else:
    print("Ej Primtal, delbart med",isehg)