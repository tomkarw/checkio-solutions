def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    
    max = 0
    i = 0
    while i < len(line):
        j = 0
        while j < len(line)-i:
            if line[i] != line[i+j]:
                i = i+j -1
                break
            else:
                j += 1
                if j > max:
                    max = j
                
        i += 1
    
    return max

from itertools import groupby

def long_repeat(line):

    return max((sum(1 for _ in g) for k, g in groupby(line)), default=0)

   

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
