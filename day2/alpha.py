n=input()
alpha="abcdefghijklmnopqrstuvwxyzQWERTYUIOPLAKSJDHFGZMXNCBV"
digit="0123456789"
def func(x):
    if (x in alpha):
        print("it is a alphabet")
    elif (x in digit):
        print("it is a digit")
    else:
        print("it is a special character")
func(n)