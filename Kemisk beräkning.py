modes = ["0) Av\n","1) Jämvikt\n"]
print(modes[0],modes[1],sep='')
mode = int(input())
while mode == 1:
    Reaktanter = int(input("Hur många reaktanter?\n"))
    r = 0
    i = 1
    k = 1
    m = 1
    sr = 1
    while Reaktanter > 0:
        print("\nKoncentration reaktant",i)
        k = float(input())
        print("\nMolf. reaktant",i)
        m = int(input())
        r = r + m
        sr = sr*(k**m)
        i = i + 1
        Reaktanter = Reaktanter - 1
    Produkter = int(input("\nHur många produkter?\n"))
    p = 0
    sp = 1
    i = 1
    while Produkter > 0:
        print("\nKoncentration produkt",i)
        k = float(input())
        print("\nMolf. produkt",i)
        m = float(input())
        p = p + m
        sp = sp*(k**m)
        i = i + 1
        Produkter = Produkter - 1
    volym = float(input("Volym?\n"))
    print("\nQ =",(sp/sr)*(volym**(r-p)))
    print("\n",modes[0],modes[1],sep='')
    mode = int(input("Läge?\n"))