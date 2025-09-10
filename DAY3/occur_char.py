s=input()
def ch():
    printed=set()
    res=""
    for i in s:
        if i not in printed:
            res+=i+str((s.count(i)))
            print(res)
            printed.add(i)
ch()