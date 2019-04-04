def group_equal(els):
    
    if not els:
        return []
        
    ll = [[els[0]]]

    for i in range(1,len(els)):
        
        # element is equal to the element in the previous list, append it to that list
        if els[i] == ll[-1][0]:
            ll[-1] += [els[i]]
        
        # else create a new list element
        else:
            ll += [[els[i]]]

    return ll

def group_equal(els):
    

if __name__ == '__main__':
    print("Example:")
    print(group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]) == [[1,1],[4,4,4],["hello","hello"],[4]]
    assert group_equal([1, 2, 3, 4]) == [[1], [2], [3], [4]]
    assert group_equal([1]) == [[1]]
    assert group_equal([]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
