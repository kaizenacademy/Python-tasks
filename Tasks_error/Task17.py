def days():
    day=years*365 
    return days

years=(input("Enter number of years: "))
unit=(input("Pick your choice: 
1 - Days
2 - Weeks
Input: "))

if unit == 1:
    w=day()
    print(w)
