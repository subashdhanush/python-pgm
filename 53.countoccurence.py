count=0
my_list = [1, 2, 3, 4, 2, 5, 2, 3, 4, 6, 5]
occurence=int(input("enter a numer"))
for i in my_list:
    if i == occurence:
        count=count+1
print(count)        
