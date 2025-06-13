

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

Created a new group that shows average weight by Sex and Sport

## Task 6 

### Exporting A Subset 

 I have exported:

All athletes under 18

All athletes who won a gold medal


### Reflection Journal 


What was the easiest filtering task and why?

The most easiest one was filterning Male and Female athletes because there was only two things. 

What was the most difficult grouping or sorting task?

The most difficult was aggregating with group by()

What trends surprised you in the Olympic data?

Trends were that there were more male athletes

What kinds of real-world questions could this kind of analysis help answer?

That more female althletes need to be in the Olympics

# Internal, Exportinh and Loading Data Files



    df = pd.DataFrame(data)
    
    # Display the DataFrame
    print("DataFrame:")
    print(df)

    # Save the DataFrame to a CSV file
    df.to_csv('sample_data.csv', index=False)
    print("\nDataFrame saved to 'sample_data.csv'.")

    # Read the DataFrame from the CSV file
    df_loaded = pd.read_csv('sample_data.csv')

    print("\nDataFrame loaded from 'sample_data.csv':")

    # Display the loaded DataFrame
    print(df_loaded)




#### Why do you think these three operations are key to working with data and information?

I think these three operations are useful because it can improve your coding skills as well as teach you how to use the dictionary and make new databases on the go.




# Week 4 

## Data Cleaning – Preparing Messy Data

### Task 1: Check for Missing Data
# Count missing values in each column



Which 3 columns have the most missing values?

Age, Weight and Height

Why might this happen in real-world Olympic data?

The reason why there might be a lot of missing values in the real Olympics may be because of athletes lying about their age weight and height as they are all factors which can affect their performance in the Olympics. 



## Task 2: Drop Rows with Critical Missing Data

How many rows did you remove?

I removed 2 rows

What are the pros and cons of dropping data?

The pros is that you can sort through the good data quicker when all the useless one has been dropped but sometimes you might need some of the data in the 'useless code' so it can be bit tricky. 


## Task 3: Fill Missing Values (e.g. 'Medal')


-Replace missing Weight with average weight



-Use .median() instead of .mean() and compare

## Task 4: Detect Inconsistent Data


-Extra spaces or capitalisation issues

-Typos or strange values


## Task 5: Validate and Describe Cleaned Data

Reflection:

Did cleaning improve the dataset?

Yes it did 

What questions could now be answered more confidently?

The Age, Weight and Height of competitors. 

## Task 6: Save the Clean Dataset

Check:

-Open the CSV in Excel or Sheets

-Is it readable, complete, and useful?