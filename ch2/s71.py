'''
Write program that proumt user to enter two numbers and display
thous numbers in both ways : for example: x: 8, y: 2
Output: should be as following:
82
28
'''

x = eval(input("enter first number which less than 10: "))
y = eval(input("enter second number which less than 10: "))

number1 = x * 10 + y

print(number1)

x, y = y, x

number1 = x * 10 + y
print(number1)

