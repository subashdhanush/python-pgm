from collections import OrderedDict
def check_order(string, reference):
    string_dict = OrderedDict.fromkeys(string)
    reference_dict = OrderedDict.fromkeys(reference)
    print("string_dict",string_dict)
    print("reference_dict",reference_dict)
    return string_dict == reference_dict
# Input strings
input_string = "hello world"
reference_string = "helo wrd"
# Check if the order of characters in input_string matches reference_st
if check_order(input_string, reference_string):
 print("The order of characters in the input string matches")
else:
 print("The order of characters in the input string does not match")