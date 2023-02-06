def sum(start, end):
    s = 0
    for i in range(start, end + 1):
        s += i
    print("Sum from", start, " to ", end, " is", s)


sum(1, 10)
sum(20, 37)
sum(35, 49)