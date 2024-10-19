import pandas as pd
import matplotlib.pyplot as plt


print("Starting the script...")


# Create a simple Pandas DataFrame
data = {
    'Year': [2020, 2021, 2022],
    'Sales': [100, 150, 200]
}

df = pd.DataFrame(data)

# Print DataFrame
print(df)

# Plot the data
plt.plot(df['Year'], df['Sales'], marker='o')
plt.title('Sales Over Years')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.show()
