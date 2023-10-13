def nfloat(a):
    if a[0] == "-":
        a = a.split(".")
        b = int(a[0])
        i = 0
        for d in a[1]:
            i += 1
        c = int(a[1])*10**-i
        return b-c
    else:
        return float(a)

e = nfloat(input())
if (e < 0) and ((e + e//1)*-1 > 0):
    print("Negative float:", e)
else:
    print("Float:",e)