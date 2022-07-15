---
title: Accessing Data in a Dataframe
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

We can get the values from a single column by passing a string inside
square brackets to the dataframe object. For example, to look at the
year column, use:

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
we did above, we retrieve a copy of the dataframe containing just those
columns. Note that, when we get more than one column, pandas returns a
dataframe:

```python
surveys[cols]
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
surveys.head(20)
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
    <tr>
      <th>10</th>
      <td>11</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>5</td>
      <td>DS</td>
      <td>F</td>
      <td>53.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>7</td>
      <td>DM</td>
      <td>M</td>
      <td>38.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
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
      <th>13</th>
      <td>14</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>8</td>
      <td>DM</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>6</td>
      <td>DM</td>
      <td>F</td>
      <td>36.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>4</td>
      <td>DM</td>
      <td>F</td>
      <td>36.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>3</td>
      <td>DS</td>
      <td>F</td>
      <td>48.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>2</td>
      <td>PP</td>
      <td>M</td>
      <td>22.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>4</td>
      <td>PF</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>11</td>
      <td>DS</td>
      <td>F</td>
      <td>48.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>

The `tail()` method is similar, except it returns rows from the end of
the table:

```python
surveys.tail()
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

The `head()` and `tail()` methods are useful for getting a feel for how
our data is structured, but we'll also want to be able to look at
specific rows. As when we selected columns above, we can use square
brackets to extract *slices* from the dataframe. A slice is a subset of
the dataframe starting at one row and ending at another. To get a slice,
we pass the starting and ending indexes to the square brackets as
`start:end`:

```python
surveys[2:5]
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

-   Row indexes are zero-based. That is, the first row has an index of
    0, not 1.
-   When slicing, the slice includes start but not the end index. In
    this case, that means the slice includes rows 2, 3, and 4 but not 5.
-   The row label can be different from the row index. They happen to be
    the same here, but don't count on that being true.

Core Python types like `list` and `tuple` use the same conventions, as
do most libraries that deal with sequences.

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

## Calculating values

The survey dataset includes two columns, hindfoot_length and weight,
that are stored as numbers and represent measurements. We may want to
perform calculations using numbers like these in our own data. We can do
so using Python's built-in mathematical operators, including:

-   `x + y` for addition
-   `x - y` for subtraction
-   `x * y` for multiplication
-   `x / y` for division
-   `x % y` for calculating remainders
-   `x ** y` for exponents

To make the examples in this section a little more useful, we're going
to remove all rows that contain null values using the `dropna()` method.
This will filter out any rows that don't have a valid hindfoot_length or
weight, as well as those that have a null value in any other cell. (This
is an inelegant solution to the problem of missing data. We'll talk
about more nuanced solutions later in the lesson.)

```python
surveys_nona = surveys.dropna().copy()
surveys_nona
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
      <th>62</th>
      <td>63</td>
      <td>8</td>
      <td>19</td>
      <td>1977</td>
      <td>3</td>
      <td>DM</td>
      <td>M</td>
      <td>35.0</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>63</th>
      <td>64</td>
      <td>8</td>
      <td>19</td>
      <td>1977</td>
      <td>7</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>48.0</td>
    </tr>
    <tr>
      <th>64</th>
      <td>65</td>
      <td>8</td>
      <td>19</td>
      <td>1977</td>
      <td>4</td>
      <td>DM</td>
      <td>F</td>
      <td>34.0</td>
      <td>29.0</td>
    </tr>
    <tr>
      <th>65</th>
      <td>66</td>
      <td>8</td>
      <td>19</td>
      <td>1977</td>
      <td>4</td>
      <td>DM</td>
      <td>F</td>
      <td>35.0</td>
      <td>46.0</td>
    </tr>
    <tr>
      <th>66</th>
      <td>67</td>
      <td>8</td>
      <td>19</td>
      <td>1977</td>
      <td>7</td>
      <td>DM</td>
      <td>M</td>
      <td>35.0</td>
      <td>36.0</td>
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
      <th>35540</th>
      <td>35541</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>PB</td>
      <td>F</td>
      <td>24.0</td>
      <td>31.0</td>
    </tr>
    <tr>
      <th>35541</th>
      <td>35542</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>PB</td>
      <td>F</td>
      <td>26.0</td>
      <td>29.0</td>
    </tr>
    <tr>
      <th>35542</th>
      <td>35543</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>PB</td>
      <td>F</td>
      <td>27.0</td>
      <td>34.0</td>
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
  </tbody>
</table>
<p>30676 rows × 9 columns</p>

Suppose we want to convert the weight column from grams to milligrams.
To do so, we can multiply that column by 1000:

```python
surveys_nona["weight"] * 1000
```

```{.output}
62       40000.0
63       48000.0
64       29000.0
65       46000.0
66       36000.0
          ...   
35540    31000.0
35541    29000.0
35542    34000.0
35546    14000.0
35547    51000.0
Name: weight, Length: 30676, dtype: float64
```

To convert it to kilograms, we can divide by 1000:

```python
surveys_nona["weight"] / 1000
```

```{.output}
62       0.040
63       0.048
64       0.029
65       0.046
66       0.036
         ...  
35540    0.031
35541    0.029
35542    0.034
35546    0.014
35547    0.051
Name: weight, Length: 30676, dtype: float64
```

Note that calculations do not modify the original dataset. If we want to
retain the result, we have to assign it to a new column:

```python
surveys_nona["weight_mg"] = surveys_nona["weight"] * 1000
surveys_nona
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
      <th>weight_mg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>62</th>
      <td>63</td>
      <td>8</td>
      <td>19</td>
      <td>1977</td>
      <td>3</td>
      <td>DM</td>
      <td>M</td>
      <td>35.0</td>
      <td>40.0</td>
      <td>40000.0</td>
    </tr>
    <tr>
      <th>63</th>
      <td>64</td>
      <td>8</td>
      <td>19</td>
      <td>1977</td>
      <td>7</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>48.0</td>
      <td>48000.0</td>
    </tr>
    <tr>
      <th>64</th>
      <td>65</td>
      <td>8</td>
      <td>19</td>
      <td>1977</td>
      <td>4</td>
      <td>DM</td>
      <td>F</td>
      <td>34.0</td>
      <td>29.0</td>
      <td>29000.0</td>
    </tr>
    <tr>
      <th>65</th>
      <td>66</td>
      <td>8</td>
      <td>19</td>
      <td>1977</td>
      <td>4</td>
      <td>DM</td>
      <td>F</td>
      <td>35.0</td>
      <td>46.0</td>
      <td>46000.0</td>
    </tr>
    <tr>
      <th>66</th>
      <td>67</td>
      <td>8</td>
      <td>19</td>
      <td>1977</td>
      <td>7</td>
      <td>DM</td>
      <td>M</td>
      <td>35.0</td>
      <td>36.0</td>
      <td>36000.0</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>35540</th>
      <td>35541</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>PB</td>
      <td>F</td>
      <td>24.0</td>
      <td>31.0</td>
      <td>31000.0</td>
    </tr>
    <tr>
      <th>35541</th>
      <td>35542</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>PB</td>
      <td>F</td>
      <td>26.0</td>
      <td>29.0</td>
      <td>29000.0</td>
    </tr>
    <tr>
      <th>35542</th>
      <td>35543</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>PB</td>
      <td>F</td>
      <td>27.0</td>
      <td>34.0</td>
      <td>34000.0</td>
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
      <td>14000.0</td>
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
      <td>51000.0</td>
    </tr>
  </tbody>
</table>
<p>30676 rows × 10 columns</p>

We can also add, subtract, multiply, and divide columns, as in the
following (admittedly nonsensical) calculation, which adds together the
hindfoot_length and weight columns:

```python
surveys_nona["hindfoot_length"] + surveys_nona["weight"]
```

```{.output}
62       75.0
63       85.0
64       63.0
65       81.0
66       71.0
         ...
35540    55.0
35541    55.0
35542    61.0
35546    29.0
35547    87.0
Length: 30676, dtype: float64
```

## Renaming columns

The hindfoot_length and weight columns don't specify a unit, which may
get confusing if we want to perform unit conversions like the one above.
Fortunately, dataframes allow us to rename existing columns using the
`rename()` method.

The `rename()` method uses a dictionary (or `dict`) to map between the
old and new column names. As with `list` above, the `dict` data type is
built into Python--we don't need to import anything to use it. A `dict`
maps keys to values. We can create one using curly braces:

```python
dct = {"key1": "val1", "key2": "val2"}
dct
```

```{.output}
{'key1': 'val1', 'key2': 'val2'}
```

Dictionaries are a useful and highly flexible data type. As with `list`
above, we'll be giving them short shrift here, but you can learn more
about them at [the Python
docs](https://docs.python.org/3/library/stdtypes.html#dict).

Here we'll use a `dict` to specify how we want to rename our columns.
The *keys* will be the current column names and the *values* the new
column names. Note that we explicitly assign the result of `rename()` to
the original variable--by default, `rename()` returns a copy of the
original dataframe instead of modifying the original dataframe.

```python
# Create a dict that maps from the old to the new column name
cols = {
    "hindfoot_length": "hindfoot_length_mm",
    "weight": "weight_g",
}

# Assign the result of the rename method back to surveys_nona
surveys_nona = surveys_nona.rename(columns=cols)

# View the dataframe with the new column names
surveys_nona
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
      <th>hindfoot_length_mm</th>
      <th>weight_g</th>
      <th>weight_mg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>62</th>
      <td>63</td>
      <td>8</td>
      <td>19</td>
      <td>1977</td>
      <td>3</td>
      <td>DM</td>
      <td>M</td>
      <td>35.0</td>
      <td>40.0</td>
      <td>40000.0</td>
    </tr>
    <tr>
      <th>63</th>
      <td>64</td>
      <td>8</td>
      <td>19</td>
      <td>1977</td>
      <td>7</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>48.0</td>
      <td>48000.0</td>
    </tr>
    <tr>
      <th>64</th>
      <td>65</td>
      <td>8</td>
      <td>19</td>
      <td>1977</td>
      <td>4</td>
      <td>DM</td>
      <td>F</td>
      <td>34.0</td>
      <td>29.0</td>
      <td>29000.0</td>
    </tr>
    <tr>
      <th>65</th>
      <td>66</td>
      <td>8</td>
      <td>19</td>
      <td>1977</td>
      <td>4</td>
      <td>DM</td>
      <td>F</td>
      <td>35.0</td>
      <td>46.0</td>
      <td>46000.0</td>
    </tr>
    <tr>
      <th>66</th>
      <td>67</td>
      <td>8</td>
      <td>19</td>
      <td>1977</td>
      <td>7</td>
      <td>DM</td>
      <td>M</td>
      <td>35.0</td>
      <td>36.0</td>
      <td>36000.0</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>35540</th>
      <td>35541</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>PB</td>
      <td>F</td>
      <td>24.0</td>
      <td>31.0</td>
      <td>31000.0</td>
    </tr>
    <tr>
      <th>35541</th>
      <td>35542</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>PB</td>
      <td>F</td>
      <td>26.0</td>
      <td>29.0</td>
      <td>29000.0</td>
    </tr>
    <tr>
      <th>35542</th>
      <td>35543</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>PB</td>
      <td>F</td>
      <td>27.0</td>
      <td>34.0</td>
      <td>34000.0</td>
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
      <td>14000.0</td>
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
      <td>51000.0</td>
    </tr>
  </tbody>
</table>
<p>30676 rows × 10 columns</p>

::: challenge ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Create a dataframe that returns the year, month, day, species_id and
weight in mg.

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

```python
# Assign the weight in milligrams to the weight_mg column
surveys_nona["weight_mg"] = surveys_nona["weight_g"] * 1000

# Display a copy of survey with only the desired columns
surveys_nona[["year", "month", "day", "species_id", "weight_mg"]]
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
      <th>species_id</th>
      <th>weight_mg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>62</th>
      <td>1977</td>
      <td>8</td>
      <td>19</td>
      <td>DM</td>
      <td>40000.0</td>
    </tr>
    <tr>
      <th>63</th>
      <td>1977</td>
      <td>8</td>
      <td>19</td>
      <td>DM</td>
      <td>48000.0</td>
    </tr>
    <tr>
      <th>64</th>
      <td>1977</td>
      <td>8</td>
      <td>19</td>
      <td>DM</td>
      <td>29000.0</td>
    </tr>
    <tr>
      <th>65</th>
      <td>1977</td>
      <td>8</td>
      <td>19</td>
      <td>DM</td>
      <td>46000.0</td>
    </tr>
    <tr>
      <th>66</th>
      <td>1977</td>
      <td>8</td>
      <td>19</td>
      <td>DM</td>
      <td>36000.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>35540</th>
      <td>2002</td>
      <td>12</td>
      <td>31</td>
      <td>PB</td>
      <td>31000.0</td>
    </tr>
    <tr>
      <th>35541</th>
      <td>2002</td>
      <td>12</td>
      <td>31</td>
      <td>PB</td>
      <td>29000.0</td>
    </tr>
    <tr>
      <th>35542</th>
      <td>2002</td>
      <td>12</td>
      <td>31</td>
      <td>PB</td>
      <td>34000.0</td>
    </tr>
    <tr>
      <th>35546</th>
      <td>2002</td>
      <td>12</td>
      <td>31</td>
      <td>RM</td>
      <td>14000.0</td>
    </tr>
    <tr>
      <th>35547</th>
      <td>2002</td>
      <td>12</td>
      <td>31</td>
      <td>DO</td>
      <td>51000.0</td>
    </tr>
  </tbody>
</table>
<p>30676 rows × 5 columns</p>

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## Filtering data

pandas provides a variety of ways to filter a dataframe. For example,
suppose we want to look at a specific species in the surveys_nona
dataframe. We can view the rows matching a given species using the same
square brackets we used above to select specific columns and rows. Here,
however, instead of passing a value or list of values, we will pass a
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
conditional `surveys_nona["species_id"] == "DM"` inside the square
brackets:

```python
surveys_nona[surveys_nona["species_id"] == "DM"]
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
      <th>hindfoot_length_mm</th>
      <th>weight_g</th>
      <th>weight_mg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>62</th>
      <td>63</td>
      <td>8</td>
      <td>19</td>
      <td>1977</td>
      <td>3</td>
      <td>DM</td>
      <td>M</td>
      <td>35.0</td>
      <td>40.0</td>
      <td>40000.0</td>
    </tr>
    <tr>
      <th>63</th>
      <td>64</td>
      <td>8</td>
      <td>19</td>
      <td>1977</td>
      <td>7</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>48.0</td>
      <td>48000.0</td>
    </tr>
    <tr>
      <th>64</th>
      <td>65</td>
      <td>8</td>
      <td>19</td>
      <td>1977</td>
      <td>4</td>
      <td>DM</td>
      <td>F</td>
      <td>34.0</td>
      <td>29.0</td>
      <td>29000.0</td>
    </tr>
    <tr>
      <th>65</th>
      <td>66</td>
      <td>8</td>
      <td>19</td>
      <td>1977</td>
      <td>4</td>
      <td>DM</td>
      <td>F</td>
      <td>35.0</td>
      <td>46.0</td>
      <td>46000.0</td>
    </tr>
    <tr>
      <th>66</th>
      <td>67</td>
      <td>8</td>
      <td>19</td>
      <td>1977</td>
      <td>7</td>
      <td>DM</td>
      <td>M</td>
      <td>35.0</td>
      <td>36.0</td>
      <td>36000.0</td>
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
      <td>48000.0</td>
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
      <td>56000.0</td>
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
      <td>53000.0</td>
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
      <td>42000.0</td>
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
      <td>46000.0</td>
    </tr>
  </tbody>
</table>
<p>9727 rows × 10 columns</p>

To limit our results to observations made in or after 2000, use:

```python
surveys_nona[surveys_nona["year"] >= 2000]
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
      <th>hindfoot_length_mm</th>
      <th>weight_g</th>
      <th>weight_mg</th>
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
      <td>17000.0</td>
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
      <td>53000.0</td>
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
      <td>17000.0</td>
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
      <td>50000.0</td>
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
      <td>16000.0</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>35540</th>
      <td>35541</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>PB</td>
      <td>F</td>
      <td>24.0</td>
      <td>31.0</td>
      <td>31000.0</td>
    </tr>
    <tr>
      <th>35541</th>
      <td>35542</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>PB</td>
      <td>F</td>
      <td>26.0</td>
      <td>29.0</td>
      <td>29000.0</td>
    </tr>
    <tr>
      <th>35542</th>
      <td>35543</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>PB</td>
      <td>F</td>
      <td>27.0</td>
      <td>34.0</td>
      <td>34000.0</td>
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
      <td>14000.0</td>
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
      <td>51000.0</td>
    </tr>
  </tbody>
</table>
<p>4947 rows × 10 columns</p>

As with `rename()` above, each filtering operation returns a copy of the
dataframe. We will look at how to make changes to the original dataframe
at the end of this lesson.

## Building more complex queries

We can combine conditionals using what are called *bitwise operators*:

-   `&`: True if conditions on both sides of the operator are True (and)
-   `|`: True if a condition on either side is True (or)

To return all observations of DM in or after 2000, we can combine the
two conditionals we used previously. Note that, when joining
conditionals using `&` or `|`, we must wrap each individual condition in
parentheses. If we omit the parentheses, pandas will not perform the
comparisons in the expected order.

```python
surveys_nona[(surveys_nona["species_id"] == "DM") & (surveys_nona["year"] >= 2000)]
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
      <th>hindfoot_length_mm</th>
      <th>weight_g</th>
      <th>weight_mg</th>
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
      <td>50000.0</td>
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
      <td>60000.0</td>
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
      <td>52000.0</td>
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
      <td>43000.0</td>
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
      <td>56000.0</td>
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
      <td>48000.0</td>
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
      <td>56000.0</td>
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
      <td>53000.0</td>
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
      <td>42000.0</td>
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
      <td>46000.0</td>
    </tr>
  </tbody>
</table>
<p>823 rows × 10 columns</p>

Some column methods can also be used for filtering. One example is
`isin()`, which is used to match a list of values. This method can be
combined with other conditionals as above. The example below returns
rows from 2000 or later with either "DM", "DO", or "DS" in the
species_id column:

```python
surveys_nona[
    surveys_nona["species_id"].isin(["DM", "DO", "DS"]) & (surveys_nona["year"] >= 2000)
]
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
      <th>hindfoot_length_mm</th>
      <th>weight_g</th>
      <th>weight_mg</th>
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
      <td>53000.0</td>
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
      <td>50000.0</td>
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
      <td>41000.0</td>
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
      <td>52000.0</td>
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
      <td>54000.0</td>
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
      <td>56000.0</td>
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
      <td>53000.0</td>
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
      <td>42000.0</td>
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
      <td>46000.0</td>
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
      <td>51000.0</td>
    </tr>
  </tbody>
</table>
<p>1229 rows × 10 columns</p>

## Sorting data

We can sort a dataframe using the `sort_values()` method. For this
example, we'll work from the subset defined above. First we need to
assign that subset to a variable:

```python
results = surveys_nona[
    surveys_nona["species_id"].isin(["DM", "DO", "DS"]) & (surveys_nona["year"] >= 2000)
]
```

Now we'll sort the results by weight_g. To do so, pass that column name
as an argument (that is, inside the trailing parentheses) to the
`sort_values()` method:

```python
results.sort_values("weight_g")
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
      <th>hindfoot_length_mm</th>
      <th>weight_g</th>
      <th>weight_mg</th>
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
      <td>18000.0</td>
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
      <td>20000.0</td>
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
      <td>21000.0</td>
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
      <td>21000.0</td>
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
      <td>22000.0</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>35159</th>
      <td>35160</td>
      <td>11</td>
      <td>10</td>
      <td>2002</td>
      <td>13</td>
      <td>DO</td>
      <td>F</td>
      <td>36.0</td>
      <td>65.0</td>
      <td>65000.0</td>
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
      <td>65000.0</td>
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
      <td>68000.0</td>
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
      <td>68000.0</td>
    </tr>
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
      <td>76000.0</td>
    </tr>
  </tbody>
</table>
<p>1229 rows × 10 columns</p>

By default, rows are sorted in ascending order (smallest to largest). We
can modify this behavior using the *ascending* keyword argument:

```python
results.sort_values("weight_g", ascending=False)
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
      <th>hindfoot_length_mm</th>
      <th>weight_g</th>
      <th>weight_mg</th>
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
      <td>76000.0</td>
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
      <td>68000.0</td>
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
      <td>68000.0</td>
    </tr>
    <tr>
      <th>35159</th>
      <td>35160</td>
      <td>11</td>
      <td>10</td>
      <td>2002</td>
      <td>13</td>
      <td>DO</td>
      <td>F</td>
      <td>36.0</td>
      <td>65.0</td>
      <td>65000.0</td>
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
      <td>65000.0</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>32957</th>
      <td>32958</td>
      <td>10</td>
      <td>14</td>
      <td>2001</td>
      <td>9</td>
      <td>DM</td>
      <td>F</td>
      <td>33.0</td>
      <td>22.0</td>
      <td>22000.0</td>
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
      <td>21000.0</td>
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
      <td>21000.0</td>
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
      <td>20000.0</td>
    </tr>
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
      <td>18000.0</td>
    </tr>
  </tbody>
</table>
<p>1229 rows × 10 columns</p>

We can sort on multiple fields at once by passing a list of column
names. We can control how each column sorts by passing a list with the
same number of values (that is, one value per column) to the ascending
keyword. The cell below sorts the results first by species_id (largest
to smallest), then by weight (smallest to largest):

```python
results.sort_values(["species_id", "weight_g"], ascending=[False, True])
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
      <th>hindfoot_length_mm</th>
      <th>weight_g</th>
      <th>weight_mg</th>
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
      <td>23000.0</td>
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
      <td>24000.0</td>
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
      <td>24000.0</td>
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
      <td>24000.0</td>
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
      <td>24000.0</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>31858</th>
      <td>31859</td>
      <td>3</td>
      <td>24</td>
      <td>2001</td>
      <td>2</td>
      <td>DM</td>
      <td>F</td>
      <td>36.0</td>
      <td>60.0</td>
      <td>60000.0</td>
    </tr>
    <tr>
      <th>32909</th>
      <td>32910</td>
      <td>10</td>
      <td>14</td>
      <td>2001</td>
      <td>4</td>
      <td>DM</td>
      <td>F</td>
      <td>37.0</td>
      <td>60.0</td>
      <td>60000.0</td>
    </tr>
    <tr>
      <th>34604</th>
      <td>34605</td>
      <td>7</td>
      <td>14</td>
      <td>2002</td>
      <td>9</td>
      <td>DM</td>
      <td>F</td>
      <td>36.0</td>
      <td>60.0</td>
      <td>60000.0</td>
    </tr>
    <tr>
      <th>34675</th>
      <td>34676</td>
      <td>9</td>
      <td>8</td>
      <td>2002</td>
      <td>12</td>
      <td>DM</td>
      <td>F</td>
      <td>36.0</td>
      <td>60.0</td>
      <td>60000.0</td>
    </tr>
    <tr>
      <th>34126</th>
      <td>34127</td>
      <td>5</td>
      <td>16</td>
      <td>2002</td>
      <td>9</td>
      <td>DM</td>
      <td>F</td>
      <td>35.0</td>
      <td>64.0</td>
      <td>64000.0</td>
    </tr>
  </tbody>
</table>
<p>1229 rows × 10 columns</p>

As with the dataframe methods above, `sort_values()` returns a copy of
the original dataframe and leaves the original untouched.

::: challenge ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Write a query that returns year, species_id, and weight in kg from the
surveys_nona table, sorted with the largest weights at the top.

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

```python
# Create a new column with weight in kg
surveys_nona["weight_kg"] = surveys_nona["weight_g"] / 1000

# Create a subset containing only year, species_id, and weight_kg
subset = surveys_nona[["year", "species_id", "weight_kg"]]

# Sort the subset by weight_kg
subset.sort_values("weight_kg", ascending=False)
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
      <th>weight_kg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>33048</th>
      <td>2001</td>
      <td>NL</td>
      <td>0.280</td>
    </tr>
    <tr>
      <th>12870</th>
      <td>1987</td>
      <td>NL</td>
      <td>0.278</td>
    </tr>
    <tr>
      <th>15458</th>
      <td>1989</td>
      <td>NL</td>
      <td>0.275</td>
    </tr>
    <tr>
      <th>2132</th>
      <td>1979</td>
      <td>NL</td>
      <td>0.274</td>
    </tr>
    <tr>
      <th>12728</th>
      <td>1987</td>
      <td>NL</td>
      <td>0.270</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>29905</th>
      <td>1999</td>
      <td>PP</td>
      <td>0.004</td>
    </tr>
    <tr>
      <th>9908</th>
      <td>1985</td>
      <td>RM</td>
      <td>0.004</td>
    </tr>
    <tr>
      <th>10438</th>
      <td>1985</td>
      <td>RM</td>
      <td>0.004</td>
    </tr>
    <tr>
      <th>8735</th>
      <td>1983</td>
      <td>RM</td>
      <td>0.004</td>
    </tr>
    <tr>
      <th>7083</th>
      <td>1982</td>
      <td>PF</td>
      <td>0.004</td>
    </tr>
  </tbody>
</table>
<p>30676 rows × 3 columns</p>

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## Modifying data

We've already shown how to modify an existing a dataframe by adding a
new column. What if we want to modify existing cells instead? As we've
seen, this can be a little tricky in pandas because most of its methods
return a copy of the original dataframe. For example, we can get subsets
of a dataframe using square brackets. The cell below returns the
species_id column for rows 2 through 5:

```python
surveys[2:6]["species_id"]
```

```{.output}
2    DM
3    DM
4    DM
5    PF
Name: species_id, dtype: object
```

But trying to set new values using this syntax may not work as expected.
When working with the full dataframe, we can use

Say we want to set the species_id column to a new value, "FD". Try
running the code in the cell below:

```python
surveys[2:6]["species_id"] = "FD"
```

```{.output}
C:\...\1234567890.py:1: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  surveys[2:6]["species_id"] = "FD"

```

You should have received a `SettingWithCopyWarning` warning after
running that cell. This warning tells us that the data in the original
dataframe has not been modified. This is because the square brackets
returned a copy, meaning that any changes will be reflected in the copy,
not the original. We can verify that the original dataframe has not been
changed by displaying the rows that would have been modified:

```python
surveys[2:6]
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
  </tbody>
</table>

### Using loc to modify existing cells

One way to modify existing data in pandas is to use the `loc` attribute.
This attribute allows you to extract and modify cells in a DataFrame
using the following syntax: `df.loc[row_indexer, col_indexer]`.

The *row_indexer* argument is used to select one or more rows. It can
be: - A row label (i.e., the bold column on the far left) - `0` returns
the row with label 0

-   A slice including multiple rows:
    -   `:` returns all rows
    -   `:2` returns all rows from the beginning of the dataframe to the
        row labeled 2, *inclusive*
    -   `2:` returns all rows from the row labeled 2 to the end of the
        dataframe, *inclusive*
    -   `2:5` returns all rows between those labeled 2 and 5,
        *inclusive*
-   A conditional, as in the examples above.

The *col_indexer* argument is used to select one or more columns. It
will typically be a list of column names and can be omitted, in which
case all columns will be returned.

::: callout ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### Row labels and indexes

The row labels in this dataframe happen to be numeric and aligned
exactly to the row's index (so for the first row both the index and the
label are 0, for the second row both the index and the label are 1,
etc.) This is often **but not always** true in pandas. For example, if
we used record_id as the label, the row labels would be one-based and
the row indexes would be zero-based.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: callout ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### loc slicing behavior

Slices using `loc` are inclusive--rows matching both the start and end
values are included in the returned slice. This differs from list
slices, where the start but not end value is included in the slice.
`loc` works this way because it is looking at the row *label*, not the
row *index*.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

We'll be making some changes to our data, so let's work from a copy
instead of modifying the original. Create a copy using the `copy()`
method:

```python
surveys_copy = surveys.copy()
```

To select a subset of rows and columns using `loc`, use:

```python
surveys_copy.loc[2:5, "species_id"]
```

```{.output}
2    DM
3    DM
4    DM
5    PF
Name: species_id, dtype: object
```

Unlike the methods earlier in the lesson, this is a view, not a copy, of
the data in the surveys_copy dataframe. That means that the object
returned by loc is live and can be used to change the original
dataframe. We can now assign a new value to the species_id column in the
matching rows of the original dataframe:

```python
surveys_copy.loc[2:5, "species_id"] = "FD"
```

We can see that these changes are reflected in the original surveys_copy
object:

```python
surveys_copy.loc[1:6, "species_id"]
```

```{.output}
1    NL
2    FD
3    FD
4    FD
5    FD
6    PE
Name: species_id, dtype: object
```

::: callout ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### Slicing with iloc

pandas provides another indexer, `iloc`, that allows us to select and
modify data using row and column indexes instead of labels. Learn more
in the [pandas
documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html).

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

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
