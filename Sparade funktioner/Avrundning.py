def rounding(a,b):
    t = 10**b
    a = a*t
    if a - a//1 >= 0.5:
        return (a//1)/t + 1/t
    else:
        return (a//1)/t
tal = input("Tal: ")
if tal.__contains__("/") == True:
    tal = tal.split("/")
    tal = int(tal[0])/int(tal[1])
elif tal.__contains__("*") == True:
    tal = tal.split("*")
    tal = int(tal[0])*int(tal[1])
else:
    tal = int(tal)
tal2 = int(input("Decimaler: "))
print(rounding(tal,tal2), round(tal, tal2))
