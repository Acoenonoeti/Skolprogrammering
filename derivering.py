def funktion(x):
    return x**3 + 2*x + 5
def deriv(value, dec):
    h = 1e-9
    h = (funktion(value+h) - funktion(value))/h
    h = round(h,dec)
    return h
e = int(input("Vilket värde?\n"))
b = int(input("Hur noga?\n"))
print("f(",e,") ", "är ungefär ",deriv(e,b),sep="")