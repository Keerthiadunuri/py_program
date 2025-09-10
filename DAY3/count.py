s=input()
def counts():
    d=0
    a=0
    sp=0
    for i in s:
        if(i.isdigit()):
            d+=1
        elif(i.isalpha()):
            a+=1
        else:
            sp+=1
    print(f"digits{d} alpha{a} special chars{sp}")
counts()
            