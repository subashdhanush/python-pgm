n1=0
n2=1
count=0
nterms=int(input("enter a number"))
while count < nterms:
    print(n1)
    # print(n2)
    result=n1+n2
    n1=n2
    n2=result
    count=count+1
