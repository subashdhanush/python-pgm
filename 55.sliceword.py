def removechar(input_str,i):
    if i < 0 or i > len(input_str):
        print(f"Invalid index {i}. The string remains unchanged.")
        return input_str
    result_str=input_str[:i] + input_str[i+1:]
    return result_str    

input_str="Hello, wWorld!"
i=7
newstr=removechar(input_str,i)
print(newstr)