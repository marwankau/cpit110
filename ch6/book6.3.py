def reverse(n):
    s = 0
    while n > 0:
        s = s * 10 + n % 10
        n = n // 10
    return s


def isPalindrome(number):
    return number == reverse(number)


m = eval(input("Enter an integer to check if it is palindrome: "))

b = isPalindrome(m)

print("The number is", ("" if b else "not"),  "palindrome")
