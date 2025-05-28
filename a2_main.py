import pandas as pd
# athlete_events.csv
df = pd.read_csv("athlete_events.csv")
print(df.head())
print(df.columns)
print(df['Sport'].value_counts().head())
print(df['Sex'].value_counts()) 