import math
n = int(input("Enter a number: "))
def strong_number(x):
    temp = x
    s = 0
    while x > 0:
        d = x % 10
        s += math.factorial(d)
        x //= 10
    if s == temp:
        print("Strong number")
    else:
        print("Not a strong number")
strong_number(n)
