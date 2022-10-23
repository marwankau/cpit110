weight1, price1 = eval(input("Enter weight and price for package 1: "))
weight2, price2 = eval(input("Enter weight and price for package 2: "))

kilo_price1 = price1 / weight1
kilo_price2 = price2 / weight2

if kilo_price1 < kilo_price2:
    print("Package 1 has better price")
elif kilo_price1 > kilo_price2:
    print("Package 2 has better price")
else:
    print("Both have same price!")




