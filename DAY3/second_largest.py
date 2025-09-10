l=[]
def largest():
    n=int(input())
    for i in range(n):
        v=int(input())
        l.append(v)
    if(l[0]>l[1]):
        m1=l[0]
        m2=l[1]
    else:
        m1=l[1]
        m2=l[0]
    for j in range(2,n):
        if(l[j]>m1):
            m2=m1
            m1=l[j]
        elif m2[j]>m1 and l[j]!=m2:
            m2=l[j]
    print(m2)
largest()