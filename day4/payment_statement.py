class Payment:
    def __init__(self, amount):
        self.amount = amount
    def pay(self):
        print("Amount paid:", self.amount)
class CashPayment(Payment):
    def __init__(self, amount):
        super().__init__(amount)
    def pay(self):
        print(f"Paid {self.amount} through Cash")
class CardPayment(Payment):
    def __init__(self, amount):
        super().__init__(amount)
    def pay(self):
        print(f"Paid {self.amount} using Credit Card")
class Upipayment(Payment):
    def __init__(self, amount):
        super().__init__(amount)
    def pay(self):
        print(f"Paid {self.amount} using UPI")
c = CashPayment(500)
card = CardPayment(1200)
upi = Upipayment(750)
c.pay()
card.pay()
upi.pay()
payments = [CashPayment(1000), CardPayment(2000), Upipayment(1500)]

for p in payments:
    p.pay()

        
    
        