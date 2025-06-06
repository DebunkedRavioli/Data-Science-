
#Activity B

import pandas as pd
# A1\athlete_events.csv
df = pd.read_csv("athlete_events.csv")
print(df.head())
print(df.columns)

# Activtity C


import pandas as pd
# athlete_events.csv
df = pd.read_csv("athlete_events.csv")
print(df.head())
print(df.columns)
print(df['Sport'].value_counts().head())
print(df['Sex'].value_counts()) 
print(df.describe())
print(df['NOC'].nunique())
print(df['NOC'].unique())

