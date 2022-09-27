import math

x1, y1 = eval(input("Enter 1st point: "))
x2, y2 = eval(input("Enter 2nd point: "))
x3, y3 = eval(input("Enter 3rd point: "))

a = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
b = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
c = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

A = math.acos((a * a - b * b - c * c) / (-2 * b * c))
B = math.acos((b * b - a * a - c * c) / (-2 * a * c))
C = math.acos((c * c - b * b - a * a) / (-2 * a * b))

A = math.degrees(A)
B = math.degrees(B)
C = math.degrees(C)

print("The three angles are", A, B, C)
