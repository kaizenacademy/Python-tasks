def calculate_tax(price):
	tax = price * 0.08
	return tax

def Sum(price, tax, discount):
	price = price + tax - discount
	return price

price = float(input("Please enter the price: "))

tax = calculate_tax(price)

print(Sum(price, tax, 10))