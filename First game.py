import math
run = 1
class Struktur:
    def __init__(self,X,Y,Scale,Name):
        self.X = X
        self.Y = Y
        self.Scale = Scale
        self.Namn = Name
def hitcheck(x,y):
    i = False
    for strukt in struktur:
         if math.isclose(strukt.X, x, abs_tol=strukt.Scale) and math.isclose(strukt.Y, y, abs_tol=strukt.Scale):
            i = True
            return strukt.Namn
    if i == False:
        return True
struktur = []
x = 0
y = 0
while run != 0:
    run = input("Vandra runt (1), Sätta ut strukturer (2), Ta bort strukturer (3), Inspektera Strukturer (4) Avsluta (0)\n")
    while run.isnumeric == False:
        run = input("Vandra runt (1), Sätta ut strukturer (2), Ta bort strukturer (3), Inspektera Strukturer (4) Avsluta (0)\n")
    if run.isnumeric:
        run = int(float(run)//1)
    if run == 2:
        struktur.append(Struktur(int(input("X-koordinat: ")),int(input("Y-koordinat: ")),float(input("Skala: "))-1,input("Namn: ")))
    if run == 4:
        a = 0
        for strukt in struktur:
            a += 1
            print(strukt.Namn," (",a,")",sep='', end=" ")
        check = int(input("\nVilken struktur vill du titta på?: "))-1
        print("X: ",struktur[check].X,"\nY: ", struktur[check].Y, "\nSkala: ", struktur[check].Scale,sep='',end="\n")
    if run == 1:
        print("WASD kontroller, avsluta med annat än WASD\n")
        while run == 1:
            a = input()
            hit = False
            if a == "w":
                if hitcheck(x,y+1) == True:
                    y +=1
                else:
                    print("Ow,",hitcheck(x,y+1))
            elif a == "W":
                if hitcheck(x,y+1) == True:
                    y +=1
                    if hitcheck(x,y+1) == True:
                        y +=1
                    else:
                        print("Ow,",hitcheck(x,y+1))
                else:
                    print("Ow,",hitcheck(x,y+1))
            elif a == "s":
                if hitcheck(x,y-1) == True:
                    y -=1
                else:
                    print("Ow,",hitcheck(x,y-1))
            elif a == "S":
                if hitcheck(x,y-1) == True:
                    y -=1
                    if hitcheck(x,y-1) == True:
                        y -=1
                    else:
                        print("Ow,",hitcheck(x,y-1))
                else:
                    print("Ow,",hitcheck(x,y-1))
            elif a == "a":
                if hitcheck(x-1,y) == True:
                    x -=1
                else:
                    print("Ow,",hitcheck(x-1,y))
            elif a == "A":
                if hitcheck(x-1,y) == True:
                    x -=1
                    if hitcheck(x-1,y) == True:
                        x -=1
                    else:
                        print("Ow,",hitcheck(x-1,y))
                else:
                    print("Ow,",hitcheck(x-1,y))
            elif a == "d":
                if hitcheck(x+1,y) == True:
                    x +=1
                else:
                    print("Ow,",hitcheck(x+1,y))
            elif a == "D":
                if hitcheck(x+1,y) == True:
                    x +=1
                    if hitcheck(x+1,y) == True:
                        x +=1
                    else:
                        print("Ow,",hitcheck(x+1,y))
                else:
                    print("Ow,",hitcheck(x+1,y))
            elif a.lower() == "space":
                print("Good job, du hoppa :)\nEaster egg found!")
            else:
                break
            
            print("\n",x,y,"\n")
    if run == 3:
        a = 0
        for strukt in struktur:
            a += 1
            print(strukt.Namn," (",a,")",sep='', end=" ")
        check = int(input("\nVilken struktur vill du ta bort? "))-1
        while (check > a) or (check < 0):
                check = int(input("\nVilken struktur vill du ta bort?\n"))-1
        print("Tog bort",struktur[check].Namn,"\n")
        struktur.__delitem__(check)