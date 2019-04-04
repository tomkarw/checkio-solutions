def total_cost(calls):
    days = {}
    for call in calls:
        date, _, duration = call.split()
        days[date] = days.get(date,0) + int((int(duration) + 59)/60)
    
    bill = 0
    
    for duration in days.values():
        tarif = 1
        if duration > 99:
            duration -= 100
            bill += 100
            tarif = 2
            print(100)
        print(duration * tarif)
        bill += duration * tarif
        
    return bill

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")))
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"
