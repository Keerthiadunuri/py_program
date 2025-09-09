n = int(input("Enter amount: "))

def count_notes(n):
    notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    c = 0
    for note in notes:
        if n >= note:
            num = n // note
            c += num
            n = n % note
    print("Total notes:", c)

count_notes(n)
