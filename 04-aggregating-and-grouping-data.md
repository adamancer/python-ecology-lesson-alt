---
title: Aggregating and Grouping Data
---

::: questions ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   How do we calculate statistics using pandas?
-   How do we group data using pandas?
-   How do null values affect calculations using pandas?

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: objectives :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   Introduce aggregation calculations in pandas
-   Introduce grouping in pandas
-   Learn about how pandas handles null values

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

As always, we'll begin by importing pandas and reading our CSV:


```python
import pandas as pd

surveys = pd.read_csv("data/surveys.csv")
```

## Aggregating data

Aggregation allows us to combine results by grouping records based on
value. It is also useful for calculating combined values in groups.

Let’s go to the surveys table and find out how many observations are
in our dataset. We've already seen that we can use the `info()` method
to get high-level about the dataset, including the number of entries.
What if just wanted the number of rows? In that case, we can use the
built-in function `len()`, which is used to calculate the number of
items in an object (for example, the number of characters in a string or
the number of items in a list). When used on a dataframe, `len()`
returns the number of rows:


```python
len(surveys)
```

```{.output}
35549
```

`pandas` also provides a suite of aggregation methods. For example, we
can find out the total weight of all the individuals in grams using
`sum()`:


```python
surveys["weight"].sum()
```

```{.output}
1377594.0
```

Other aggregation methods supported by pandas include `min()`, `max()`,
and `mean()`.

::: challenge ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Calculate the total weight, average weight, minimum and maximum weights
for all animals caught over the duration of the survey. Can you modify
your code so that it outputs these values only for weights between 5 and
10 grams?

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


```python
# Create a subset of only the animals between 5 and 10 grams
weights = surveys[(surveys["weight"] > 5) & (surveys["weight"] < 10)]["weight"]

# Display aggregation calculations using a dict
{
    "sum": weights.sum(),
    "mean": weights.mean(),
    "min": weights.min(),
    "max": weights.max(),
}
```

```{.output}
{'sum': 16994.0, 'mean': 7.91523055426176, 'min': 6.0, 'max': 9.0}
```

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

To quickly generate summary statistics, we can use the `describe()`
method. When you use this method on a dataframe, it calculates stats for
all columns with numeric data:


```python
surveys.describe()
```

```{.output}
          record_id         month  ...  hindfoot_length        weight
count  35549.000000  35549.000000  ...     31438.000000  32283.000000
mean   17775.000000      6.477847  ...        29.287932     42.672428
std    10262.256696      3.396925  ...         9.564759     36.631259
min        1.000000      1.000000  ...         2.000000      4.000000
25%     8888.000000      4.000000  ...        21.000000     20.000000
50%    17775.000000      6.000000  ...        32.000000     37.000000
75%    26662.000000     10.000000  ...        36.000000     48.000000
max    35549.000000     12.000000  ...        70.000000    280.000000

[8 rows x 7 columns]
```

You can see that `describe()` isn't picky: It includes both ID and date
columns in its results. Notice also that the counts differ in between
columns. This is because `count()` only counts non-NaN rows.

If you prefer, you can also describe a single column at a time:


```python
surveys["weight"].describe()
```

```{.output}
count    32283.000000
mean        42.672428
std         36.631259
min          4.000000
25%         20.000000
50%         37.000000
75%         48.000000
max        280.000000
Name: weight, dtype: float64
```

If you need more control over the output (for example, if you want to
calculate the total weight of all animals, as in the challenge above),
pandas provides the `agg()` method:


```python
surveys.agg({"weight": ["sum", "mean", "min", "max"]})
```

```{.output}
            weight
sum   1.377594e+06
mean  4.267243e+01
min   4.000000e+00
max   2.800000e+02
```

## Grouping data

Now, let’s see how many individuals were counted in each species. We
do this using `groupby()`, which creates an object similar to a
dataframe where rows are grouped by the data in one or more columns:


```python
grouped = surveys.groupby("species_id")
```

When we aggregate the grouped data, `pandas` provides separate
calculations for each member of the group. In the example below, we'll
calculate the number of times each species appears in the dataset:


```python
grouped["species_id"].count()
```

```{.output}
species_id
AB      303
AH      437
AS        2
BA       46
CB       50
CM       13
CQ       16
CS        1
CT        1
CU        1
CV        1
DM    10596
DO     3027
DS     2504
DX       40
NL     1252
OL     1006
OT     2249
OX       12
PB     2891
PC       39
PE     1299
PF     1597
PG        8
PH       32
PI        9
PL       36
PM      899
PP     3123
PU        5
PX        6
RF       75
RM     2609
RO        8
RX        2
SA       75
SC        1
SF       43
SH      147
SO       43
SS      248
ST        1
SU        5
UL        4
UP        8
UR       10
US        4
ZL        2
Name: species_id, dtype: int64
```

::: challenge ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Write statements that return:

1.  How many individuals were counted in each year in total
2.  How many were counted each year, for each different species
3.  The average weights of each species in each year
4.  How many individuals were counted for each species that was
    observed more than 10 times

Can you get the answer to both 2 and 3 in a single query?

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### Show me the solution to challenge 1


```python
# Individual counts per year
surveys.groupby("year")["record_id"].count()
```

```{.output}
year
1977     503
1978    1048
1979     719
1980    1415
1981    1472
1982    1978
1983    1673
1984     981
1985    1438
1986     942
1987    1671
1988    1469
1989    1569
1990    1311
1991    1347
1992    1038
1993     750
1994     668
1995    1222
1996    1706
1997    2493
1998    1610
1999    1135
2000    1552
2001    1610
2002    2229
Name: record_id, dtype: int64
```

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### Show me the solution to challenge 2


```python
# Individual counts by species and year
surveys.groupby(["year", "species_id"])["record_id"].count()
```

```{.output}
year  species_id
1977  DM            264
      DO             12
      DS             98
      NL             31
      OL             10
                   ... 
2002  SF              7
      SH             11
      SS              9
      UR              1
      US              4
Name: record_id, Length: 509, dtype: int64
```

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### Show me the solution to challenge 3


```python
# Mean weight by species and year
surveys.groupby(["year", "species_id"])["weight"].mean()
```

```{.output}
year  species_id
1977  DM             41.141304
      DO             42.666667
      DS            121.437500
      NL                   NaN
      OL             21.666667
                       ...    
2002  SF             62.166667
      SH             64.666667
      SS                   NaN
      UR                   NaN
      US                   NaN
Name: weight, Length: 509, dtype: float64
```

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### Show me the solution to challenge 4


```python
# Counts by species that appear more than 10 times
species = surveys.groupby("species_id")["record_id"].count()
species[species > 10]
```

```{.output}
species_id
AB      303
AH      437
BA       46
CB       50
CM       13
CQ       16
DM    10596
DO     3027
DS     2504
DX       40
NL     1252
OL     1006
OT     2249
OX       12
PB     2891
PC       39
PE     1299
PF     1597
PH       32
PL       36
PM      899
PP     3123
RF       75
RM     2609
SA       75
SF       43
SH      147
SO       43
SS      248
Name: record_id, dtype: int64
```

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### Show me the solution to challenges 2 and 3 combined


```python
# Counts and mean weight by species and year
surveys.groupby(["year", "species_id"]).agg({"record_id": "count", "weight": "mean"})
```

```{.output}
                 record_id      weight
year species_id                       
1977 DM                264   41.141304
     DO                 12   42.666667
     DS                 98  121.437500
     NL                 31         NaN
     OL                 10   21.666667
...                    ...         ...
2002 SF                  7   62.166667
     SH                 11   64.666667
     SS                  9         NaN
     UR                  1         NaN
     US                  4         NaN

[509 rows x 2 columns]
```

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## Handling missing data

You may have noticed that some columns in the surveys dataframe have the
value NaN instead of text or numbers. NaN, short for "not a number," is
a special type of float used by pandas to represent missing data. When
reading from a CSV, as we have done throughout this lesson, pandas
interprets certains values as NaN (see *na_values* in the [pd.read_csv()
documentation](https://pandas.pydata.org/pandas-
docs/stable/reference/api/pandas.read_csv.html) for the default list).
NaNs are excluded from most aggregation calculations in `pandas`,
including counts.

It is crucial to understand how missing data is represented in your
dataset. Failing to do so may introduce errors into your analysis. The
ecology dataset used in this lesson uses empty cells to represent
missing data, but other disciplines have different conventions. For
example, some geographic datasets use -9999 to represent null values.
Failure to convert that value to NaN would produce significant errors in
any calculations performed on that dataset.
