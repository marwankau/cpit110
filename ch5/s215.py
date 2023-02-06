count = 0
num = 2
while count < 50:
    isPrime = True
    for x in range(num - 1, 1, -1):
        if num % x == 0:
            isPrime = False
            break
    if isPrime:
        count += 1   # if the number is prime
        print(format(num, "5d"), end=" ")
        if count % 10 == 0:
            print()
    num += 1
