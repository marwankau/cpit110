a, b, c = eval(input("Enter a, b, c: "))
discriminant = b ** 2 - 4 * a * c

if discriminant > 0:   # positive equation has two roots
    r1 = (-b + discriminant ** 0.5) / (2 * a)
    r2 = (-b - discriminant ** 0.5) / (2 * a)
    print("The roots are", round(r1, 6), "and", round(r2, 6))
elif discriminant == 0:
    r = -b / (2 * a)
    print("The root is", round(r, 6))
else:
    print("The equation has no root!")
