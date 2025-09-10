l=[]
l1=[]
def uni():
    n=int(input())
    for i in range(n):
        v=input()
        l.append(v)
    for j in range(n):
        if l.count(l[j])==1:
            l1.append(l[j])
            print(l1)
uni()