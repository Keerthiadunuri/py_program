cust_no=int(input())
cust_name=input()
pmr=int(input())
lmr=int(input())
total_units=pmr-lmr
curr_bill=total_units*3.80
print( "cust_no  cust_name  pmr   lmr   total_units   curr_bill")
print( f" {cust_no}  {cust_name}  {pmr}  {lmr} {total_units}  {curr_bill}")