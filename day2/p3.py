n=int(input())
def pat(x):
    for i in range(x):
        for j in range(x):
            if(i==j):
                print(" $ ",end="")
            elif(i+j==x-1):
                print(" $ ",end="")
            else:
                print(" * ",end="")
        print()
pat(n)
    