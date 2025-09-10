#highest frequency of a character
s = input("Enter a string: ")

max_freq = max(s.count(ch) for ch in set(s))
max_chars = [ch for ch in set(s) if s.count(ch) == max_freq]

print("Max frequency:", max_freq)
print("Characters:", max_chars)
