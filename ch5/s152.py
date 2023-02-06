num1 = eval(input("Enter first integer: "))
num2 = eval(input("Enter second integer: "))

if num1 == 0 or num2 == 0:
    print("Numbers must be more than 0")
else:
    n1, n2 = num1, num2

    if num1 < num2:
        n1, n2 = num2, num1

    gcd = n2
    tmp = n1 % n2
    print(n1, n2, tmp)
    while tmp != 0:
        gcd = tmp
        n1 = n2
        n2 = tmp
        tmp = n1 % n2
        print(n1, n2, tmp)

    print("GCD is", gcd)
