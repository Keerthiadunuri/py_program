s = input("Enter a string: ")

min_freq = min(s.count(ch) for ch in set(s))
chars = [ch for ch in set(s) if s.count(ch) == min_freq]

print("Minimum frequency:", min_freq)
print("Characters:", chars)
