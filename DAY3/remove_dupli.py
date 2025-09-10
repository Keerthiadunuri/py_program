#remove duplicate elements in th list
l=[]
def  duplicate():
    n=int(input())
    for i in range(n):
        v=int(input())
        l.append(v)
    s=set(l)
    print(s)
duplicate()