FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"] 
HUNDRED = "hundred"


def checkio(number):
    
    w = ''
    
    d = list(map(int,str(number).zfill(3)))
    
    if d[0] > 0:
        w += FIRST_TEN[d[0]-1] + ' ' + HUNDRED + ' '
    if d[1] == 1:
        return w + SECOND_TEN[d[1]*10+d[2]-10]
    if d[1] > 1:
        w += OTHER_TENS[d[1]-2] + ' '
    if d[2] > 0:
        w +=  FIRST_TEN[d[2]-1] + ' '
        
    return w[:-1]
        
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(checkio(4))
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
