

# Week 2


 ### Activity 1 

1. How many columns are in the dataset?

Answer: The amount of columns in the dataset is 15 and the amount of rows is 5. 

2. Name three of them and explain what they represent.

Answer:
The three columns in the data sets represent the name, gender and what sport they participated in. 

3. What do the first 5 rows show?

Answer: The first 5 rows show the athletes names, gender and sport. 

### Activity 2:

After including this line of code: print(df['Sport'].value_counts().head())
print(df['Sex'].value_counts())

I found out that the top 5 sports where:

Athletics,Gymansatics,Swimming,Shooting and Cycling.(In Order)

And the amount of Female Vs Male Athletes were:

Male Athletes - 196594
Female Athletes - 74522 


### Activity 3:
 
Q1: How many columns are in the dataset?

There are 15 columns.

Q2: Name 3 of them and explain what they represent.

Age,Gender and Event. Each cloumn shows us key details of the participant. 

Q3: What do the first 5 rows show?

The first 5 rows shows each sport, names, gender and Medal.  
  

### Activity 4 

Q1: What are the top 5 sports? 

The top 5 sports are Athletics, Gymanstics, Swimming, Shooting and Cycling. 

Q2: How many male vs female athletes?

There are 196594 Male Athletes and 74522 Female Athletes. 

### Activity 5 

Q1: What’s the average age?

The Average is 25 years old

Q2: What’s the oldest and youngest athlete?

The youngest athlete is 10 years old and the oldest athlete is 97 years old. 

Q3: Are there any columns with missing or strange values?

All the columns with any missing values are replaced with N/A. 

Extension: Explore Country Code

The following country codes stand for:

URS-
Soviet Union

GDR-East Germany

FRG-West Germany 

### Reflection:

Q1: What’s one thing you learned about the Olympics dataset?

One thing that I learned from the olympic dataset was the youngest athlete was 10 years old and the oldest athlete was 97 years old. 

Q2: What did you find challenging in setting up or running Pandas?

Nothing. Only thing I had to do was pip install pandas.

Q3: What’s something you'd like to analyse next?

Something else that I would like to analyse is the bus timetables so we can make bus transport more efficient and safer. 



# Week 3:  Filtering, Sorting & Grouping – Finding Patterns in Data

## Task 1 

### Reflect:

What do these filters do? 

These filters help isolate specific rows from the dataset. The first one selects only female athletes, and the second one filters for athletes older than 35 years. 

How many rows were returned? Use len().

Number of female athletes: len(female_athletes) → 74352

Number of athletes older than 35: len(older_athletes) → 2349

## Task 2 

### Create A New Filter

aussie_swimmers = df[(df['Team'] == 'Australia') & (df['Sport'] == 'Swimming')]
print(aussie_swimmers[['Name', 'Age', 'Sex', 'Year']].head())
print("Number of Australian swimmers:", len(aussie_swimmers))

This filter is for athletes from Australia in Swimming. 

## Task 3 

### Apply the Skill 

                        Name  Height  Weight       Sport
265040                Yao Ming   226.0   141.0  Basketball
265041                Yao Ming   226.0   141.0  Basketball
265042                Yao Ming   226.0   141.0  Basketball
207373   Arvydas Romas Sabonis   223.0   122.0  Basketball
207374   Arvydas Romas Sabonis   223.0   122.0  Basketball
207375   Arvydas Romas Sabonis   223.0   122.0  Basketball
32376     Tommy Loren Burleson   223.0   102.0  Basketball
59371   Roberto Dueas Hernndez   221.0   137.0  Basketball
59372   Roberto Dueas Hernndez   221.0   137.0  Basketball
17669           Gunther Behnke   221.0   114.0  Basketball

    Name  Weight      Sport
23155               Ricardo Blas, Jr.   214.0       Judo
23156               Ricardo Blas, Jr.   214.0       Judo
205467              Aytami Ruano Vega   198.0       Judo
75031                   Marek Galiski   190.0  Wrestling
237039  Christopher J. "Chris" Taylor   182.0  Wrestling

## Task 4

### Apply the Skill

Sport with most female participants: Athletics
Number of female participants in that sport: 116662



# More Sorting Acitivites

## Task 5 

### Aggregating with groupby()













