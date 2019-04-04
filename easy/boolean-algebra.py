OP = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    
    if operation == OP[0]:
        return x and y
        
    if operation == OP[1]:
        return x or y
        
    if operation == OP[2]:
        return not x or y
        
    if operation == OP[3]:
        return (x and not y) or (not x and y)
        
    if operation == OP[4]:
        return x == y
        
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
