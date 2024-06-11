def bodymassindex(height,weight):
    return round((weight/height**2),2)

h=float(input("enter your height"))
w=float(input("enter your weight"))

bmi=bodymassindex(h,w)

if bmi <= 18.5:
   print("You are underweight.")
elif 18.5 < bmi <= 24.9:
   print("Your weight is normal.")
elif 25 < bmi <= 29.29:
   print("You are overweight.")
else:
   print("You are obese.")