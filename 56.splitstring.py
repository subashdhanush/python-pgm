input_str = "Python program to split and join a string"
print(input_str)
word_list = input_str.split() # By default, split on whitespace
print(word_list)
separator = " " # specify the separator between words
output_str = separator.join(word_list)
print(output_str)