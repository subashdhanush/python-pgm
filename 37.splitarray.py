def split_array(arr,k):
    if k <= 0 or k >= len(arr):
       return arr 
    first_part=arr[:k]
    second_part=arr[k:]
    result=second_part+first_part

    return result   

arr=[1,2,3,4,5]
k=3
result=split_array(arr,k)
print("Original Array:", arr)
print("Array after splitting and adding:", result)