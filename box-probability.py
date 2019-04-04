def checkio(marbles: str, step: int) -> float:
    """ Input: The start sequence of the pearls as a string and the move number as an integer.
        Output: The probability for a white pearl as a float. """
        
    def branch(white, step):
        """ Recursively branch into both (if possible) cases"""
        if step == 1:
            return white/all
        
        left = 0 if white == all else branch(white+1,step-1)
        right = 0 if white == 0 else branch(white-1,step-1)
        
        return (all-white)/all * left + white/all * right
    
    white = marbles.count('w')
    all = len(marbles)
    
    return round(branch(white,step),2)
    
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio('bbw', 3))

    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"
    print("Coding complete? Click 'Check' to earn cool rewards!")
