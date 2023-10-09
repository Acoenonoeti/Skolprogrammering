def logic(gate,a,b):
    if gate == "or":
        if a == True:
            return True
        elif b == True:
            return True
        else:
            return False
    elif gate == "xor":
        if a == True:
            if b == False:
                return True
            else:
                return False
        elif b == True:
            if a == False:
                return True
            else:
                return False
        else:
            return False
    elif gate == "and":
        if a == True:
            if b == True:
                return True
            else:
                return False
        else:
            return False
    elif gate == "nand":
        if a == True:
            if b == True:
                return False
            else:
                return True
        else:
            return True
    elif gate == "nor":
        if a == True:
            return False
        elif b == True:
            return False
        else:
            return True