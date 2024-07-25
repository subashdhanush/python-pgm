sentence=input("enter a sentence")
lettercount=0
digitcount=0
for char in sentence:
    if char.isalpha():
        lettercount=lettercount+1
    elif char.isdigit():
        digitcount=digitcount+1    
print(lettercount)
print(digitcount)