def time_converter(time):
    time = time.replace(':',' ',1).split()
    hour = int(time[0])
    minutes = int(time[1])
    if(time[2] == 'a.m.'):
        if(hour == 12):
            return f"00:{minutes:02d}"
        else:
            return f"{hour:02d}:{minutes:02d}"
    else:
        if (hour == 12):
            return f"12:{minutes:02d}"
        else:
            return f"{hour+12:02d}:{minutes:02d}"

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")
