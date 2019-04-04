def flat_list(array):
    
    tmp = []
    
    if not isinstance(array,list):
        return [array]
    else:
        for el in array:
            tmp += flat_list(el)
    
    return tmp



flat_list=f=lambda d:[d]if int==type(d)else sum(map(f,d),[])


    
if __name__ == '__main__':
    print(flat_list([1, 2, 3]))
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    print(flat_list([1, [2, 2, 2], 4]))
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
