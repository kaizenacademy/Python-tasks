def days_weeks ():
    days = years * 365
    return weeks 

def months_hours ():
    months = years * 12
    return days

years = int(input("Enter number of years"))
days_weeks = days_weeks
months_hours = months_hours
print(days_weeks)
print(months_hours)

# It should print days and weeks fot the 1st function, eg (365, 52)
# It should print months and hourss fot the 2nd function, eg (12, 8760)
