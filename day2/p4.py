n = int(input("Enter a number: "))

def pal(x):
    t = x
    rev = 0
    while x > 0:
        rem = x % 10
        rev = rev * 10 + rem
        x //= 10
    if rev == t:
        print("palindrome")
    else:
        print("not palindrome")

pal(n)
