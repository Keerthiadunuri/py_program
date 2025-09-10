#count frequency of elements in the list 10->2
l=[]
def fun():
    n=int(input())
    for i in range(n):
        v=input()
        l.append(v)
    s=set()
    for j in range(n):
        if l[j] not in s:
            print(l[j],'->',l.count(l[j]))
            s.add(l[j])
fun()