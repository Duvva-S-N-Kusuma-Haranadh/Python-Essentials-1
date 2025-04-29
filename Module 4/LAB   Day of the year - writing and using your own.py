def is_year_leap(year):
    if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
        return True
    return

def days_in_month(year, month):
    if is_year_leap(year) and month == 2:
        return 29
    if month == 2:
        return 28
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30

def day_of_year(year, month, day):
    x = int(str(year - 1)[2:4])
    y = x // 4
    
    if year > 2000:
        z = 0
    elif year > 1900:
        z = 1
    elif year > 1800:
        z = 3
    elif year > 1700:
        z = 5
    
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    remaining_days = [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
    
    if is_year_leap(year):
        remaining_days[1] = 1
    
    sum_ = x + y + z + day
    
    for i in range(month - 1):
        sum_ += remaining_days[i]
    
    index = sum_ % 7
    
    return days[index]
    
print(day_of_year(2005, 6, 28))
