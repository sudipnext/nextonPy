import pandas as pd

# Read the CSV file
df = pd.read_csv("characters_data1.csv")

# Remove duplicates
df = df.drop_duplicates(subset=['Node Name'])


# Save the updated file
df.to_csv('anime.csv', index=False)
