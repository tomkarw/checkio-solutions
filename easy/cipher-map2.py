def read(cg, cp):
    
    pw = ''
    
    for rowGrill, rowPass in zip(cg, cp):
        for cellGrill, cellPass in zip(rowGrill, rowPass):
            if cellGrill == 'X':
                pw += cellPass

    return pw

def flip(cg):
    return list(map(''.join,(map(reversed,map(''.join, zip(*cg))))))

def recall_password(cg, cp):
    
    pw = ''
    
    for _ in range(4):
        pw += read(cg, cp)
        cg = flip(cg)
        
    return pw

def recall_password(grill, cypher):

    password = ""

    for _ in grill:  # must be of len 4

        for grill_row, cypher_row in zip(grill, cypher):

            for grill_letter, cypher_letter in zip(grill_row, cypher_row):

                if grill_letter == 'X':

                    password += cypher_letter

        row1, row2, row3, row4 = grill

        grill = tuple(zip(row4, row3, row2, row1))  # rotate

    return password

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
