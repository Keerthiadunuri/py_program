l=[]
p=int(input())
def List():
    for i in range(p):
        n=int(input())
        l.append(n)
    for j in range(p):
        if(l[j]<0):
            print(l[j])
List()