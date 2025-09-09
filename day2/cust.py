cust_no = int(input("Enter customer number: "))
cust_name = input("Enter customer name: ")
pmr = int(input("Enter present month reading: "))
lmr = int(input("Enter last month reading: "))

total_units = pmr - lmr

def curr(units):
    if units <= 50:
        return units * 3.80
    elif units <= 100:
        return 50 * 3.80 + (units - 50) * 4.20
    elif units <= 200:
        return 50 * 3.80 + 50 * 4.20 + (units - 100) * 5.10
    elif units <= 300:
        return 50 * 3.80 + 50 * 4.20 + 100 * 5.10 + (units - 200) * 6.30
    else:
        return 50 * 3.80 + 50 * 4.20 + 100 * 5.10 + 100 * 6.30 + (units - 300) * 7.50

curr_bill = curr(total_units)

print("\n---- Electricity Bill ----")
print("cust_no  cust_name  pmr   lmr   total_units   curr_bill")
print(f"{cust_no:<8}{cust_name:<11}{pmr:<6}{lmr:<6}{total_units:<13}{curr_bill:.2f}")
