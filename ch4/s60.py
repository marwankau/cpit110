import random

i = random.randint(0, 100)
j = random.randint(0, 100)
k = random.randint(0, 100)

print("i =", i, "j =", j, "k =", k)

if i > k:
    if j > k:
        print("both i and j greater than k")
else:
    print("i less or equal k but we don't know about j")
