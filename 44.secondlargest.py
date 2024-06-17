numbers = [30, 10, 45, 5, 20]
numbers.sort(reverse=True)
if len(numbers)>2:
    second_largest=numbers[1]
    print(second_largest)
else:
    print("The list does not contain a second largest number.")    