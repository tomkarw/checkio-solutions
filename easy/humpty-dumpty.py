from math import pi, atanh, asin

# a - width/2
# c - height/2

def checkio(height, width):
    return [ 0.523 * width**2 * height, 2 * pi * width/2 * ( 1 + (1 - 

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"
