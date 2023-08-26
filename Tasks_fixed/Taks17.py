def days():
    day=years*365 
    return day

years=int(input("Enter number of years: "))
unit=int(input("""Pick your choice: 
1 - Days
2 - Weeks
Input: """))

if unit == 1:
    w=days()
    print(w)
