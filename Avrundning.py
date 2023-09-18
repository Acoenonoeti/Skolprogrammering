def round(a,b):
    if a % b >= 0.5:
        return (a//b)+1
    else:
        return a//b

tal = float(input("Täljare: "))
tal2 = float(input("Nämnare: "))
print(int(round(tal,tal2)), " (",tal/tal2,")",sep='')