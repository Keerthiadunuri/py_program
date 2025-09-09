n=int(input())
def pat(x):
    for i in range(x):
        for j in range(x):
            if(i==j):
                print("$",end="")
            else:
                print("*",end="")
        print()
pat(n)