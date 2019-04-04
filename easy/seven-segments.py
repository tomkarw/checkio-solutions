import string

numbers = { 0 : ('a','b','c','d','e','f'),
            1 : ('b','c'),
            2 : ('a','b','d','e','g'),
            3 : ('a','b','c','d','g'),
            4 : ('b','c','f','g'),
            5 : ('a','c','d','f','g'),
            6 : ('a','c','d','e','f','g'),
            7 : ('a','b','c'),
            8 : ('a','b','c','d','e','f','g'),
            9 : ('a','b','c','d','f','g')
}

def possible_numbers(lit_seq,broken_seq):
    
    count = 0
    
    for k, number_set in numbers.items():
        if lit_seq.issubset(set(number_set)):
            if set(number_set).issubset(set(lit_seq | broken_seq)):
                count += 1
    return count

def seven_segment(lit_seg, broken_seg):
    
    lit_seg_upper = set(map(str.lower,filter(lambda c: c in string.ascii_uppercase,lit_seg)))
    lit_seg_lower = set(filter(lambda c: c in string.ascii_lowercase,lit_seg))
    
    broken_seg_upper = set(map(str.lower,filter(lambda c: c in string.ascii_uppercase,broken_seg)))
    broken_seg_lower = set(filter(lambda c: c in string.ascii_lowercase,broken_seg))
    
    possible_upper = possible_numbers(lit_seg_upper,broken_seg_upper)
    possible_lower = possible_numbers(lit_seg_lower,broken_seg_lower)
    
    return possible_upper * possible_lower



segments = list(map(set, [
    'bc',
    'abged',
    'abgcd',
    'fbgc',
    'afgcd',
    'afgcde',
    'abc',
    'abcdefg',
    'abcdfg',
    'abcdef'
]))

def seven_segment(*args):

    def digit(f):
        lit, broken = ({s.lower() for s in segs if f(s)} for segs in args)
        return sum(lit <= s <= (broken | lit) for s in segments)
        
    return digit(str.islower) * digit(str.isupper)



if __name__ == '__main__':
    assert seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2, '11, 71'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}) == 6, '15, 16, 35, 36, 75, 76'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}) == 20, '15...98'
    print('"Run" is good. How is "Check"?')
