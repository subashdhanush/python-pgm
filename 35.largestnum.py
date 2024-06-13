def findlargestnum(arr):
    if not arr:
        return "Array is empty"
    largest_element=arr[0]
    for element in arr:
        if element > largest_element:
            largest_element=element
    return largest_element            


array=[10,99,30,50]
result=findlargestnum(array)
print(result)