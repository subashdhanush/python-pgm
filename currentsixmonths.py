from datetime import datetime
import calendar

# Get the current month and year
current_month = datetime.now().month

# List to store the names of the next 6 months
next_six_months = []

# Loop to get the next 6 months
for i in range(6):
    # Calculate the month index (1-12)
    month_index = (current_month + i - 1) % 12 + 1
    
    # Append the month name to the list
    next_six_months.append(calendar.month_name[month_index])

# Print the next 6 months
print(next_six_months)