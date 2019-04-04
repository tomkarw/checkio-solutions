def safe_pawns(pawns: set) -> int:
    
    count = 0
    for pawn1 in pawns:
        for pawn2 in pawns:
            if int(pawn2[1]) == int(pawn1[1]) - 1:
                if pawn2[0] == chr(ord(pawn1[0])+1) or pawn2[0] == chr(ord(pawn1[0])-1):
                    count += 1
                    break
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
