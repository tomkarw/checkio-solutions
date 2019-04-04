months = { 
    1 : 'January',
    2 : 'February',
    3 : 'March',
    4 : 'April',
    5 : 'May',
    6 : 'June',
    7 : 'July',
    8 : 'August',
    9 : 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

def date_time(time: str) -> str:
    date, time = time.split()
    day, month, year = map(int,date.split('.'))
    hour, minute = map(int,time.split(':'))
    
    hWord = 'hour' if hour == 1 else 'hours'
    mWord = 'minute' if minute == 1 else 'minutes'
    return f"{day} {months[month]} {year} year {hour} {hWord} {minute} {mWord}"

if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 01:01'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 01:01") == "1 January 2000 year 1 hour 1 minute", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
