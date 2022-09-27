print("---------------------------------")
print(format("x|", ">6s"), format("x^2", "12s"), "√x")
print("---------------------------------")
x = 5
print(format(str(x) + "|", ">6s"), format(x ** 2, "<12.2f"), format(x ** 0.5, ".2f"))
x = 500
print(format(str(x) + "|", ">6s"), format(x ** 2, "<12.2f"), format(x ** 0.5, ".2f"))
x = 20
print(format(str(x) + "|", ">6s"), format(x ** 2, "<12.2f"), format(x ** 0.5, ".2f"))
x = 3000
print(format(str(x) + "|", ">6s"), format(x ** 2, "<12.2f"), format(x ** 0.5, ".2f"))
print("---------------------------------")
