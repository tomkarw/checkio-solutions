#The list of banned words are as follows:
#    sum
#    import
#    for
#    while
#    reduce

#Input: A list of numbers.

#Output: The sum of numbers. 

def checkio(data):
    if len(data) == 0:
        return 0
    
    return data[0] + checkio(data[1:])

def checkio(data):
    d = map(str, data)
    return eval('+'.join(d))



assert checkio([1,2,3]) == 6
