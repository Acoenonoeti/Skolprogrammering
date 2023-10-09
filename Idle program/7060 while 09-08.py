import time
import random
done = False
while done == False:
    word = []
    alternativ = int(input("Hur många alternativ?\n"))
    loops = alternativ
    ordning = 1
    while loops > 0:
        print("Alternativ ",ordning,"?",sep='')
        d = input()
        print("\n")
        ordning = ordning + 1
        word.append(d)
        loops = loops - 1
    respons = input("Gissa!\n")
    svar = word[random.randrange(int(alternativ))]
    if respons == svar:
        print("Bra jobbat!\n")
    else:
        print("Tyvärr, rätt svar var...")
        time.sleep(3)
        print(svar,"\n")
    igen = input("Kör igen (y/n)?\n")
    if igen == "n":
        done = True
    elif igen == "y":
        print("\n\n")
    