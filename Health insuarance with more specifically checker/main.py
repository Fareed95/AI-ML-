import pandas as pd

# Data extracted from the image
data = {
    "Age": [25, 30, 35, 40, 45],
    "Height": [162.56, 172.72, 167.64, 157.48, 157.48],
    "Weight": [70, 95, 78, 110, 85],
    "Premium": [18000, 38000, 38000, 60000, 70000]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Saving the DataFrame to a CSV file
file_path = 'Term_Insurance_Dataset.csv'
df.to_csv(file_path, index=False)

file_path