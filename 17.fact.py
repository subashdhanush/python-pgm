num=5
fact=1
if num < 0:
    print("Does'nt accept Negative values")
for i in range(1,num+1):
    # print(i)
    fact=fact*num
    num=num-1
print(fact)    