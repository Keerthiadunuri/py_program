#print count of total duplicates in the list
l=[]
def fun():
    n=int(input())
    for i in range(n):
        v=input()
        l.append(v)
    for j in range(n):
        if(l.count(l[j])==2):
            print(l[j])
fun()
        