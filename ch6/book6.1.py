def getPentagonalNumber(n):
    p = n * (3 * n - 1) // 2

    return p


for i in range(1, 101):
    p = getPentagonalNumber(i)
    print(format(p, "7d"), end="")
    if i % 10 == 0:
        print()
