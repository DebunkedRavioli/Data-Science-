import pandas as pd

df = pd.read_csv('athlete_events.csv')



# Filter for female athletes only
female_athletes = df[df['Sex'] == 'F']
print(female_athletes.head())

# Filter for athletes older than 35
older_athletes = df[df['Age'] > 35]
print(older_athletes[['Name', 'Age', 'Sport']].head())

# Female athletes over 30
combo_filter = df[(df['Sex'] == 'F') & (df['Age'] > 30)]
print(combo_filter[['Name', 'Age', 'Sport']].head())

# Male athletes in Basketball
basketball_males = df[(df['Sex'] == 'M') & (df['Sport'] == 'Basketball')]
print(basketball_males.head())

# Australian athletes in Swimming
aussie_swimmers = df[(df['Team'] == 'Australia') & (df['Sport'] == 'Swimming')]
print(aussie_swimmers[['Name', 'Age', 'Sex', 'Year']].head())
print("Number of Australian swimmers:", len(aussie_swimmers))


sorted_by_age = df.sort_values(by='Age', ascending=False)
print(sorted_by_age[['Name', 'Age', 'Sport']].head())

# Sort by weight
sorted_by_weight = df.sort_values(by='Weight', ascending=False)
print(sorted_by_weight[['Name', 'Weight', 'Sport']].head())

# Sort by height then weight (both descending)
sorted_height_weight = df.sort_values(by=['Height', 'Weight'], ascending=False)
print(sorted_height_weight[['Name', 'Height', 'Weight', 'Sport']].head(10))


# Count participants in each sport
sport_counts = df['Sport'].value_counts()
print(sport_counts.head())

# Count medals per team
medals_by_team = df[df['Medal'].notnull()].groupby('Team')['Medal'].count()
print(medals_by_team.sort_values(ascending=False).head())

# Sport with most female participants
female_sports = df[df['Sex'] == 'F']['Sport'].value_counts()
print("Sport with most female participants:", female_sports.idxmax())
print("Number of female participants in that sport:", female_sports.max())

# Average height per sport
avg_height = df.groupby('Sport')['Height'].mean().sort_values(ascending=False)
print(avg_height.head())

# Median age by year
median_age_by_year = df.groupby('Year')['Age'].median()
print(median_age_by_year.tail())

# Sorted by Sex and Sport
avg_weight = df.groupby(['Sex', 'Sport'])['Weight'].mean()
print(avg_weight.head())
