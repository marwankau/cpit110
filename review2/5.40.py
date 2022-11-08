import random

head = 0
tail = 0

for i in range(1000_000):
    c = random.randint(0, 1)   # 0: head, 1: tail
    if c == 0:
        head += 1
    else:
        tail += 1

print("head appears", head, "times", format(head / 1000_000, ".2%"))
print("tails appears", tail, "times", format(tail / 1000_000, ".2%"))
