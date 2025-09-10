#print even odd elements in list
l=[]
e=[]
o=[]
def fun():
    n=int(input())
    for i in range(n):
        v=int(input())
        l.append(v)
    for j in range(n):
        if(l[j]%2==0):
            e.append(l[j])
        else:
            o.append(l[j])
    print('even',e)
    print('odd',o)
fun()
    