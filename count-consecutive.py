def count_consecutive_summers(num):
    low = 1
    high = int(((1+8*num)**(1/2)-1)/2) # could be simply '1', but this is a little optimization
    count = 0
    while low <= num and high <=num:
        sum = (low+high)/2*(high-low+1) # formula for sum of all numbers between 'low' and 'high''
        if sum == num:
            count += 1
            high += 1
        elif sum > num:
            low += 1
        else:
            high += 1
    return count

if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
