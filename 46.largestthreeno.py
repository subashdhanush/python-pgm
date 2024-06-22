def largest_numbers(numbers,n):
    sorted_list=sorted(numbers,reverse=True)
    ans=sorted_list[:n]
    return ans


numbers = [30, 10, 45, 5, 20, 50, 15, 3, 345, 54, 67, 87, 98, 100, 34]
N=int(input("enter a number"))
result=largest_numbers(numbers,N)
print(result)