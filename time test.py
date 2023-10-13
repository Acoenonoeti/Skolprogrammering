import time
import random
a = True
d = 0
e = 0
f = 0
g = 0
h = 30
while a:
    while h > 0:
        c = []
        b = random.randrange(1000)
        if b != 0:
            b = random.randrange(b)
        while b > 0:
            c.append("x")
            b = random.randrange(1000)
            if b != 0:
                b = random.randrange(b)
        c.append("y")
        b = random.randrange(100000)
        if b != 0:
            b = random.randrange(b)
        while b > 0:
            c.append("x")
            b = random.randrange(100000)
            if b != 0:
                b = random.randrange(b)

        b = time.time_ns()
        if c.__contains__("y"):
            d = b - time.time_ns() + d
            e = e + 1
        b = time.time_ns()
        for t in c:
            if t == "y":
                f = b - time.time_ns() + f
                g = g + 1
                break
        h -= 1
    print("Contain:",d/e,"\nFor:",f/g)
    a = input("Loop? ").lower
    if a != "no":
        a = True
        h = 30
    else:
        break