done = "n"
lista = []
while done == "n":
    a = input()
    if a.isnumeric == False:
        while a.isnumeric == False:
            a = input()
            if a.isnumeric:
                a = float(a)
                lista.append(a)
    else:
        a = float(a)
        lista.append(a)
    done = input("\nKlar? (y/n)\n")
print("\n")
print(lista)
e = input("Metod?\n")
if e == "*":
    b = 1
    for i in lista:
        b = i*b
    print(b)
elif e == "+":
    b = 0
    for i in lista:
        b = i+b
    print(b)
elif e == "-":
    b = 0
    for i in lista:
        b = i-b
    print(b)
elif e == "/":
    b = 1
    for i in lista:
        b = i/b
    print(b)
elif e == "**":
    b = 1
    for i in lista:
        b = i**b
    print(b)
elif e == "//":
    b = 1
    for i in lista:
        b = i/b
    print(b)
elif e == "rot":
    b = 1
    for i in lista:
        b = b*(i**(1/2))
    print(b)