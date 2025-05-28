import pandas as pd

# Read in CSV file
df = pd.read_csv('digital_diet_mental_health.csv')

# Drop duplicates
df = df.drop_duplicates()

print(df.info())          # Check data types and nulls
print(df.isnull().sum())  # Show missing values
print(df.duplicated().sum())  # Count duplicates
print(df.describe())      # Look for outliers or strange stats
# # Fill missing values with mean
# df = df.fillna(df.mean())

# # Convert data types
# df['date'] = pd.to_datetime(df['date'])
# df['amount'] = df['amount'].astype(float)

# # Define custom cleaning function
# def clean_name(name):
#     return name.strip().title()

# # Apply custom function to 'name' column
# df['name'] = df['name'].apply(clean_name)

# # Write cleaned data to CSV file
# df.to_csv('output.csv', index=False)