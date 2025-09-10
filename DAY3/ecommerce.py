l=[]
def  ecomme():
    while True:
        print('1.add product to cart \n 2.remove product from the cart\n 3.serach product\n 4.display product\n 5.total products\n')
        n=int(input())
        if(n==1):
            p=input()
            l.append(p)
        elif(n==2):
            p1=input()
            l.remove(p1)
        elif (n==3):
            p2=input()
            if p2 in l:
                print("product",p2)
            else:
                print("not found")
        elif(n==4):
            print("products in the list",l)
        elif(n==5):
            print(len(l))
        elif(n==6):
            print(sorted(l))
        elif(n==7):
            print(l.clear())
        else:
            print("not valid")
            break
ecomme()
