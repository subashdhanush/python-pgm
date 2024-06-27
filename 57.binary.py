def isbinary(input_str):
    for i in input_str:
        if i not in '01':
            return False
    return True        

input_str="1011110"

if isbinary(input_str):
    print("it is a binary")
else:
    print("it is not a binary")    