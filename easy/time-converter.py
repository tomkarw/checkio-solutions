def time_converter(time):
    
    hour, minutes = map(int,time.split(':'))
    
    return ((str(hour-12) + ":" + str(minutes).zfill(2) if hour >=13 else str(hour) + ":" + str(minutes).zfill(2)) \
                + (" p.m." if hour >= 12 else " a.m.")) if (hour or minutes) else "12:00 a.m."

def time_converter(time):

    h, m = map(int, time.split(':'))

    return f"{(h-1)%12+1}:{m:02d} {'ap'[h>11]}.m."



if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    print(time_converter('09:00'))
    assert time_converter('09:00') == '9:00 a.m.'
    print(time_converter('23:15'))
    assert time_converter('23:15') == '11:15 p.m.'
    print(time_converter('00:00'))
    print("Coding complete? Click 'Check' to earn cool rewards!")
