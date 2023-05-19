def days_weeks ():
    days = years * 365
    weeks = years * 52
    return days, weeks 

def months_hours ():
    months = years * 12
    hours = years * 365 * 24
    return months, hours

years = int(input("Enter number of years"))
days_weeks = days_weeks()
months_hours = months_hours()
print(days_weeks)
print(months_hours)