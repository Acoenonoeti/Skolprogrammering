i = int(138/2)-1
e = 0
while i > 0:
    print(i*" ","/",e*" ","\ ",sep="")
    e += 2
    i -= 1
print("/",136*" ","\ ",sep="",end="")
while e > 0:
    print(i*" ","\ ",(e-2)*" ","/",sep="")
    i += 1
    e -= 2