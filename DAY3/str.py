s=input("string 1")
s1=input("string 2")
def count_string():
    c=0
    for i in s:
        c+=1
    print(c)
def compare():
    if s==s1:
        print("true")
def concate():
    print(s+s1)
count_string()
compare()
concate()