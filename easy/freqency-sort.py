def frequency_sort(items):
    
    freq = {}
    
    for item in items:
        freq[item] = freq.get(item,0) + 1
    
    l = []
    
    for item in sorted(freq.items(), key = lambda kv: kv[1], reverse = True):
        l += [item[0]] * item[1]
        
    return l

def frequency_sort(items):
    return sorted(items, key=lambda x: (-items.count(x), items.index(x)))

if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
