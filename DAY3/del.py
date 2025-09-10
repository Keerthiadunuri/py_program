#program to delete specified position elemnt in list
l=[]
def dele():
    n=int(input())
    for i in range(n):
        v=input()
        l.append(v)
    p=int(input())
    del l[p]
    print(l)
dele()