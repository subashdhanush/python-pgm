arm=int(input("enter a program"))
sumdigit=0
armtemp=arm
while armtemp > 0:
    digit=armtemp%10
    sumdigit=digit*digit*digit+sumdigit
    armtemp=armtemp//10   
if arm == sumdigit:
    print("Arm Strong")
else:
    print("Not Arm Strong")        

