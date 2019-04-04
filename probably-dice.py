
def probability(dice_number, sides, target):
    
    # dictionary for storing values already calculated
    memo = {}
    
    def favourable(dice_number, sides, target):
        
        # if we already know how many options there are for some number of dices and some target value, we simply use it
        if (dice_number, target) in memo:
            return memo[(dice_number, target)]
        
        # this means that we succesfully reached the target sum
        if target == 0 and dice_number == 0:
            return 1
        
        # this means we failed to reach the target
        if dice_number == 0 or target < 0:
            return 0
        
        # there could be few more optimalizations, but I think they might only harm perforamance
        # we will never reach the target
        if target > dice_number * sides:
            return 0
        
        # we will surely surpass target
        if target < dice_number:
            return 0
        
        s = 0
        
        # for every possible roll of dice
        for k in range(sides):
            # recursive call with less dices and lower target
            fav = favourable(dice_number-1, sides, target-k-1)
            # let's store the new value in our dict
            memo[(dice_number-1, target-k-1)] = fav
            # and add current roll to the sum
            s += fav
            
        return s
    
    # new we simply call our recursive function and divide it by all posible rolls
    return favourable(dice_number, sides, target)/(sides**dice_number)
   
if __name__ == '__main__':
    #These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision
    
    assert(almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert(almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert(almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert(almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert(almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert(almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    print(probability(10, 10, 50), 0.0375)
    assert(almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
