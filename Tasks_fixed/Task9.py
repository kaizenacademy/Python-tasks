tip = 0
while tip != 14.99 and tip !=19.99:
    tip = float(input("Please enter tip amount: "))


if tip == 14.99:
    print("Standard")

elif tip == 19.99:
    print("Good")