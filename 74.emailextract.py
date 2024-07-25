def extractusername(email):
    parts=email.split('@')
    print(parts)

    if len(parts) == 2:
        return parts[0]
    else:
        return "Invalid Email format"

try:
    email=input("enter an mail address") 
    username=extractusername(email)
    print(username)
except ValueError:
     print("Invalid input. Please enter a valid email address.")
