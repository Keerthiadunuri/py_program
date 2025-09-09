n=int(input())
def armstrong(x):
    s=0
    t=x
    while(t>0):
        r=t%10
        s=s+(r*r*r)
        t=t//10
    if(s==x):
        print("armstrong")
    else:
        print("not armstrong")
armstrong(n)