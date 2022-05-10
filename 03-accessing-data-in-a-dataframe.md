---
title: Accessing Data in a Dataframe
---

::: questions ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   How can we look at individual rows and columns?
-   How can we perform calculations on the data?
-   How can we modify data?

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: objectives :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   Use square brackets to access individual rows and columns
-   Grab multiple columns at once using a list
-   Rename columns using a dictionary

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

We'll begin by importing pandas and reading our CSV, as we did in the
previous lesson:


```python
import pandas as pd

surveys = pd.read_csv("data/surveys.csv")
```

## Viewing the dataframe

To view a dataframe in a Jupyter Notebook, type the variable name as the
last line of the cell. By default, this will display the first and last
five rows of the dataframe:


```python
surveys
```

```{.output}
       record_id  month  day  year  ...  species_id  sex hindfoot_length  weight
0              1      7   16  1977  ...          NL    M            32.0     NaN
1              2      7   16  1977  ...          NL    M            33.0     NaN
2              3      7   16  1977  ...          DM    F            37.0     NaN
3              4      7   16  1977  ...          DM    M            36.0     NaN
4              5      7   16  1977  ...          DM    M            35.0     NaN
...          ...    ...  ...   ...  ...         ...  ...             ...     ...
35544      35545     12   31  2002  ...          AH  NaN             NaN     NaN
35545      35546     12   31  2002  ...          AH  NaN             NaN     NaN
35546      35547     12   31  2002  ...          RM    F            15.0    14.0
35547      35548     12   31  2002  ...          DO    M            36.0    51.0
35548      35549     12   31  2002  ...         NaN  NaN             NaN     NaN

[35549 rows x 9 columns]
```

We will now look at how to access rows and columns in the dataframe.

### Columns

You can get the values from a single column using square brackets at the
end of the dataframe object. For example, to look at the year column,
use:


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

Python using the built-in `list` data type to store sequences, that is,
an ordered list of objects. Any type of Python object can be store in a
list: strings, integers, floats, even other lists. Once created, a list
can be modified by appending, inserting, or deleting items. We will not
be going into detail about these operations here, but as always you can
learn more about how to use a list using `help()` or [the Python
docs](https://docs.python.org/3/library/stdtypes.html#list).

Create a list using square brackets. Let's create a list of the three
columns in our dataframe that are related to the date:


```python
cols = ["year", "month", "day"]
```

When we pass this list to the square brackets, as we did above, we
retrieve a copy of the dataframe containing just those columns:


```python
surveys[cols]
```

```{.output}
       year  month  day
0      1977      7   16
1      1977      7   16
2      1977      7   16
3      1977      7   16
4      1977      7   16
...     ...    ...  ...
35544  2002     12   31
35545  2002     12   31
35546  2002     12   31
35547  2002     12   31
35548  2002     12   31

[35549 rows x 3 columns]
```

## Rows

You can get the rows at the beginning of the table using the head
method:


```python
surveys.head()
```

```{.output}
   record_id  month  day  year  plot_id species_id sex  hindfoot_length  weight
0          1      7   16  1977        2         NL   M             32.0     NaN
1          2      7   16  1977        3         NL   M             33.0     NaN
2          3      7   16  1977        2         DM   F             37.0     NaN
3          4      7   16  1977        7         DM   M             36.0     NaN
4          5      7   16  1977        3         DM   M             35.0     NaN
```

Provide a number inside the parentheses if you want a specific number of
rows:


```python
surveys.head(20)
```

```{.output}
    record_id  month  day  year  ...  species_id  sex hindfoot_length  weight
0           1      7   16  1977  ...          NL    M            32.0     NaN
1           2      7   16  1977  ...          NL    M            33.0     NaN
2           3      7   16  1977  ...          DM    F            37.0     NaN
3           4      7   16  1977  ...          DM    M            36.0     NaN
4           5      7   16  1977  ...          DM    M            35.0     NaN
5           6      7   16  1977  ...          PF    M            14.0     NaN
6           7      7   16  1977  ...          PE    F             NaN     NaN
7           8      7   16  1977  ...          DM    M            37.0     NaN
8           9      7   16  1977  ...          DM    F            34.0     NaN
9          10      7   16  1977  ...          PF    F            20.0     NaN
10         11      7   16  1977  ...          DS    F            53.0     NaN
11         12      7   16  1977  ...          DM    M            38.0     NaN
12         13      7   16  1977  ...          DM    M            35.0     NaN
13         14      7   16  1977  ...          DM  NaN             NaN     NaN
14         15      7   16  1977  ...          DM    F            36.0     NaN
15         16      7   16  1977  ...          DM    F            36.0     NaN
16         17      7   16  1977  ...          DS    F            48.0     NaN
17         18      7   16  1977  ...          PP    M            22.0     NaN
18         19      7   16  1977  ...          PF  NaN             NaN     NaN
19         20      7   17  1977  ...          DS    F            48.0     NaN

[20 rows x 9 columns]
```

The `tail()` method is similar, except it returns rows from the end of
the table:


```python
surveys.tail()
```

```{.output}
       record_id  month  day  year  ...  species_id  sex hindfoot_length  weight
35544      35545     12   31  2002  ...          AH  NaN             NaN     NaN
35545      35546     12   31  2002  ...          AH  NaN             NaN     NaN
35546      35547     12   31  2002  ...          RM    F            15.0    14.0
35547      35548     12   31  2002  ...          DO    M            36.0    51.0
35548      35549     12   31  2002  ...         NaN  NaN             NaN     NaN

[5 rows x 9 columns]
```

The `head()` and `tail()` methods are useful for getting a feel for how
our data is structured, but we'll also want to  be able to look at
specific rows. As when we selected columns above, we can use square
brackets to extract *slices* from the dataframe. This time, however, we
pass two numbers separated by a colon representing the starting and
ending indexes:


```python
surveys[2:5]
```

```{.output}
   record_id  month  day  year  plot_id species_id sex  hindfoot_length  weight
2          3      7   16  1977        2         DM   F             37.0     NaN
3          4      7   16  1977        7         DM   M             36.0     NaN
4          5      7   16  1977        3         DM   M             35.0     NaN
```

There are three things to be aware of when slicing a dataframe:

-   Row indexes are zero-based. That is, the first row has an index
    of 0, not 1.
-   When slicing, the slice includes start but not end index. In
    this case, that means the slice includes rows 2, 3, and 4 but
    not 5.
-   The row label can be different from the row index

Core Python types like `list` and `tuple` use the same conventions, as
do most libraries that deal with sequences.

## Unique values

Recall that you can use square brackets to return a single column from a
dataframe. You can get the list of unique values within that column
using the `unique()` method:


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

`pandas` does not provide a dedicated function or method to find
distinct values across multiple columns. However, we can use the
`drop_duplicates()` method on a copy of the dataframe containing only
the columns we're interested in to get the expected result:


```python
subset = surveys[["plot_id", "species_id"]]
subset.drop_duplicates()
```

```{.output}
       plot_id species_id
0            2         NL
1            3         NL
2            2         DM
3            7         DM
4            3         DM
...        ...        ...
35474       22         SF
35511       11         US
35519        9         SF
35527       13         US
35543       15         US

[612 rows x 2 columns]
```

## Calculated values

The survey dataset includes two columns, hindfoot_length and weight,
that are stored as numbers and represent measurements. You may want to
perform calculations using numbers like these in your own data. You can
do so using Python's built-in mathematical operators, including:

-   `+` for addition
-   `-` for subtraction
-   `*` for multiplication
-   `/` for division
-   `**` for exponents

For example, to convert all values in the weight column from grams to
milligrams, we can multiply the column by 1000:


```python
surveys["weight"] * 1000
```

```{.output}
0            NaN
1            NaN
2            NaN
3            NaN
4            NaN
          ...   
35544        NaN
35545        NaN
35546    14000.0
35547    51000.0
35548        NaN
Name: weight, Length: 35549, dtype: float64
```

To convert it to kilograms, we can divide by 1000:


```python
surveys["weight"] / 1000
```

```{.output}
0          NaN
1          NaN
2          NaN
3          NaN
4          NaN
         ...  
35544      NaN
35545      NaN
35546    0.014
35547    0.051
35548      NaN
Name: weight, Length: 35549, dtype: float64
```

Note that this calculation does not modify the original dataset. If we
want to retain the result, we have to assign it to a new column:


```python
surveys["weight_mg"] = surveys["weight"] * 1000

# Now the weight_mg columns appear in our dataframe
surveys
```

```{.output}
       record_id  month  day  year  ...  sex hindfoot_length weight  weight_mg
0              1      7   16  1977  ...    M            32.0    NaN        NaN
1              2      7   16  1977  ...    M            33.0    NaN        NaN
2              3      7   16  1977  ...    F            37.0    NaN        NaN
3              4      7   16  1977  ...    M            36.0    NaN        NaN
4              5      7   16  1977  ...    M            35.0    NaN        NaN
...          ...    ...  ...   ...  ...  ...             ...    ...        ...
35544      35545     12   31  2002  ...  NaN             NaN    NaN        NaN
35545      35546     12   31  2002  ...  NaN             NaN    NaN        NaN
35546      35547     12   31  2002  ...    F            15.0   14.0    14000.0
35547      35548     12   31  2002  ...    M            36.0   51.0    51000.0
35548      35549     12   31  2002  ...  NaN             NaN    NaN        NaN

[35549 rows x 10 columns]
```

You can also add, subtract, multiply, and divide columns, as in the
following (admittedly nonsensical) calculation, which adds together the
hindfoot_length and weight columns:


```python
surveys["hindfoot_length"] + surveys["weight"]
```

```{.output}
0         NaN
1         NaN
2         NaN
3         NaN
4         NaN
         ... 
35544     NaN
35545     NaN
35546    29.0
35547    87.0
35548     NaN
Length: 35549, dtype: float64
```

## Renaming columns

The hindfoot_length and weight columns don't specify a unit, which may
get confusing if we want to perform unit conversions like the one above.
Fortunately, dataframes allow us to rename existing columns using
`rename()`.

The `rename()` method uses a dictionary (or `dict`) to map between the
old and new column names. The `dict` data type is built in to Python--
you don't need to import anything to use it. They consist of keys and
values. You can create a `dict` using curly braces:


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

Here we'll use a dict to specify how we want to rename our columns. The
*keys* will be the current columns names and the *values* are the new
column names. Note that we explicitly assign the result of `rename()` to
the original variable--by default, `rename()` returns a copy of the
original dataframe instead of modifying the original dataframe. Most
dataframe operations work this way.


```python
# Create a dict that maps from the old to the new column name
cols = {
    "hindfoot_length": "hindfoot_length_mm",
    "weight": "weight_g",
}

# Assign the result of the rename method back to surveys
surveys = surveys.rename(columns=cols)

# View the dataframe with the new column names
surveys
```

```{.output}
       record_id  month  day  ...  hindfoot_length_mm  weight_g weight_mg
0              1      7   16  ...                32.0       NaN       NaN
1              2      7   16  ...                33.0       NaN       NaN
2              3      7   16  ...                37.0       NaN       NaN
3              4      7   16  ...                36.0       NaN       NaN
4              5      7   16  ...                35.0       NaN       NaN
...          ...    ...  ...  ...                 ...       ...       ...
35544      35545     12   31  ...                 NaN       NaN       NaN
35545      35546     12   31  ...                 NaN       NaN       NaN
35546      35547     12   31  ...                15.0      14.0   14000.0
35547      35548     12   31  ...                36.0      51.0   51000.0
35548      35549     12   31  ...                 NaN       NaN       NaN

[35549 rows x 10 columns]
```

::: challenge ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Create a dataframe that returns the year, month, day, species_id and
weight in mg.

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


```python
# Assign the weight in milligrams to the weight_mg column
surveys["weight_mg"] = surveys["weight_g"] * 1000

# Create a copy of the year, month, day, and weight_mg columns
subset = surveys[["year", "month", "day", "weight_mg"]]

# View the subset
subset
```

```{.output}
       year  month  day  weight_mg
0      1977      7   16        NaN
1      1977      7   16        NaN
2      1977      7   16        NaN
3      1977      7   16        NaN
4      1977      7   16        NaN
...     ...    ...  ...        ...
35544  2002     12   31        NaN
35545  2002     12   31        NaN
35546  2002     12   31    14000.0
35547  2002     12   31    51000.0
35548  2002     12   31        NaN

[35549 rows x 4 columns]
```

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## Filtering

`pandas` provides a variety of ways to filter the data in the dataframe.
For example, suppose you want to look at a specific species in the
survey dataframe. You can view the rows matching a given species using
the same square brackets we used above to select specific columns and
rows. Here, however, instead of passing a value or list of values, we
will pass a conditional.

A *conditional* is a statement that evaluates as either True or False.
They often make use of inequality operators, for example:

-   `==` for equals
-   `!=` for does not equal
-   `>` for greater than
-   `>=` for greater than or equal to
-   `<` for less than
-   `<=` for less than or equal to

Examples of conditional statements include:

-   `"a" == "b"'` evaluates False
-   `"a" != b"` evaluates True
-   `3 > 4` evaluates False

::: callout ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

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
       record_id  month  day  year  ...  sex hindfoot_length_mm weight_g  weight_mg
2              3      7   16  1977  ...    F               37.0      NaN        NaN
3              4      7   16  1977  ...    M               36.0      NaN        NaN
4              5      7   16  1977  ...    M               35.0      NaN        NaN
7              8      7   16  1977  ...    M               37.0      NaN        NaN
8              9      7   16  1977  ...    F               34.0      NaN        NaN
...          ...    ...  ...   ...  ...  ...                ...      ...        ...
35532      35533     12   31  2002  ...    F               36.0     48.0    48000.0
35533      35534     12   31  2002  ...    M               37.0     56.0    56000.0
35534      35535     12   31  2002  ...    M               37.0     53.0    53000.0
35535      35536     12   31  2002  ...    F               35.0     42.0    42000.0
35536      35537     12   31  2002  ...    F               36.0     46.0    46000.0

[10596 rows x 10 columns]
```

To limit our results to observations made in or after 2000, use:


```python
surveys[surveys["year"] >= 2000]
```

```{.output}
       record_id  month  day  ...  hindfoot_length_mm  weight_g weight_mg
30158      30159      1    8  ...                22.0      17.0   17000.0
30159      30160      1    8  ...                35.0      53.0   53000.0
30160      30161      1    8  ...                21.0      17.0   17000.0
30161      30162      1    8  ...                36.0      50.0   50000.0
30162      30163      1    8  ...                20.0      16.0   16000.0
...          ...    ...  ...  ...                 ...       ...       ...
35544      35545     12   31  ...                 NaN       NaN       NaN
35545      35546     12   31  ...                 NaN       NaN       NaN
35546      35547     12   31  ...                15.0      14.0   14000.0
35547      35548     12   31  ...                36.0      51.0   51000.0
35548      35549     12   31  ...                 NaN       NaN       NaN

[5391 rows x 10 columns]
```

As with `rename()` above, each filtering operation returns a copy of the
dataframe. We will look at how to make changes to the original dataframe
at the end of this lesson.

## Building more complex queries

You can combine conditionals using *bitwise operators*:

-   `&`: True if conditions on both sides of the operator are True
-   `|`: True if a condition on either side is True

To return all observations of DM in or after 2000, we can combine the
two conditionals we used previously. Note that, when joining
conditionals using `&` or `|`, you should wrap each condition in
parentheses. If you omit the parentheses, `pandas` will not perform the
comparisons in the expected order.


```python
surveys[(surveys["species_id"] == "DM") & (surveys["year"] >= 2000)]
```

```{.output}
       record_id  month  day  year  ...  sex hindfoot_length_mm weight_g  weight_mg
30161      30162      1    8  2000  ...    M               36.0     50.0    50000.0
30178      30179      1    8  2000  ...    M               36.0     60.0    60000.0
30195      30196      1    8  2000  ...    M               37.0     52.0    52000.0
30196      30197      1    8  2000  ...    F               34.0     43.0    43000.0
30209      30210      1    8  2000  ...    M               38.0     56.0    56000.0
...          ...    ...  ...   ...  ...  ...                ...      ...        ...
35532      35533     12   31  2002  ...    F               36.0     48.0    48000.0
35533      35534     12   31  2002  ...    M               37.0     56.0    56000.0
35534      35535     12   31  2002  ...    M               37.0     53.0    53000.0
35535      35536     12   31  2002  ...    F               35.0     42.0    42000.0
35536      35537     12   31  2002  ...    F               36.0     46.0    46000.0

[847 rows x 10 columns]
```

`pandas` also provides methods that can be used for filtering. One
example is `isin()`, which is used to match a list of values. This
method can be combined with other conditionals as above. The example
below returns rows from 2000 or later with either "DM", "DO", or "DS" in
the species_id column:


```python
surveys[surveys["species_id"].isin(["DM", "DO", "DS"]) & (surveys["year"] >= 2000)]
```

```{.output}
       record_id  month  day  year  ...  sex hindfoot_length_mm weight_g  weight_mg
30159      30160      1    8  2000  ...    M               35.0     53.0    53000.0
30161      30162      1    8  2000  ...    M               36.0     50.0    50000.0
30166      30167      1    8  2000  ...    M               35.0     41.0    41000.0
30170      30171      1    8  2000  ...    M               36.0     52.0    52000.0
30172      30173      1    8  2000  ...    F               35.0     54.0    54000.0
...          ...    ...  ...   ...  ...  ...                ...      ...        ...
35533      35534     12   31  2002  ...    M               37.0     56.0    56000.0
35534      35535     12   31  2002  ...    M               37.0     53.0    53000.0
35535      35536     12   31  2002  ...    F               35.0     42.0    42000.0
35536      35537     12   31  2002  ...    F               36.0     46.0    46000.0
35547      35548     12   31  2002  ...    M               36.0     51.0    51000.0

[1268 rows x 10 columns]
```

## Sorting

You can sort a dataframe using the `sort_values()` method. For this
example, we'll work from the subset defined above. First we need to
assign that query to a variable:


```python
results = surveys[
    surveys["species_id"].isin(["DM", "DO", "DS"]) & (surveys["year"] >= 2000)
]
```

Now we'll sort results by `weight_g`. To do so, pass that column name as
an argument (that is, inside the trailing parentheses) to the
`sort_values()` method:


```python
results.sort_values("weight_g")
```

```{.output}
       record_id  month  day  year  ...  sex hindfoot_length_mm weight_g  weight_mg
30614      30615      4   30  2000  ...    M               34.0     18.0    18000.0
34790      34791     10    5  2002  ...    M               34.0     20.0    20000.0
32782      32783      9   23  2001  ...    M               34.0     21.0    21000.0
32650      32651      9   22  2001  ...    F               33.0     21.0    21000.0
34345      34346      6   16  2002  ...    M               34.0     22.0    22000.0
...          ...    ...  ...   ...  ...  ...                ...      ...        ...
34724      34725      9   10  2002  ...    M               38.0      NaN        NaN
34950      34951     10    6  2002  ...    F               36.0      NaN        NaN
35088      35089     11   10  2002  ...    F               35.0      NaN        NaN
35387      35388     12   29  2002  ...    M               35.0      NaN        NaN
35485      35486     12   29  2002  ...    M               37.0      NaN        NaN

[1268 rows x 10 columns]
```

By default, rows are sorted in *ascending* order (smallest to largest).
You can modify this behavior using the ascending keyword argument:


```python
results.sort_values("weight_g", ascending=False)
```

```{.output}
       record_id  month  day  year  ...  sex hindfoot_length_mm weight_g  weight_mg
31955      31956      4   21  2001  ...    F               36.0     76.0    76000.0
31942      31943      4   21  2001  ...    F               37.0     68.0    68000.0
32041      32042      5   26  2001  ...    F               37.0     68.0    68000.0
30441      30442      3    4  2000  ...    F                NaN     66.0    66000.0
35159      35160     11   10  2002  ...    F               36.0     65.0    65000.0
...          ...    ...  ...   ...  ...  ...                ...      ...        ...
34724      34725      9   10  2002  ...    M               38.0      NaN        NaN
34950      34951     10    6  2002  ...    F               36.0      NaN        NaN
35088      35089     11   10  2002  ...    F               35.0      NaN        NaN
35387      35388     12   29  2002  ...    M               35.0      NaN        NaN
35485      35486     12   29  2002  ...    M               37.0      NaN        NaN

[1268 rows x 10 columns]
```

You can sort on multiple fields at once by passing a list of column
names. You can control how each column sorts by passing a list of the
same length to the ascending keyword:


```python
results.sort_values(["species_id", "weight_g"], ascending=[True, False])
```

```{.output}
       record_id  month  day  ...  hindfoot_length_mm  weight_g weight_mg
34126      34127      5   16  ...                35.0      64.0   64000.0
30178      30179      1    8  ...                36.0      60.0   60000.0
31858      31859      3   24  ...                36.0      60.0   60000.0
32909      32910     10   14  ...                37.0      60.0   60000.0
34604      34605      7   14  ...                36.0      60.0   60000.0
...          ...    ...  ...  ...                 ...       ...       ...
33960      33961      5   15  ...                36.0       NaN       NaN
34072      34073      5   16  ...                34.0       NaN       NaN
34437      34438      7   13  ...                 NaN       NaN       NaN
35387      35388     12   29  ...                35.0       NaN       NaN
35485      35486     12   29  ...                37.0       NaN       NaN

[1268 rows x 10 columns]
```

As with the dataframe methods above, `sort_values()` returns a copy of
the original dataframe and leaves the original untouched.

::: challenge ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Write a query that returns year, species_id, and weight in kg from the
surveys table, sorted with the largest weights at the top.

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


```python
# Create a new column with weight in kg
surveys["weight_kg"] = surveys["weight_g"] / 1000

# Create a subset containing only year, species_id, and weight_kg
subset = surveys[["year", "species_id", "weight_kg"]]

# Sort the subset by weight_kg
subset = subset.sort_values("weight_kg", ascending=False)

subset
```

```{.output}
       year species_id  weight_kg
33048  2001         NL      0.280
12870  1987         NL      0.278
15458  1989         NL      0.275
2132   1979         NL      0.274
12728  1987         NL      0.270
...     ...        ...        ...
35530  2002         PB        NaN
35543  2002         US        NaN
35544  2002         AH        NaN
35545  2002         AH        NaN
35548  2002        NaN        NaN

[35549 rows x 3 columns]
```

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## Modifying data

We've already shown how to modify an existing a dataframe by adding a
new column. What if we want to modify existing cells instead? As we've
seen, this can be a little tricky in `pandas` because most of its
methods return a copy of the original dataframe. For example, you can
easily look at subsets of a dataframe using square brackets. The cell
below returns the species_id column for rows 2 through 5:


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
Say we want to set the species_id column to a new value, "CAT". Try
running the code in the cell below:


```python
surveys[2:6]["species_id"] = "CAT"
```

```{.output}
<string>:1: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
```

You should have received a `SettingWithCopyWarning` warning after
running that cell. This warning tells you that the data in the original
dataframe has not been modified. This is because the square brackets
returned a copy, meaning that any changes will be reflected in the copy,
not the original. We can verify that the original dataframe has not been
changed by displaying the rows that would have been affected by this
changed:


```python
surveys[2:6]
```

```{.output}
   record_id  month  day  ...  weight_g  weight_mg weight_kg
2          3      7   16  ...       NaN        NaN       NaN
3          4      7   16  ...       NaN        NaN       NaN
4          5      7   16  ...       NaN        NaN       NaN
5          6      7   16  ...       NaN        NaN       NaN

[4 rows x 11 columns]
```

### Using loc to modify existing cells

One way to modify existing data in `pandas` is to use the `loc`
attribute. This attribute allows you to extract and modify cells in a
DataFrame using the following syntax: `df.loc[row_indexer,
col_indexer]`.

The *row_indexer* argument is used to select one or more rows. It can
be:

-   A row label (i.e., the bold column on the far left)
    -   `0` returns the row with label 0

-   A slice including multiple rows:
    -   `:` returns all rows
    -   `:2` returns all rows from the beginning of the
        dataframe to the row labeled 2, *inclusive*
    -   `2:` returns all rows from the row labeled 2 to the end
        of the dataframe, *inclusive*
    -   `2:5` returns all rows between those labeled 2 and 5,
        *inclusive*

-   A conditional, as in the examples above.

The *col_indexer* argument is used to select one or more columns. It
will typically be a list of column names and can be omitted, in which
case all columns will be returned.

::: callout ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

The row labels in this dataframe happen to be numeric and aligned
exactly to the row's index (so for the first row both the index and the
label are 0, for the second row both the index and the label are 1,
etc.) This is often **but not always** true in pandas. For example, if
we used record_id as the label, the row labels would be one-based and
the row indexes would be zero-based.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: callout ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Slices using `loc` are inclusive--rows matching both the start and end
values are included in the returned slice. This differs from list
slices, where the start but not end value is included in the slice.
`loc` works this way because it is looking at the row *label*, not the
row *index*.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

We'll be making some changes to our data, so let's work from a copy
instead of modifying the original:


```python
surveys_copy = surveys.copy()
```

To select a subset of rows and columns using `loc`, use:


```python
surveys_copy.loc[
    2:5, "species_id"
]  # note that we use 2:5 with loc (end index included)
```

```{.output}
2    DM
3    DM
4    DM
5    PF
Name: species_id, dtype: object
```

Unlike the methods earlier in the lesson, this is a view, not a copy, of
the data in the surveys_copy dataframe. We can now assign a new value to
the species_id column in the matching rows of the original dataframe:


```python
surveys_copy.loc[2:5, "species_id"] = "CAT"
```

We can see that these changes are reflected in the original surveys_copy
object:


```python
surveys_copy.loc[1:6, "species_id"]
```

```{.output}
1     NL
2    CAT
3    CAT
4    CAT
5    CAT
6     PE
Name: species_id, dtype: object
```

::: callout ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

`pandas` provides another indexer, `iloc`, that allows you to select and
modify data using row and column indexes instead of labels. Learn more
in the [`pandas` documentation](https://pandas.pydata.org/pandas-
docs/stable/reference/api/pandas.DataFrame.iloc.html).

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
