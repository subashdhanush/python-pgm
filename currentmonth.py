import datetime

# Get the current month
current_month = datetime.datetime.now().month
print(current_month)
# Assume some operation occurs here, and time passes...
current_year = datetime.datetime.now().year
last_two_digits = current_year % 100
print(last_two_digits)
# Get the new current month after some time
new_month = datetime.datetime.now().month

# Check if the month has changed
if current_month != new_month:
    print(f"Month has changed from {current_month} to {new_month}")
else:
    print("Month is still the same.")
