def sum(begin, end):
    s = 0

    for i in range(begin, end + 1):
        s += i

    print(begin, "to", end, "sum =", s)


sum(1, 10)  # call function sum
