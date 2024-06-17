punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

mystr=input("enter a string")

punt=""
for char in mystr:
    if char not in punctuations:
        punt=punt+char

print(punt)