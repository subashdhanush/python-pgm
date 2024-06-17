mystr=input("enter a string")
words=[words.capitalize() for words in mystr.split()]
words.sort()

for i in words:
    print(i)