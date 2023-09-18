import random
import time
def tärningskast(sidor,tärningar):
    tärning = []
    while tärningar > 0:
        tärning.append(random.randrange(sidor)+1)
        tärningar = tärningar - 1
    return tärning
play = "y"
while play == "y":
    f = int(input("Hur många tärningar?\n"))
    print("\n")
    r = int(input("Hur många sidor?\n"))
    listan = tärningskast(r,f)
    Odds = (r**(-f+1))*100
    print("\n","Odds för vinst: ",Odds,"%\n",sep="")
    time.sleep(2)
    print(listan)
    listnummer = 0
    i = 0
    while f - 1 > 0:
        if listan[listnummer] == listan[listnummer + 1]:
            i = i + 1
        listnummer = listnummer + 1
        f = f - 1
    if listnummer == i:
        print("\n","Vinst\n",sep="")
    else:
        print("\n","Förlust\n",sep="")
    play = input("Kör igen? (y/n)\n")
    print("\n")