import math
C=50
H=30

def calculate_Q(D):
    return int(math.sqrt((2*C*D)/H))



input_sequence = input("Enter comma-separated values of D: ")
D_values = input_sequence.split(',')

result=[calculate_Q(int(D)) for D in D_values]
print(','.join(map(str, result)))