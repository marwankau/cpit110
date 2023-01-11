x1, y1 = eval(input("Enter x1 and y1 for point 1: "))
x2, y2 = eval(input("Enter x2 and y2 for point 2: "))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("The distance between the two points is", distance)