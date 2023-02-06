for i in range(1, 7):
    print("  " * (6 - i), end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()