amount = eval(input("Enter purchase amount: "))
tax = amount * 0.06

tax = round(tax * 100) / 100

print("Sales tax is", tax)
