import math
amount = eval(input("Enter an amount in double, e.g. 11.56: "))

dollars = math.floor(amount)

cents = round((amount - dollars) * 100)

QUARTER = 25
DIME = 10
NICKEL = 5

quarters = cents // QUARTER
cents = cents - quarters * QUARTER

dimes = cents // DIME
cents = cents - dimes * DIME

nickels = cents // NICKEL
cents = cents - nickels * NICKEL

print("\t", dollars, "dollars")
print("\t", quarters, "quarters")
print("\t", dimes, "dimes")
print("\t", nickels, "nickels")
print("\t", cents, "pennies")
