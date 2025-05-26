import pandas as pd
# A1\athlete_events.csv
df = pd.read_csv("athlete_events.csv")
print(df.head())
print(df.columns)