#print all unique elements in the lsit
l=[]
def  uni():
    n=int(input())
    for i in range(n):
        v=int(input())
        l.append(v)
    s=set(l)
    print(s)
uni()