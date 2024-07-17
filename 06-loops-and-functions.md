---
title: Data Workflows and Automation
teaching: 40
exercises: 50
---

::::::::::::::::::::::::::::::::::::::: objectives

- Describe why for loops are used in Python.
- Employ for loops to automate data analysis.
- Write unique filenames in Python.
- Build reusable code in Python.
- Write functions using conditional statements (if, then, else).

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- Can I automate operations in Python?
- What are functions and why should I use them?

::::::::::::::::::::::::::::::::::::::::::::::::::

So far, we've used Python and the pandas library to explore and manipulate
individual datasets by hand, much like we would do in a spreadsheet. The beauty
of using a programming language like Python, though, comes from the ability to
automate data processing through the use of loops and functions.

## For loops

Loops allow us to repeat a workflow (or series of actions) a given number of
times or while some condition is true. We would use a loop to automatically
process data that's stored in multiple files (daily values with one file per
year, for example). Loops lighten our work load by performing repeated tasks
without our direct involvement and make it less likely that we'll introduce
errors by making mistakes while processing each file by hand.

Let's write a simple for loop that simulates what a kid might see during a
visit to the zoo:

```python
animals = ['lion', 'tiger', 'crocodile', 'vulture', 'hippo']
print(animals)
```

```output
['lion', 'tiger', 'crocodile', 'vulture', 'hippo']
```

```python
for creature in animals:
    print(creature)
```

```output
lion
tiger
crocodile
vulture
hippo
```

The line defining the loop must start with `for` and end with a colon, and the
body of the loop must be indented.

In this example, `creature` is the loop variable that takes the value of the next
entry in `animals` every time the loop goes around. We can call the loop variable
anything we like. After the loop finishes, the loop variable will still exist
and will have the value of the last entry in the collection:

```python
animals = ['lion', 'tiger', 'crocodile', 'vulture', 'hippo']
for creature in animals:
    pass
```

```output
```

```python
print('The loop variable is now: ' + creature)
```

```output
The loop variable is now: hippo
```

We are not asking Python to print the value of the loop variable anymore, but
the for loop still runs and the value of `creature` changes on each pass through
the loop. The statement `pass` in the body of the loop means "do nothing".

:::::::::::::::::::::::::::::::::::::::  challenge

## Challenge - Loops

1. What happens if we don't include the `pass` statement?

2. Rewrite the loop so that the animals are separated by commas, not new lines
  (Hint: You can concatenate strings using a plus sign. For example,
  `print(string1 + string2)` outputs 'string1string2').

::::::::::::::::::::::: solution

1. 
    ```python
    animals = ['lion', 'tiger', 'crocodile', 'vulture', 'hippo']
    for creature in animals:
    
    ```
    
    ```error
    IndentationError: expected an indented block
    ```

2. Using the `end` argument to `print`:
    
    ```python
    for creature in animals:
        print(creature + ',', end='')
    ```

    ```output
    lion,tiger,crocodile,vulture,hippo,
    ```
    
   This puts a comma on the end of the list, which is not ideal.
   To avoid this, we need to use an altogether different approach:
   string objects in Python have a `join` method, 
   which can be used to concatenate items in a list with the string in between, e.g.
   
    ```python
    ', '.join(animals)
    ```
    
    ```output
    'lion, tiger, crocodile, vulture, hippo'
    ```
   
::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

## Automating data processing using For Loops

The file we've been using so far, `surveys.csv`, contains 25 years of data and is
very large. We would like to separate the data for each year into a separate
file.

Let's start by making a new directory inside the folder `data` to store all of
these files using the module `os`:

```python
import os

os.mkdir('data/yearly_files')
```

The command `os.mkdir` is equivalent to `mkdir` in the shell. Just so we are
sure, we can check that the new directory was created within the `data` folder:

```python
os.listdir('data')
```

```output
['plots.csv',
 'portal_mammals.sqlite',
 'species.csv',
 'survey2001.csv',
 'survey2002.csv',
 'surveys.csv',
 'surveys2002_temp.csv',
 'yearly_files']
```

The command `os.listdir` is equivalent to `ls` in the shell.

In previous lessons, we saw how to use the library pandas to load the species
data into memory as a DataFrame, how to select a subset of the data using some
criteria, and how to write the DataFrame into a CSV file. Let's write a script
that performs those three steps in sequence for the year 2002:

```python
import pandas as pd

# Load the data into a DataFrame
surveys_df = pd.read_csv('data/surveys.csv')

# Select only data for the year 2002
surveys2002 = surveys_df[surveys_df.year == 2002]

# Write the new DataFrame to a CSV file
surveys2002.to_csv('data/yearly_files/surveys2002.csv')
```

To create yearly data files, we could repeat the last two commands over and
over, once for each year of data. Repeating code is neither elegant nor
practical, and is very likely to introduce errors into your code. We want to
turn what we've just written into a loop that repeats the last two commands for
every year in the dataset.

Let's start by writing a loop that prints the names of the files we want
to create - the dataset we are using covers 1977 through 2002, and we'll create
a separate file for each of those years. Listing the filenames is a good way to
confirm that the loop is behaving as we expect.

We have seen that we can loop over a list of items, so we need a list of years
to loop over. We can get the years in our DataFrame with:

```python
surveys_df['year']
```

```output
0        1977
1        1977
2        1977
3        1977
         ...
35545    2002
35546    2002
35547    2002
35548    2002
```

but we want only unique years, which we can get using the `unique` method
which we have already seen.

```python
surveys_df['year'].unique()
```

```output
array([1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987,
       1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998,
       1999, 2000, 2001, 2002], dtype=int64)
```

Putting this into our for loop we get

```python
for year in surveys_df['year'].unique():
   filename='data/yearly_files/surveys' + str(year) + '.csv'
   print(filename)
```

```output
data/yearly_files/surveys1977.csv
data/yearly_files/surveys1978.csv
data/yearly_files/surveys1979.csv
data/yearly_files/surveys1980.csv
data/yearly_files/surveys1981.csv
data/yearly_files/surveys1982.csv
data/yearly_files/surveys1983.csv
data/yearly_files/surveys1984.csv
data/yearly_files/surveys1985.csv
data/yearly_files/surveys1986.csv
data/yearly_files/surveys1987.csv
data/yearly_files/surveys1988.csv
data/yearly_files/surveys1989.csv
data/yearly_files/surveys1990.csv
data/yearly_files/surveys1991.csv
data/yearly_files/surveys1992.csv
data/yearly_files/surveys1993.csv
data/yearly_files/surveys1994.csv
data/yearly_files/surveys1995.csv
data/yearly_files/surveys1996.csv
data/yearly_files/surveys1997.csv
data/yearly_files/surveys1998.csv
data/yearly_files/surveys1999.csv
data/yearly_files/surveys2000.csv
data/yearly_files/surveys2001.csv
data/yearly_files/surveys2002.csv
```

We can now add the rest of the steps we need to create separate text files:

```python
# Load the data into a DataFrame
surveys_df = pd.read_csv('data/surveys.csv')

for year in surveys_df['year'].unique():

    # Select data for the year
    surveys_year = surveys_df[surveys_df.year == year]

    # Write the new DataFrame to a CSV file
    filename = 'data/yearly_files/surveys' + str(year) + '.csv'
    surveys_year.to_csv(filename)
```

Look inside the `yearly_files` directory and check a couple of the files you
just created to confirm that everything worked as expected.

## Writing Unique File Names

Notice that the code above created a unique filename for each year.

```python
filename = 'data/yearly_files/surveys' + str(year) + '.csv'
```

Let's break down the parts of this name:

- The first part is some text that specifies the directory to store our
  data file in (data/yearly\_files/) and the first part of the file name
  (surveys): `'data/yearly_files/surveys'`
- We can concatenate this with the value of a variable, in this case `year` by
  using the plus `+` sign and the variable we want to add to the file name: `+ str(year)`
- Then we add the file extension as another text string: `+ '.csv'`

Notice that we use single quotes to add text strings. The variable is not
surrounded by quotes. This code produces the string
`data/yearly_files/surveys2002.csv` which contains the path to the new filename
AND the file name itself.

:::::::::::::::::::::::::::::::::::::::  challenge

## Challenge - Modifying loops

1. Some of the surveys you saved are missing data (they have null values that
  show up as NaN - Not A Number - in the DataFrames and do not show up in the text
  files). Modify the for loop so that the entries with null values are not
  included in the yearly files.

2. Let's say you only want to look at data from a given multiple of years. How would you modify your loop in order to generate a data file for only every 5th year, starting from 1977?

3. Instead of splitting out the data by years, a colleague wants to do analyses each species separately. How would you write a unique CSV file for each species?

::::::::::::::::::::::: solution

1.
   ```python
   surveys_year = surveys_df[surveys_df.year == year].dropna()
   ```
2. You could just make a list manually,
   however, why not check the first and last year making use of the code itself?
   
   ```python
   n_year = 5  # better overview by making variable from it
   first_year = surveys_df['year'].min()
   last_year = surveys_df['year'].max()
   
   for year in range(first_year, last_year, n_year):
       print(year)
       
       # Select data for the year
       surveys_year = surveys_df[surveys_df.year == year].dropna()
   ```
3. 
   ```python
   for species in surveys_df['species_id'].dropna().unique():
       surveys_species = surveys_df[surveys_df.species_id == species]
       filename = 'episodes/data/species_files/surveys' + species + '.csv'
       surveys_species.to_csv(filename)
    ```

::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

