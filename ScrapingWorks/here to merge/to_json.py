import pandas as pd

df = pd.read_csv('finalized.csv')
df.to_json('finalized.json', orient='records')