
print("kilograms      pounds        |     pounds       kilograms")
print("-" * 65)

from_pound = 20

for kilo in range(1, 200, 2):
    pounds = kilo * 2.2
    to_kilo = from_pound * 0.45
    print(format(kilo, "<10d"), format(pounds, "10.1f"), format("|", ">8s"), " " * 3, format(from_pound, "<10d"), format(to_kilo, "10.2f"))

    from_pound += 5