def is_leap(year):
    leap = False
    
    # Write your logic here
    cond = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    if cond: 
        leap = True
    return leap