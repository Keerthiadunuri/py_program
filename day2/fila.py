n = int(input("Enter a number: "))
last = n % 10
first = n
while first >= 10:
    first //= 10
print("Sum of first and last digit:", first + last)
