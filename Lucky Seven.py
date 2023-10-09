import random
run = input("Vill du köra? (y/n)\n")
while run == "y":
    slot = [random.randrange(10),random.randrange(10),random.randrange(10)]
    print(slot)
    if slot[0] == slot[1] == slot[2]:
        if slot[0] == 7:
            print("Jackpot!\n")
        else:
            print("Vinst\n")
    else:
        print("Förlust\n")
    run = input("Kör igen? (y/n)\n")
    while not(run == "n" or run == "y"):
        run = input("Förstår inte. (y/n)\n")