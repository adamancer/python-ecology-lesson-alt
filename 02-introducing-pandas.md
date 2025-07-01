---
title: Introducing pandas
teaching: 60
exercises: 0
---

::: questions ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   What data will we be working with in this lesson?
-   What is pandas?
-   Why use pandas for data analysis?
-   How do we read and write data using pandas?

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: objectives :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   Learn about the dataset we'll be working with
-   Look at the benefits of using pandas to analyze data
-   Import data from a CSV into a pandas dataframe
-   Learn how pandas handles different types of data
-   Write a dataframe to a CSV

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## Dataset description

*The dataset description was taken from [Data Management with SQL for
Ecologists](https://datacarpentry.org/sql-ecology-lesson/) (CC-BY-4.0)*

The data we will be using is a time-series for a small mammal community
in southern Arizona. This is part of a project studying the effects of
rodents and ants on the plant community that has been running for almost
40 years. The rodents are sampled on a series of 24 plots, with
different experimental manipulations controlling which rodents are
allowed to access which plots.

This is a real dataset that has been used in over 100 publications.
We've simplified it for the workshop, but you can download the full
dataset and work with it using exactly the same tools we'll learn about
today.

## Answering questions using data

Let's look at some of the cleaned spreadsheets we downloaded during
Setup to complete this challenge. Over the course of this lesson, we'll
be working with the following three files:

-   surveys.csv
-   species.csv
-   plots.csv

::: challenge ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Open each of these csv files and explore them. What information is
contained in each file? Specifically, if we had the following research
questions:

-   How has the hindfoot length and weight of Dipodomys species changed
    over time?
-   What is the average weight of each species, per year?
-   What information can I learn about Dipodomys species in the 2000s,
    over time?

What would we need to answer these questions? Which files have the data
we need? What operations would we need to perform if we were doing these
analyses by hand?

**Hint:** We can view CSV files using JupyterLab using the left sidebar.
Click on the Folder icon in the top left of the sidebar to see the
files, then go to the data directory to see the CSV we've downloaded for
this lesson.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

In order to answer the questions described above, we'll need to do the
following basic data operations:

-   select subsets of the data (rows and columns)
-   group subsets of data
-   do math and other calculations
-   combine data across spreadsheets

In addition, we don't want to do this manually! Instead of searching for
the right pieces of data ourselves, or clicking between spreadsheets, or
manually sorting columns, we want to make the computer do the work.

In particular, we want to use a tool where it's easy to repeat our
analysis in case our data changes. We also want to do all this searching
without actually modifying our source data.

## Why use pandas?

The Python Data Analysis Library, or pandas, is a Python library used to
work with dataframes. A dataframe is a representation of tabular data
very similar to a spreadsheet, consisting of rows (representing records)
and columns (representing fields or variables). Tables are a very common
format for representing scientific data and should be very familiar to
anyone taking this course.

pandas offers the same advantages as any well-written library: It
creates a common codebase for working on a single task, in this case,
analyzing data. Some benefits of this approach include:

-   **Reliability:** Provides flexible, well-tested methods for reading,
    querying, aggregating, grouping, and plotting data
-   **Repeatability:** Repeat the same analyses when data is added or
    changed
-   **Speed:** Faster in many cases than coding our own functions in
    Python
-   **Reproducibility:** Document and share code in narrative form using
    tools like Jupyter notebooks
-   **Community:** Access a large, active community for help when we run
    into problems

## Importing data using pandas

Unlike the libraries in the Python Standard Library discussed in the
previous lesson, pandas is not part of the typical Python installation.
Once it has been installed, however, it can be accessed using the same
`import` command used to import the built-in libraries. By convention,
pandas is imported using the alias "pd". We can assign the alias using
the `as` keyword:

```python
import pandas as pd
```

::: callout ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### Using aliases

Why use an alias? We will refer to pandas many, many times when writing
a script, so it's useful to abbreviate the name and save some
keystrokes. But it's also a matter of consistency with the larger
community. Many of the core scientific Python libraries, including
pandas, recommend a specific alias, so most code shared online will use
those aliases as well.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Now that pandas has been imported, we can access the function we need to
load data from a CSV, `pd.read_csv()`. The function call has three
parts:

-   The name (or in this case, alias) of the object that defines the
    function. This can be a library or any other object. It can also be
    omitted in some cases (for example, when using a function built into
    Python).
-   The name of the method we'd like to use
-   A set of parentheses that tells the function to run.

Many functions include *parameters* that allow the user to modify the
behavior of the function. Parameters may be positional or named. In
Python, data passed to positional parameters are called *arguments*
(often abbreviated as args), and data passed to named parameters are
called *keyword arguments* (often abbreviated as kwargs). In either
case, the arguments are included inside the parentheses used to call the
function.

Below, we will pass a single argument to `pd.read_csv()`: A string that
tells the function where to find the surveys.csv file.

```python
pd.read_csv("data/surveys.csv")
```

```{.output}
```

<style>
  table.dataframe tbody tr:hover { background-color: #ccffff !important; }
  table.dataframe tr:nth-child(even) { background-color: #f5f5f5; }
  table.dataframe th { text-align: right; font-weight: bold; }
  table.dataframe td { text-align: right; }
</style>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>record_id</th>
      <th>month</th>
      <th>day</th>
      <th>year</th>
      <th>plot_id</th>
      <th>species_id</th>
      <th>sex</th>
      <th>hindfoot_length</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>2</td>
      <td>NL</td>
      <td>M</td>
      <td>32.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>3</td>
      <td>NL</td>
      <td>M</td>
      <td>33.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>2</td>
      <td>DM</td>
      <td>F</td>
      <td>37.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>7</td>
      <td>DM</td>
      <td>M</td>
      <td>36.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>3</td>
      <td>DM</td>
      <td>M</td>
      <td>35.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>35544</th>
      <td>35545</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>AH</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35545</th>
      <td>35546</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>AH</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35546</th>
      <td>35547</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>10</td>
      <td>RM</td>
      <td>F</td>
      <td>15.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>35547</th>
      <td>35548</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>7</td>
      <td>DO</td>
      <td>M</td>
      <td>36.0</td>
      <td>51.0</td>
    </tr>
    <tr>
      <th>35548</th>
      <td>35549</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>35549 rows × 9 columns</p>

Here are a few things to observe about how the dataframe is structured:

-   By default, JupyterLab displays the first and last five rows of the
    dataframe
-   Each row represents a record
-   Each column represents a field
-   The unlabeled column on the far left is called the *row label*
-   pandas has done a lot of work behind the scenes when reading the
    data, including:
    -   Assigning the *row index* as the row label
    -   Assigning each column a data type based on its contents
    -   Assigning certain cells the value NaN, which stands for "not a
        number" and is used to designate null values in the dataset.
        Here, those cells represent blank cells in the spreadsheet.

Much of this behavior can be controlled when the spreadsheet is first
read by using keyword arguments. For example, to force `pd.read_csv()`
to use the existing record_id column as the row label, use the
*index_col* keyword argument:

```python
pd.read_csv("data/surveys.csv", index_col="record_id")
```

```{.output}
```

<style>
  table.dataframe tbody tr:hover { background-color: #ccffff !important; }
  table.dataframe tr:nth-child(even) { background-color: #f5f5f5; }
  table.dataframe th { text-align: right; font-weight: bold; }
  table.dataframe td { text-align: right; }
</style>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>month</th>
      <th>day</th>
      <th>year</th>
      <th>plot_id</th>
      <th>species_id</th>
      <th>sex</th>
      <th>hindfoot_length</th>
      <th>weight</th>
    </tr>
    <tr>
      <th>record_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>2</td>
      <td>NL</td>
      <td>M</td>
      <td>32.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>3</td>
      <td>NL</td>
      <td>M</td>
      <td>33.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>2</td>
      <td>DM</td>
      <td>F</td>
      <td>37.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>7</td>
      <td>DM</td>
      <td>M</td>
      <td>36.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>3</td>
      <td>DM</td>
      <td>M</td>
      <td>35.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>35545</th>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>AH</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35546</th>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>AH</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35547</th>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>10</td>
      <td>RM</td>
      <td>F</td>
      <td>15.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>35548</th>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>7</td>
      <td>DO</td>
      <td>M</td>
      <td>36.0</td>
      <td>51.0</td>
    </tr>
    <tr>
      <th>35549</th>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>35549 rows × 8 columns</p>

Now record_id appears on the far left, indicating that pandas is using
that column as the row label.

::: challenge ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Run `help()` on the `pd.read_csv()` method (note that you should omit
the trailing parentheses). Alternatively, take a look at the [much
prettier
documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
provided by the pandas developers. Based on that information, answer the
following questions:

1.  What parameter would you use to control how null values are
    interpreted?
2.  What values are interpreted as NaN by default?

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### Show me the solution to challenge 1

na_values

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### Show me the solution to challenge 2

In addition to empty cells, the following values are interpreted as NaN,
or null, by pandas. These strings may look familiar from programs like
Excel.

-   #N/A
-   #N/A N/A
-   #NA
-   -1.#IND
-   -1.#QNAN
-   -NaN
-   -nan
-   1.#IND
-   1.#QNAN
-   \<NA\>
-   N/A
-   NA
-   NULL
-   NaN
-   n/a
-   nan
-   null

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## Assigning to variables

We can assign the dataframe to a variable to make it easier to access.
As we saw in the previous lesson, we use a single equals sign to assign
an object to a variable. The variable name should be short and
descriptive. By convention, variable names in Python use snake_case
(that is, lower case with individual words separated by underscores).

```python
surveys = pd.read_csv("data/surveys.csv")
surveys
```

```{.output}
```

<style>
  table.dataframe tbody tr:hover { background-color: #ccffff !important; }
  table.dataframe tr:nth-child(even) { background-color: #f5f5f5; }
  table.dataframe th { text-align: right; font-weight: bold; }
  table.dataframe td { text-align: right; }
</style>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>record_id</th>
      <th>month</th>
      <th>day</th>
      <th>year</th>
      <th>plot_id</th>
      <th>species_id</th>
      <th>sex</th>
      <th>hindfoot_length</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>2</td>
      <td>NL</td>
      <td>M</td>
      <td>32.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>3</td>
      <td>NL</td>
      <td>M</td>
      <td>33.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>2</td>
      <td>DM</td>
      <td>F</td>
      <td>37.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>7</td>
      <td>DM</td>
      <td>M</td>
      <td>36.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>3</td>
      <td>DM</td>
      <td>M</td>
      <td>35.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>35544</th>
      <td>35545</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>AH</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35545</th>
      <td>35546</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>AH</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35546</th>
      <td>35547</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>10</td>
      <td>RM</td>
      <td>F</td>
      <td>15.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>35547</th>
      <td>35548</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>7</td>
      <td>DO</td>
      <td>M</td>
      <td>36.0</td>
      <td>51.0</td>
    </tr>
    <tr>
      <th>35548</th>
      <td>35549</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>35549 rows × 9 columns</p>

## Understanding data types in pandas

We can use the `info()` method to see how pandas interpreted each column
in the dataset. This method gives use the name, count, and data type of
each column and provides some information about the dataset as a whole
(for example, memory usage, which is helpful to know when working with
large datasets):

```python
surveys.info()
```

```{.output}
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 35549 entries, 0 to 35548
Data columns (total 9 columns):
 #   Column           Non-Null Count  Dtype  
---  ------           --------------  -----  
 0   record_id        35549 non-null  int64  
 1   month            35549 non-null  int64  
 2   day              35549 non-null  int64  
 3   year             35549 non-null  int64  
 4   plot_id          35549 non-null  int64  
 5   species_id       34786 non-null  object 
 6   sex              33038 non-null  object 
 7   hindfoot_length  31438 non-null  float64
 8   weight           32283 non-null  float64
dtypes: float64(2), int64(5), object(2)
memory usage: 2.4+ MB

```

Note that the data types used by pandas look a little different than the
ones used by Python itself. See the table below for the rough
equivalents.

### Data types in pandas

  Data Type    Description                   Similar To
  ------------ ----------------------------- -------------------
  object       Character string or mixed     str
  int64        Integer numerical             int
  float64      Approximate numerical         float
  bool         Stores True or False values   bool
  datetime64   Stores date and time values   datetime.datetime

## Saving a dataframe

When analyzing a dataset, we'll often want to save our work to a file.
The `to_csv()` method can be used to write a dataframe to a CSV. As when
we read a CSV from a file above, we need to provide a path to which to
save the file. The example below also includes the *index* keyword
argument. Setting that parameter to False tells pandas not to include
the row label when writing the CSV.

```python
surveys.to_csv("data/surveys_mod.csv", index=False)
```

This is far from the only option for writing data--pandas supports a
variety of file types for both reading and writing. Try searching for
"read\_" in the [pandas API
reference](https://pandas.pydata.org/docs/reference/index.html) to see
the supported formats.

::: keypoints ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   This lesson uses real data from a decades-long survey of rodents in
    Arizona
-   pandas is a data analysis library that allows users to read,
    manipulate, and view tabular data using Python
-   pandas represents data as a dataframe consisting of rows (records)
    and columns (fields or variables)
-   Read a dataframe from CSV using the `pd.read_csv()` function
-   Write a dataframe to CSV using the `to_csv()` method
-   The behavior of a function can be modified by including arguments
    and keyword arguments when the function is called
-   pandas uses its own classes to represent text, numbers, booleans,
    and datetimes

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
