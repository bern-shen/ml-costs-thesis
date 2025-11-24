import pandas as pd

# Read the CSV file, treating GVKEY as string to preserve leading zeros
df = pd.read_csv('linker.csv', dtype={'GVKEY': str})

# Extract unique values from the GVKEY column (dropna to ignore empty values)
unique_gvkey = df['GVKEY'].dropna().unique()

# Write to gvkey.txt with one GVKEY per line
with open('gvkey.txt', 'w') as f:
    for val in unique_gvkey:
        f.write(val + '\n')

print(f"Extracted {len(unique_gvkey)} unique GVKEY values to gvkey.txt")
