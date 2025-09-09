n=int(input())
def pat(x):
    for i in range(x+1):
        for j in range(x+1):
            print("*",end="")
        print()
pat(n)