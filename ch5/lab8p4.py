print("Pattern 1")

for i in range(6):
    for j in range(i + 1):
        print(j + 1, end=" ")
    print()


print("\n\nPattern 2\n")

for i in range(6):
    for j in range(6 - i):
        print(j + 1, end=" ")
    print()


print("\n\nPattern 3\n")

for i in range(6):
    print("  " * (6 - i - 1), end="")
    for j in range(i + 1, 0, -1):
        print(j, end=" ")
    print()


print("\n\nPattern 4\n")

for i in range(6):
    print("  " * i, end="")
    for j in range(6 - i):
        print(j + 1, end=" ")
    print()


