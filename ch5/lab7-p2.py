print(format("kilogram", "14s"), format("pounds", "11s"), end="|")
print(" " * 5, format("pounds", "13s"), format("kilogram", "8s"))
print("-" * 56)

p = 20
for k in range(1, 200, 2):
    pounds = k * 2.2
    print(format(k, "<14d"), format(pounds, "6.1f"), " " * 4, end="|")

    kilo = p / 2.2
    print(" " * 5, format(p, "<13d"), format(kilo, "8.2f"))
    p += 5
