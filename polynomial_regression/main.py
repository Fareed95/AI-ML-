import pandas as pd

# Define the data
data = {
    'Position': [
        'Business Analyst',
        'Junior Consultant',
        'Senior Consultant',
        'Manager',
        'Country Manager',
        'Region Manager',
        'Partner',
        'Senior Partner',
        'C-level',
        'CEO'
    ],
    'Level (X-variable)': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Salary (Y-variable)': [
        45000, 50000, 60000, 80000, 110000, 150000, 200000, 300000, 500000, 1000000
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('positions_salaries.csv', index=False)
