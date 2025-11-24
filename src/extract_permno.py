import pandas as pd

# Read the CSV file
df = pd.read_csv('membership.csv')

# Extract unique values from the permno column and convert to integers
unique_permno = df['permno'].dropna().unique()

# Write to members.txt with one permno per line
with open('members.txt', 'w') as f:
    for val in unique_permno:
        f.write(str(int(val)) + '\n')

print(f"Extracted {len(unique_permno)} unique permno values to members.txt")
