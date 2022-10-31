count = 0
num = 2

while count < 50:
    isPrime = True
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break

    if isPrime:
        print(format(num, "4d"), end=" ")
        count += 1
        if count % 10 == 0:
            print()

    num += 1

