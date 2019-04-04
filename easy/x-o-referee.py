from typing import List

def checkio(game_result: List[str]) -> str:
    
    for c in ['X','O']:
        for horizontal in game_result:
            if horizontal.count(c) == 3:
                return c
                
        for vertical in zip(*game_result):
            if vertical.count(c) == 3:
                return c
                
        if ''.join(game_result[i][i] for i in range(3)).count(c) == 3:
            return c
        
        if''.join(game_result[2-i][i] for i in range(3)).count(c) ==3:
            return c
        
    return "D"

def checkio(result):

    rows = result
    cols = map(''.join, zip(*rows))
    diags = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))
    lines = rows + list(cols) + list(diags)

    return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'



if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")



