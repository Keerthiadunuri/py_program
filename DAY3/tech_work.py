day1=set()
day2=set()
day3=set()
def attend():
    n=int(input())
    print('emails of day1')
    for i in range(n):
        mail=input()
        mail=mail.lower()
        day1.add(mail)
    n1=int(input())
    print('emails on day2')
    for j in range(n):
        mail=input()
        mail=mail.lower()
        day2.add(mail)
    n2=int(input())
    print('email on day3')
    for k in range(n):
        mail=input()
        mail=mail.lower()
        day3.add(mail)
    print(f"no duplicates{day1}{day2}{day3}")
    t=(day1|day2|day3)
    print(f"unique attendees{t}")
    u=(day1&day2&day3)
    print(f"people attended three days{u}")
    t1=(day1 - day2 - day3) | (day2 - day1 - day3) | (day3 - day1 - day2)
    print(f"people attende only exactly one day{t1}")
    print(f"{day1&day2}{day2&day3}{day1&day3}")
    
    #last two  incomplete
    
attend()
    