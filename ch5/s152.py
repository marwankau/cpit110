num1 = eval(input("Enter first integer: "))
num2 = eval(input("Enter second integer: "))
a = num1
b = num2
if b > a:
    a, b = b, a

r = -1

while r != 0:
    q = a // b
    r = a % b

    a = b
    b = r

print("The greatest common divisor for", num1, "and", num2, " is", a)
