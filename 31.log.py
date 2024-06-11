import math

num=float(input("enter a number"))

if num<=0:
    print("enter a positive number")
else:
    result=math.log(num)
    print(f"the natural of logarithm of {num} is {result}")    