class BankAccount:
    
    def __init__(self):
        self.__balance=0
    def deposit(self,amount):
        self.__balance+=amount
        print(f"amount in account{self.__balance}")
    def withdraw(self,wamount):
        self.__balance-=wamount
        print(f"withrawn amount{self.__balance}")
    def get_balance(self):
        return self.__balance
b=BankAccount()
b.deposit(1000)
b.withdraw(200)
b.get_balance()
        