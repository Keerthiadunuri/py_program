#libraray management system....
d={}
def lib():
    while(True):
        print(f"1.add\n2.delete\n3.search\n4.update\n5.display\n6.length\n7.check\n")
        ch=int(input("enter choice"))
        if(ch==1):
            n=int(input("No. of books to be added"))
            for i in range(n):
                k=input("Book Id:")
                v=input("Book Title:")
                d[k]=v
            print(d)
        elif(ch==2):
            id=input("enter BookId to be deleted")
            del d[id]
        elif(ch==3):
            id1=input("enter Id to be searched")
            print(d[id1])
        elif(ch==4):
            id2=input("enter the id where title is to corrected")
            title=input()
            d[id2]=title
        elif(ch==5):
            print(f"displaying all books{d}")
        elif(ch==6):
            print("length of books",len(d))
        elif(ch==7):
            ti=input()
            if(ti in d.values()):
                print("yes title exists")
            else:
                print("doesnt exist")
        elif(ch==8):
            break
        else:
            print("Invalid")
lib()

