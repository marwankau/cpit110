m = eval(input("Enter an integer: "))

if m % 2 == 0 and m % 3 == 0:
    print(m, "is divisible by 2 and 3")
if m % 2 == 0 or m % 3 == 0:
    print(m, "is divisible by 2 or 3")
if (m % 2 == 0 or m % 3 == 0) and not (m % 2 == 0 and m % 3 == 0):
    print(m, "is divisible by 2 or 3 but not both")