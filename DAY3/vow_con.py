#count of vowels and consonants
str=input()
s="aeiouAEIOU"
def count():
    c=v=0
    for ch in str:
        if ch in s:
            v+=1
        else:
            c+=1
    print(f"vowels count:{v}\n consonants count:{c}")
count()