def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

print("Select Operation")
print("1.Add")
print("2.Sub")
print("3.Mult")
print("4.Div")


while True:
    choice=input("enter a choice(1/2/3/4)")
    if choice in ('1','2','3','4'):
        try:
          num1=float(input("enter a number"))
          num2=float(input("enter a number"))
        except ValueError:
           print("Invalid input. Please enter a number.")
           continue    
        
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", sum(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", mul(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", div(num1, num2))

        next_calculation = input("Let's do next calculation? (yes/no):")
        if next_calculation == "no":
           break    
    else:
        print("Invalid Input")

