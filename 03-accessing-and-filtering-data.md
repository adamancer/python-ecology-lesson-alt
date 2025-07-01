---
title: Accessing and Filtering Data
teaching: 60
exercises: 0
---

::: questions ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   How can we look at individual rows and columns in a dataframe?
-   How can we perform calculations?
-   How can we modify the table and data?

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: objectives :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   Access individual rows and columns
-   Access multiple columns at once using a list
-   Perform calculations like addition and subtraction
-   Rename columns using a dictionary
-   Access rows containing specific data
-   Sort the data returned by a query
-   Modify data using loc

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

We'll begin by importing pandas and reading our CSV, as we did in the
previous lesson:

```python
import pandas as pd

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

We will now look at how to access rows and columns in the dataframe.

## Getting columns

We can get the values from a single column in the dataframe by passing a
string inside square brackets to the dataframe object. For example, to
look at the year column, use:

```python
surveys["year"]
```

```{.output}
0        1977
1        1977
2        1977
3        1977
4        1977
         ... 
35544    2002
35545    2002
35546    2002
35547    2002
35548    2002
Name: year, Length: 35549, dtype: int64
```

A single column is returned as a `Series`, which is why the output for
this cell is formatted differently than the other cells in this lesson.
The main difference between a `Series` and a `DataFrame` is that a
`DataFrame` can have multiple columns. The two classes share many but
not all attributes and methods. Note also that this is a copy of data
from the original dataframe. Changing values in the series will have no
effect on the original dataframe.

### Using lists to get more than one column at a time

Python uses the built-in `list` data type to store sequences, that is,
an ordered list of objects. Any type of Python object can be stored in a
list: strings, integers, floats, even other lists or collections. Once
created, a list can be modified by appending, inserting, or deleting
items. We will not be going into detail about these operations here, but
as always you can learn more about how to use a list using `help()` or
[the Python docs](https://docs.python.org/3/library/stdtypes.html#list).

Create a list using square brackets. Let's create a list of the three
columns in our dataframe that together give the date of an observation:

```python
cols = ["year", "month", "day"]
```

When we pass this list to the survey dataframe using square brackets, as
we did above, we get a copy of the dataframe containing just those
columns. Note that, because we asked for more than one column, pandas
returns a dataframe:

```python
surveys[cols]
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
      <th>year</th>
      <th>month</th>
      <th>day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1977</td>
      <td>7</td>
      <td>16</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1977</td>
      <td>7</td>
      <td>16</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1977</td>
      <td>7</td>
      <td>16</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1977</td>
      <td>7</td>
      <td>16</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1977</td>
      <td>7</td>
      <td>16</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>35544</th>
      <td>2002</td>
      <td>12</td>
      <td>31</td>
    </tr>
    <tr>
      <th>35545</th>
      <td>2002</td>
      <td>12</td>
      <td>31</td>
    </tr>
    <tr>
      <th>35546</th>
      <td>2002</td>
      <td>12</td>
      <td>31</td>
    </tr>
    <tr>
      <th>35547</th>
      <td>2002</td>
      <td>12</td>
      <td>31</td>
    </tr>
    <tr>
      <th>35548</th>
      <td>2002</td>
      <td>12</td>
      <td>31</td>
    </tr>
  </tbody>
</table>
<p>35549 rows × 3 columns</p>

## Getting rows

We can get the rows at the beginning of the table using the head method:

```python
surveys.head()
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
  </tbody>
</table>

By default, this methods returns the first five rows. We can provide a
number inside the parentheses if we need a specific number of rows:

```python
surveys.head(10)
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
      <th>5</th>
      <td>6</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>1</td>
      <td>PF</td>
      <td>M</td>
      <td>14.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>2</td>
      <td>PE</td>
      <td>F</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>1</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>1</td>
      <td>DM</td>
      <td>F</td>
      <td>34.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>6</td>
      <td>PF</td>
      <td>F</td>
      <td>20.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>

The `tail()` method is similar, except it returns rows from the end of
the table:

```python
surveys.tail()
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

Or we can use `sample()` to return a random row from anywhere in the
dataframe:

```python
surveys.sample()
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
      <th>13485</th>
      <td>13486</td>
      <td>10</td>
      <td>24</td>
      <td>1987</td>
      <td>20</td>
      <td>DM</td>
      <td>F</td>
      <td>36.0</td>
      <td>36.0</td>
    </tr>
  </tbody>
</table>

The `head()`, `tail()`, and `sample()` methods are useful for getting a
feel for how our data is structured, but we may also want to look at
specific rows. As when we selected columns above, we can use square
brackets to extract *slices* from the dataframe. A slice is a subset of
the dataframe starting at one row and ending at another. To get a slice,
we pass the starting and ending indexes to the square brackets as
`start:end`:

```python
surveys[2:5]
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
  </tbody>
</table>

There are three things to be aware of when slicing a dataframe:

-   Row indexes are *zero-based*. The first row has an index of 0, not
    1.
-   When slicing, the slice includes start but not the end index. In
    this case, that means the slice includes rows 2, 3, and 4 but not 5.
-   The row label can be different from the row index. They happen to be
    the same here, but don't count on that being true.

Core Python types like `list` and `tuple` use the same conventions, as
do most Python libraries that deal with sequences.

## Getting unique values

Recall that we can use square brackets to return a single column from a
dataframe. We can get the list of unique values within that column using
the `unique()` method:

```python
surveys["species_id"].unique()
```

```{.output}
array(['NL', 'DM', 'PF', 'PE', 'DS', 'PP', 'SH', 'OT', 'DO', 'OX', 'SS',
       'OL', 'RM', nan, 'SA', 'PM', 'AH', 'DX', 'AB', 'CB', 'CM', 'CQ',
       'RF', 'PC', 'PG', 'PH', 'PU', 'CV', 'UR', 'UP', 'ZL', 'UL', 'CS',
       'SC', 'BA', 'SF', 'RO', 'AS', 'SO', 'PI', 'ST', 'CU', 'SU', 'RX',
       'PB', 'PL', 'PX', 'CT', 'US'], dtype=object)
```

To do the same across multiple columns, we can use the
`drop_duplicates()` method on a copy of the dataframe containing only
the columns we're interested in. Like any well-named method,
`drop_duplicates()` does exactly what the name implies: It returns a
copy of the dataframe with all duplicate rows removed.

```python
surveys[["plot_id", "species_id"]].drop_duplicates()
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
      <th>plot_id</th>
      <th>species_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>NL</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>NL</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>DM</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>DM</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>DM</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>35474</th>
      <td>22</td>
      <td>SF</td>
    </tr>
    <tr>
      <th>35511</th>
      <td>11</td>
      <td>US</td>
    </tr>
    <tr>
      <th>35519</th>
      <td>9</td>
      <td>SF</td>
    </tr>
    <tr>
      <th>35527</th>
      <td>13</td>
      <td>US</td>
    </tr>
    <tr>
      <th>35543</th>
      <td>15</td>
      <td>US</td>
    </tr>
  </tbody>
</table>
<p>612 rows × 2 columns</p>

## Filtering data

It is often more useful to take subsets from the dataframe based on
data. pandas provides a variety of ways to filter a dataframe. For
example, suppose we want to look at a specific species in the surveys
dataframe. We can view the rows matching a given species using the same
square brackets we used above to select specific columns and rows. Here,
however, instead of using a value or list of values, we will use a
*conditional expression*.

A conditional expression is a statement that evaluates as either True or
False. They often make use of inequality operators, for example:

-   `==` for equals
-   `!=` for does not equal
-   `>` for greater than
-   `>=` for greater than or equal to
-   `<` for less than
-   `<=` for less than or equal to

Examples of conditional statements include:

-   `"a" == "b"` evaluates False
-   `"a" != b"` evaluates True
-   `3 > 4` evaluates False

Note that, when comparing strings, evaluations are case sensitive:

-   `"a" == "A"` evaluates False

::: callout ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### = for assignment, == for equality

Remember that, in Python, a single equal sign is used to assign values
to variables. We've already used the assignment operator in this lesson,
for example, when we created a new column in the dataframe.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

To limit the dataframe to rows matching the species "DM", include the
conditional `surveys["species_id"] == "DM"` inside the square brackets:

```python
surveys[surveys["species_id"] == "DM"]
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
      <th>7</th>
      <td>8</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>1</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>1</td>
      <td>DM</td>
      <td>F</td>
      <td>34.0</td>
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
      <th>35532</th>
      <td>35533</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>14</td>
      <td>DM</td>
      <td>F</td>
      <td>36.0</td>
      <td>48.0</td>
    </tr>
    <tr>
      <th>35533</th>
      <td>35534</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>14</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>56.0</td>
    </tr>
    <tr>
      <th>35534</th>
      <td>35535</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>14</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>53.0</td>
    </tr>
    <tr>
      <th>35535</th>
      <td>35536</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>14</td>
      <td>DM</td>
      <td>F</td>
      <td>35.0</td>
      <td>42.0</td>
    </tr>
    <tr>
      <th>35536</th>
      <td>35537</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>14</td>
      <td>DM</td>
      <td>F</td>
      <td>36.0</td>
      <td>46.0</td>
    </tr>
  </tbody>
</table>
<p>10596 rows × 9 columns</p>

To limit our results to observations made in or after 2000, use:

```python
surveys[surveys["year"] >= 2000]
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
      <th>30158</th>
      <td>30159</td>
      <td>1</td>
      <td>8</td>
      <td>2000</td>
      <td>1</td>
      <td>PP</td>
      <td>F</td>
      <td>22.0</td>
      <td>17.0</td>
    </tr>
    <tr>
      <th>30159</th>
      <td>30160</td>
      <td>1</td>
      <td>8</td>
      <td>2000</td>
      <td>1</td>
      <td>DO</td>
      <td>M</td>
      <td>35.0</td>
      <td>53.0</td>
    </tr>
    <tr>
      <th>30160</th>
      <td>30161</td>
      <td>1</td>
      <td>8</td>
      <td>2000</td>
      <td>1</td>
      <td>PP</td>
      <td>F</td>
      <td>21.0</td>
      <td>17.0</td>
    </tr>
    <tr>
      <th>30161</th>
      <td>30162</td>
      <td>1</td>
      <td>8</td>
      <td>2000</td>
      <td>1</td>
      <td>DM</td>
      <td>M</td>
      <td>36.0</td>
      <td>50.0</td>
    </tr>
    <tr>
      <th>30162</th>
      <td>30163</td>
      <td>1</td>
      <td>8</td>
      <td>2000</td>
      <td>1</td>
      <td>PP</td>
      <td>M</td>
      <td>20.0</td>
      <td>16.0</td>
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
<p>5391 rows × 9 columns</p>

Each filtering operation returns a copy of the dataframe. We will look
at how to make changes to the original dataframe at the end of this
lesson.

## Complex filters

We can combine conditionals using *bitwise operators*. These work like
the terms AND and OR in many search interfaces.

-   `&`: True if conditions on both sides of the operator are True (and)
-   `|`: True if a condition on either side is True (or)

To return all observations of DM in or after 2000, we can combine the
two conditionals we used previously. Note that, when joining
conditionals using `&` or `|`, we must wrap each individual condition in
parentheses. If we omit the parentheses, pandas will not perform the
comparisons in the expected order.

```python
surveys[(surveys["species_id"] == "DM") & (surveys["year"] >= 2000)]
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
      <th>30161</th>
      <td>30162</td>
      <td>1</td>
      <td>8</td>
      <td>2000</td>
      <td>1</td>
      <td>DM</td>
      <td>M</td>
      <td>36.0</td>
      <td>50.0</td>
    </tr>
    <tr>
      <th>30178</th>
      <td>30179</td>
      <td>1</td>
      <td>8</td>
      <td>2000</td>
      <td>12</td>
      <td>DM</td>
      <td>M</td>
      <td>36.0</td>
      <td>60.0</td>
    </tr>
    <tr>
      <th>30195</th>
      <td>30196</td>
      <td>1</td>
      <td>8</td>
      <td>2000</td>
      <td>17</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>52.0</td>
    </tr>
    <tr>
      <th>30196</th>
      <td>30197</td>
      <td>1</td>
      <td>8</td>
      <td>2000</td>
      <td>17</td>
      <td>DM</td>
      <td>F</td>
      <td>34.0</td>
      <td>43.0</td>
    </tr>
    <tr>
      <th>30209</th>
      <td>30210</td>
      <td>1</td>
      <td>8</td>
      <td>2000</td>
      <td>22</td>
      <td>DM</td>
      <td>M</td>
      <td>38.0</td>
      <td>56.0</td>
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
      <th>35532</th>
      <td>35533</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>14</td>
      <td>DM</td>
      <td>F</td>
      <td>36.0</td>
      <td>48.0</td>
    </tr>
    <tr>
      <th>35533</th>
      <td>35534</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>14</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>56.0</td>
    </tr>
    <tr>
      <th>35534</th>
      <td>35535</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>14</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>53.0</td>
    </tr>
    <tr>
      <th>35535</th>
      <td>35536</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>14</td>
      <td>DM</td>
      <td>F</td>
      <td>35.0</td>
      <td>42.0</td>
    </tr>
    <tr>
      <th>35536</th>
      <td>35537</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>14</td>
      <td>DM</td>
      <td>F</td>
      <td>36.0</td>
      <td>46.0</td>
    </tr>
  </tbody>
</table>
<p>847 rows × 9 columns</p>

We can also use methods to filter the dataframe. For example, `isin()`
is used to match a list of values. Methods can be combined with other
conditionals as above. The example below returns rows from 2000 or later
with either "DM", "DO", or "DS" in the species_id column:

```python
surveys[
    surveys["species_id"].isin(["DM", "DO", "DS"]) & (surveys["year"] >= 2000)
]
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
      <th>30159</th>
      <td>30160</td>
      <td>1</td>
      <td>8</td>
      <td>2000</td>
      <td>1</td>
      <td>DO</td>
      <td>M</td>
      <td>35.0</td>
      <td>53.0</td>
    </tr>
    <tr>
      <th>30161</th>
      <td>30162</td>
      <td>1</td>
      <td>8</td>
      <td>2000</td>
      <td>1</td>
      <td>DM</td>
      <td>M</td>
      <td>36.0</td>
      <td>50.0</td>
    </tr>
    <tr>
      <th>30166</th>
      <td>30167</td>
      <td>1</td>
      <td>8</td>
      <td>2000</td>
      <td>1</td>
      <td>DO</td>
      <td>M</td>
      <td>35.0</td>
      <td>41.0</td>
    </tr>
    <tr>
      <th>30170</th>
      <td>30171</td>
      <td>1</td>
      <td>8</td>
      <td>2000</td>
      <td>2</td>
      <td>DO</td>
      <td>M</td>
      <td>36.0</td>
      <td>52.0</td>
    </tr>
    <tr>
      <th>30172</th>
      <td>30173</td>
      <td>1</td>
      <td>8</td>
      <td>2000</td>
      <td>2</td>
      <td>DO</td>
      <td>F</td>
      <td>35.0</td>
      <td>54.0</td>
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
      <th>35533</th>
      <td>35534</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>14</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>56.0</td>
    </tr>
    <tr>
      <th>35534</th>
      <td>35535</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>14</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>53.0</td>
    </tr>
    <tr>
      <th>35535</th>
      <td>35536</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>14</td>
      <td>DM</td>
      <td>F</td>
      <td>35.0</td>
      <td>42.0</td>
    </tr>
    <tr>
      <th>35536</th>
      <td>35537</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>14</td>
      <td>DM</td>
      <td>F</td>
      <td>36.0</td>
      <td>46.0</td>
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
  </tbody>
</table>
<p>1268 rows × 9 columns</p>

## Sorting data

We can sort a dataframe using the `sort_values()` method. For this
example, we'll work from the subset defined above. First we need to
assign that subset to a variable:

```python
results = surveys[
    surveys["species_id"].isin(["DM", "DO", "DS"]) & (surveys["year"] >= 2000)
]
```

Now we'll sort the results by weight_g. To do so, pass that column name
as an argument (that is, inside the trailing parentheses) to the
`sort_values()` method:

```python
results.sort_values("weight")
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
      <th>30614</th>
      <td>30615</td>
      <td>4</td>
      <td>30</td>
      <td>2000</td>
      <td>12</td>
      <td>DM</td>
      <td>M</td>
      <td>34.0</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>34790</th>
      <td>34791</td>
      <td>10</td>
      <td>5</td>
      <td>2002</td>
      <td>17</td>
      <td>DM</td>
      <td>M</td>
      <td>34.0</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>32650</th>
      <td>32651</td>
      <td>9</td>
      <td>22</td>
      <td>2001</td>
      <td>17</td>
      <td>DM</td>
      <td>F</td>
      <td>33.0</td>
      <td>21.0</td>
    </tr>
    <tr>
      <th>32782</th>
      <td>32783</td>
      <td>9</td>
      <td>23</td>
      <td>2001</td>
      <td>14</td>
      <td>DM</td>
      <td>M</td>
      <td>34.0</td>
      <td>21.0</td>
    </tr>
    <tr>
      <th>32968</th>
      <td>32969</td>
      <td>10</td>
      <td>14</td>
      <td>2001</td>
      <td>9</td>
      <td>DM</td>
      <td>M</td>
      <td>32.0</td>
      <td>22.0</td>
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
      <th>34724</th>
      <td>34725</td>
      <td>9</td>
      <td>10</td>
      <td>2002</td>
      <td>9</td>
      <td>DM</td>
      <td>M</td>
      <td>38.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>34950</th>
      <td>34951</td>
      <td>10</td>
      <td>6</td>
      <td>2002</td>
      <td>14</td>
      <td>DM</td>
      <td>F</td>
      <td>36.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35088</th>
      <td>35089</td>
      <td>11</td>
      <td>10</td>
      <td>2002</td>
      <td>11</td>
      <td>DM</td>
      <td>F</td>
      <td>35.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35387</th>
      <td>35388</td>
      <td>12</td>
      <td>29</td>
      <td>2002</td>
      <td>1</td>
      <td>DO</td>
      <td>M</td>
      <td>35.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35485</th>
      <td>35486</td>
      <td>12</td>
      <td>29</td>
      <td>2002</td>
      <td>16</td>
      <td>DO</td>
      <td>M</td>
      <td>37.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>1268 rows × 9 columns</p>

By default, rows are sorted in ascending order (smallest to largest). We
can modify this behavior using the *ascending* keyword argument:

```python
results.sort_values("weight", ascending=False)
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
      <th>31955</th>
      <td>31956</td>
      <td>4</td>
      <td>21</td>
      <td>2001</td>
      <td>24</td>
      <td>DO</td>
      <td>F</td>
      <td>36.0</td>
      <td>76.0</td>
    </tr>
    <tr>
      <th>32041</th>
      <td>32042</td>
      <td>5</td>
      <td>26</td>
      <td>2001</td>
      <td>1</td>
      <td>DO</td>
      <td>F</td>
      <td>37.0</td>
      <td>68.0</td>
    </tr>
    <tr>
      <th>31942</th>
      <td>31943</td>
      <td>4</td>
      <td>21</td>
      <td>2001</td>
      <td>1</td>
      <td>DO</td>
      <td>F</td>
      <td>37.0</td>
      <td>68.0</td>
    </tr>
    <tr>
      <th>30441</th>
      <td>30442</td>
      <td>3</td>
      <td>4</td>
      <td>2000</td>
      <td>2</td>
      <td>DO</td>
      <td>F</td>
      <td>NaN</td>
      <td>66.0</td>
    </tr>
    <tr>
      <th>30289</th>
      <td>30290</td>
      <td>2</td>
      <td>5</td>
      <td>2000</td>
      <td>1</td>
      <td>DO</td>
      <td>F</td>
      <td>36.0</td>
      <td>65.0</td>
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
      <th>34724</th>
      <td>34725</td>
      <td>9</td>
      <td>10</td>
      <td>2002</td>
      <td>9</td>
      <td>DM</td>
      <td>M</td>
      <td>38.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>34950</th>
      <td>34951</td>
      <td>10</td>
      <td>6</td>
      <td>2002</td>
      <td>14</td>
      <td>DM</td>
      <td>F</td>
      <td>36.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35088</th>
      <td>35089</td>
      <td>11</td>
      <td>10</td>
      <td>2002</td>
      <td>11</td>
      <td>DM</td>
      <td>F</td>
      <td>35.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35387</th>
      <td>35388</td>
      <td>12</td>
      <td>29</td>
      <td>2002</td>
      <td>1</td>
      <td>DO</td>
      <td>M</td>
      <td>35.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35485</th>
      <td>35486</td>
      <td>12</td>
      <td>29</td>
      <td>2002</td>
      <td>16</td>
      <td>DO</td>
      <td>M</td>
      <td>37.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>1268 rows × 9 columns</p>

We can sort on multiple fields at once by passing a list of column
names. We can control how each column sorts by passing a list with the
same number of values (that is, one value per column) to the ascending
keyword. The cell below sorts the results first by species_id (largest
to smallest), then by weight (smallest to largest):

```python
results.sort_values(["species_id", "weight"], ascending=[False, True])
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
      <th>30687</th>
      <td>30688</td>
      <td>5</td>
      <td>1</td>
      <td>2000</td>
      <td>8</td>
      <td>DO</td>
      <td>M</td>
      <td>35.0</td>
      <td>23.0</td>
    </tr>
    <tr>
      <th>30768</th>
      <td>30769</td>
      <td>6</td>
      <td>3</td>
      <td>2000</td>
      <td>17</td>
      <td>DO</td>
      <td>M</td>
      <td>35.0</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>33339</th>
      <td>33340</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>12</td>
      <td>DO</td>
      <td>M</td>
      <td>34.0</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>34082</th>
      <td>34083</td>
      <td>5</td>
      <td>16</td>
      <td>2002</td>
      <td>6</td>
      <td>DO</td>
      <td>F</td>
      <td>33.0</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>34096</th>
      <td>34097</td>
      <td>5</td>
      <td>16</td>
      <td>2002</td>
      <td>6</td>
      <td>DO</td>
      <td>M</td>
      <td>35.0</td>
      <td>24.0</td>
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
      <th>34698</th>
      <td>34699</td>
      <td>9</td>
      <td>10</td>
      <td>2002</td>
      <td>15</td>
      <td>DM</td>
      <td>F</td>
      <td>38.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>34707</th>
      <td>34708</td>
      <td>9</td>
      <td>10</td>
      <td>2002</td>
      <td>14</td>
      <td>DM</td>
      <td>M</td>
      <td>35.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>34724</th>
      <td>34725</td>
      <td>9</td>
      <td>10</td>
      <td>2002</td>
      <td>9</td>
      <td>DM</td>
      <td>M</td>
      <td>38.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>34950</th>
      <td>34951</td>
      <td>10</td>
      <td>6</td>
      <td>2002</td>
      <td>14</td>
      <td>DM</td>
      <td>F</td>
      <td>36.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35088</th>
      <td>35089</td>
      <td>11</td>
      <td>10</td>
      <td>2002</td>
      <td>11</td>
      <td>DM</td>
      <td>F</td>
      <td>35.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>1268 rows × 9 columns</p>

As with the dataframe methods above, `sort_values()` returns a copy of
the original dataframe and leaves the original untouched.

::: challenge ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Write a query that returns year, species_id, and weight in kg from the
surveys table, sorted with the largest weights at the top.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

```python
# Create a subset containing only year, species_id, and weight
subset = surveys[["year", "species_id", "weight"]]

# Sort the subset by weight
subset.sort_values("weight", ascending=False)
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
      <th>year</th>
      <th>species_id</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>33048</th>
      <td>2001</td>
      <td>NL</td>
      <td>280.0</td>
    </tr>
    <tr>
      <th>12870</th>
      <td>1987</td>
      <td>NL</td>
      <td>278.0</td>
    </tr>
    <tr>
      <th>15458</th>
      <td>1989</td>
      <td>NL</td>
      <td>275.0</td>
    </tr>
    <tr>
      <th>2132</th>
      <td>1979</td>
      <td>NL</td>
      <td>274.0</td>
    </tr>
    <tr>
      <th>12728</th>
      <td>1987</td>
      <td>NL</td>
      <td>270.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>35530</th>
      <td>2002</td>
      <td>PB</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35543</th>
      <td>2002</td>
      <td>US</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35544</th>
      <td>2002</td>
      <td>AH</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35545</th>
      <td>2002</td>
      <td>AH</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35548</th>
      <td>2002</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>35549 rows × 3 columns</p>

## Making a scatter plot

We will discuss data visualization in depth in lesson 7 but will
introduce some fundamental concepts. For this lesson, we will use the
`plotly` library, which creates interactive, highly customizable plots
using our dataframe.

```python
import plotly.express as px

fig = px.scatter(surveys, x="weight", y="hindfoot_length")
fig.show()
```

```{.output}
```

<embed src="files/fig-25028926113cc479b199dab433a782b0.html" width=760 height=570>

::: keypoints ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   Use square brackets to access rows, columns, and specific cells
-   Use operators like `+`, `-`, and `/` to perform arithmetic on rows
    and columns
-   Store the results of calculations in a dataframe by adding a new
    column or overwriting an existing column
-   Sort data, rename columns, and get unique values in a dataframe
    using methods provided by pandas
-   By default, most dataframe operations return a copy of the original
    data

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
