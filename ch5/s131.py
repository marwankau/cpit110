print("  |", end="")
for i in range(1, 10):
    print(format(i, "5d"), end="")

print()
print("-" * 50)

for i in range(1, 10):
    print(format(i, "<2d"), end="|")
    for j in range(1, 10):
        print(format(j * i, "5d"), end="")
    print()
