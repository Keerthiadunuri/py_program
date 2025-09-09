n=int(input())
def prime(x):
    for i in range(1,n):
        if(i%n)==0:
            c=c+1
    if(c==2):
        print("prime")
    else:
        print("not a prime")
prime(n)
        
            