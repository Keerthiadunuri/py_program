a=int(input())
b=int(input())
c=int(input())
def largestn(a,b,c):
    if(a>b):
        if(a>c):
            print("a is largest",a)
        else:
            print("c is largest",c)
    else:
        if(b>c):
            print("b is largest",b)
        else:
            print("c is largest",c)
largestn(a,b,c)