---
title: Aggregating Data
teaching: 60
exercises: 0
---

::: questions ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   How do we calculate summary statistics?
-   How do we group data?
-   How do null values affect calculations?

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: objectives :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   Introduce aggregation calculations in pandas
-   Introduce grouping in pandas
-   Learn about how pandas handles null values
-   Make a boxplot showing summary stats

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

In the previous lesson, we saw how to access and filter our dataframe.
Here, we'll use pandas to calculate summary statistics for some of that
data.

As always, we'll begin by importing pandas and reading our CSV:

```python
import pandas as pd

surveys = pd.read_csv("data/surveys.csv")
```

## Aggregating data

Aggregation allows us to describe the data in our dataframe by
calculating totals (like the number of records) and statistics (like the
mean value of a column). Pandas allows us to run these calculations on
dataframes or on subsets of interest.

Suppose we want to know how many records are in our dataset. We've
already seen that we can use the `info()` method to get high-level about
the dataset, including the number of entries. What if just wanted the
number of rows? One approach is to use the built-in function `len()`,
which is used to count the number of items in an object (for example,
the number of characters in a string or the number of items in a list).
When used on a dataframe, `len()` returns the number of rows:

```python
len(surveys)
```

```{.output}
35549
```

Pandas provides a suite of aggregation methods that go beyond this
simple case. For example, we can count the number of non-NaN values in
each column using `count()`:

```python
surveys.count()
```

```{.output}
record_id          35549
month              35549
day                35549
year               35549
plot_id            35549
species_id         34786
sex                33038
hindfoot_length    31438
weight             32283
dtype: int64
```

Or we can find out the total weight of all individuals using `sum()`:

```python
surveys["weight"].sum()
```

```{.output}
np.float64(1377594.0)
```

Other aggregation methods supported by pandas include `min()`, `max()`,
and `mean()`. These methods all ignore NaNs, so missing data does not
affect the calculations.

::: challenge ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Calculate the total weight, average weight, minimum and maximum weights
for all animals observed during the survey. Can you modify your code so
that it outputs these values only for weights between 5 and 10 grams?

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
{'sum': np.float64(16994.0),
 'mean': np.float64(7.91523055426176),
 'min': np.float64(6.0),
 'max': np.float64(9.0)}
```

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

To quickly generate summary statistics, we can use the `describe()`
method instead of calling each aggregation method separately. When we
use this method on a dataframe, it calculates stats for all columns with
numeric data:

```python
surveys.describe()
```

```{.output}
```

<style>
  table.dataframe { display: block; overflow-x: auto; white-space: nowrap; }
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
      <th>hindfoot_length</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>35549.000000</td>
      <td>35549.000000</td>
      <td>35549.000000</td>
      <td>35549.000000</td>
      <td>35549.000000</td>
      <td>31438.000000</td>
      <td>32283.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>17775.000000</td>
      <td>6.477847</td>
      <td>15.991195</td>
      <td>1990.475231</td>
      <td>11.397001</td>
      <td>29.287932</td>
      <td>42.672428</td>
    </tr>
    <tr>
      <th>std</th>
      <td>10262.256696</td>
      <td>3.396925</td>
      <td>8.257366</td>
      <td>7.493355</td>
      <td>6.799406</td>
      <td>9.564759</td>
      <td>36.631259</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1977.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>8888.000000</td>
      <td>4.000000</td>
      <td>9.000000</td>
      <td>1984.000000</td>
      <td>5.000000</td>
      <td>21.000000</td>
      <td>20.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>17775.000000</td>
      <td>6.000000</td>
      <td>16.000000</td>
      <td>1990.000000</td>
      <td>11.000000</td>
      <td>32.000000</td>
      <td>37.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>26662.000000</td>
      <td>10.000000</td>
      <td>23.000000</td>
      <td>1997.000000</td>
      <td>17.000000</td>
      <td>36.000000</td>
      <td>48.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>35549.000000</td>
      <td>12.000000</td>
      <td>31.000000</td>
      <td>2002.000000</td>
      <td>24.000000</td>
      <td>70.000000</td>
      <td>280.000000</td>
    </tr>
  </tbody>
</table>

You can see that `describe()` isn't picky: It includes the ID, year,
month, and day columns in its results. Notice also that counts differ in
between columns. This is because `count()` only counts non-NaN rows.

If desired, we can also describe a single column at a time:

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

If we need more control over the output (for example, if we want to
calculate the total weight of all animals, as in the challenge above),
pandas provides the `agg()` method, which allows us to specify
aggregation methods by column. This method requires a `dict`, which is a
built-in data type that we have not discussed yet.

Like a `list`, a `dict` is a container that can include more than one
object. Where as a `list` is a sequence, a `dict` is a mapping
consisting of *keys* that map to *values*. Because it is built in, it
can be used in any Python application without having to import anything.

Let's see what that looks like in practice by defining a `dict` that
maps lowercase to uppercase letters. We use curly braces to define a
`dict`. The parts of each item are separated by a colon, with the key on
the left and the value on the right.

```python
letters = {"a": "A", "b": "B", "c": "C"}
```

To retrieve the value for a given key, we use square brackets:

```python
letters["a"]
```

```{.output}
'A'
```

There are many other ways to interact with a `dict`. We can add or
delete items, remap a key to a new value, or iterate over all the keys,
values, or items inside. Use `help()` or check out [the Python
docs](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
to learn more about `dict`.

Now let's return to the calculating summary statistics using `agg()`.
For this method, Each key must be a column name and each value a list of
the names of aggregation methods.

To calculate the total weight, mean weight, and mean hindfoot length of
all records in the survey, we can use:

```python
surveys.agg({"weight": ["sum", "mean"], "hindfoot_length": ["mean"]})
```

```{.output}
```

<style>
  table.dataframe { display: block; overflow-x: auto; white-space: nowrap; }
  table.dataframe tbody tr:hover { background-color: #ccffff !important; }
  table.dataframe tr:nth-child(even) { background-color: #f5f5f5; }
  table.dataframe th { text-align: right; font-weight: bold; }
  table.dataframe td { text-align: right; }
</style>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>weight</th>
      <th>hindfoot_length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>sum</th>
      <td>1.377594e+06</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>4.267243e+01</td>
      <td>29.287932</td>
    </tr>
  </tbody>
</table>

## Grouping data

Up to now, we have been calculating statistics based on all records in
the dataframe, but the dataset includes a variety of species, each with
a characteristic size and number of observations. We may find it useful
to look at subsets for individual species (or plots, years, etc.). We
can do so using the `groupby()` method, which groups records based on
the data in one or more columns. To group by species_id, use:

```python
surveys.groupby("species_id")
```

```{.output}
```

<pandas.core.groupby.generic.DataFrameGroupBy object at 0x7f287e31d6a0>

The `groupby()` methods returns a special object that includes the rows
associated with each species_id, but we wouldn't know that based on the
output of the previous cell. Instead of a table or another view of the
grouped records, the method outputs a string with the type of object
(`pandas.core.groupby.generic.DataFrameGroupBy`) and some information
about where that object is stored (`0x0...`). Not the most useful thing
in the world! We might encounter strings like this when developers
determine that there is no concise, human-readable way to represent an
object.

Nevertheless, we can use the `DataFrameGroupBy` object to calculate
summary statistics for each group. In the example below, we'll calculate
the number of times each species appears in the dataset. To simplify the
output, we'll limit the count to a single column, species_id, using
square brackets. (Because `count()` excludes NaNs, it's usually a good
practice to choose a column that does not contain missing data. Record
ID fields are a good choice, but any field that is populated for every
row will work.)

```python
surveys.groupby("species_id")["species_id"].count()
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

To group by multiple columns, we can pass a list to `groupby()`. To
determine how many observations of each species were made in each year,
we can use:

```python
surveys.groupby(["species_id", "year"])["record_id"].count()
```

```{.output}
species_id  year
AB          1980     5
            1981     7
            1982    34
            1983    41
            1984    12
                    ..
UR          1994     1
            2001     2
            2002     1
US          2002     4
ZL          1988     2
Name: record_id, Length: 509, dtype: int64
```

::: challenge ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Write statements to answer the following questions:

1.  How many individuals were counted in each year in total?
2.  How many were counted each year, for each different species?
3.  What was the average weight of each species in each year?
4.  How many individuals were counted for each species that was observed
    more than 10 times?

Can you get the answer to both 2 and 3 in a single query?

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### Show me the solution to challenge 1

How many individuals were counted in each year in total?

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

How many individuals were counted each year for each different species?

```python
# Individual counts by species and year
result = surveys.groupby(["year", "species_id"])["record_id"].count()

# Use the option_context context manager to show all rows
with pd.option_context("display.max_rows", None):
    print(result)
```

```{.output}
year  species_id
1977  DM            264
      DO             12
      DS             98
      NL             31
      OL             10
      OT             17
      OX              7
      PE              6
      PF             31
      PP              7
      RM              2
      SH              1
      SS              1
1978  AH              1
      DM            389
      DO             22
      DS            320
      NL             48
      OL             47
      OT             66
      OX              1
      PE             17
      PF             40
      PM              3
      PP             24
      RM              3
      SA              2
      SH              1
      SS              8
1979  DM            209
      DO             31
      DS            204
      NL             30
      OL             46
      OT             68
      PE             17
      PF             19
      PM              6
      PP             20
      RM              6
      SS              2
1980  AB              5
      CB              1
      CM             12
      CQ              2
      DM            493
      DO             89
      DS            346
      DX              1
      NL             57
      OL             85
      OT             96
      PE             20
      PF             95
      PM              1
      PP             17
      RM             46
      SS              9
1981  AB              7
      CB              1
      CQ              4
      DM            559
      DO            123
      DS            354
      NL             63
      OL             55
      OT             65
      PE             43
      PF             59
      PM             16
      PP             20
      RM             29
      SA             11
      SS              8
1982  AB             34
      AH              1
      CQ              8
      DM            609
      DO            117
      DS            354
      NL            111
      OL             83
      OT             94
      OX              1
      PC              2
      PE            107
      PF            152
      PM             72
      PP             32
      RF              2
      RM            154
      SA             17
      SH              2
      SS             12
1983  AB             41
      AH              2
      CB              3
      DM            528
      DO            167
      DS            280
      DX              1
      NL             98
      OL             65
      OT             86
      PC              3
      PE             38
      PF            114
      PG              1
      PM             42
      PP             32
      RM            127
      SA             10
      SH              2
      SS             12
1984  AB             12
      AH              2
      CB              1
      CQ              2
      DM            396
      DO            108
      DS             76
      NL             64
      OL             71
      OT             49
      OX              1
      PE             20
      PF              7
      PH              7
      PM             12
      PP             26
      PU              2
      RM             60
      SA             20
      SS             15
1985  AB             14
      AH             14
      CB              1
      DM            667
      DO            225
      DS             98
      NL             45
      OL             94
      OT             62
      PE             51
      PF              1
      PH              3
      PM             17
      PP             35
      RM             72
      SA              3
      SS             14
1986  AB              5
      AH             19
      CB              4
      DM            406
      DO            115
      DS             88
      DX              1
      NL             60
      OL             43
      OT             25
      PE             26
      PF              2
      PH              1
      PM             34
      PP             26
      RM             53
      SA              1
      SH              1
      SS             12
1987  AB             35
      AH             41
      CB              5
      CM              1
      CV              1
      DM            469
      DO            213
      DS            104
      NL            128
      OL             79
      OT             43
      PC              5
      PE            142
      PF              4
      PM            133
      PP             45
      RM            189
      SA              1
      SH              5
      SS             20
      UP              2
      UR              3
1988  AB             39
      AH             26
      CB              6
      DM            365
      DO            144
      DS             54
      DX              1
      NL            102
      OL             51
      OT             86
      PE            190
      PF              2
      PG              2
      PH              1
      PM             54
      PP             53
      RF             11
      RM            211
      SA              1
      SH             31
      SS             20
      UL              1
      UP              3
      UR              1
      ZL              2
1989  AB             31
      AH             30
      BA              3
      CB              1
      CS              1
      DM            321
      DO            119
      DS             33
      NL             67
      OL             57
      OT            102
      OX              1
      PC              1
      PE            177
      PF             13
      PH              2
      PM             27
      PP             45
      RF             49
      RM            398
      SA              3
      SC              1
      SF              5
      SH             55
      SS             18
      UP              2
1990  AB             27
      AH             22
      BA             11
      DM            462
      DO            171
      DS             17
      NL             29
      OL             25
      OT             77
      PC              8
      PE             75
      PF             51
      PG              4
      PH              7
      PP             34
      RF             12
      RM            231
      SF             18
      SH              9
      SS              5
      UP              1
1991  AB             15
      AH             21
      AS              1
      BA             26
      CB              2
      DM            404
      DO            122
      DS             11
      DX              4
      NL             30
      OL             36
      OT            107
      PC              6
      PE             65
      PF             62
      PP             88
      RM            307
      RO              1
      SA              2
      SF              7
      SH              1
      SO             11
      SS              2
      UR              1
1992  AB             10
      AH             16
      BA              6
      CB              7
      DM            307
      DO             94
      DS             18
      DX             12
      NL             15
      OL             45
      OT             42
      PC              9
      PE             41
      PF             57
      PH              7
      PI              1
      PP            131
      RM            158
      SF              3
      SO             20
      SS              7
      UL              1
      UR              1
1993  AB              9
      AH             15
      AS              1
      CB              5
      CU              1
      DM            253
      DO             29
      DS             18
      DX              3
      NL             24
      OL             35
      OT             22
      OX              1
      PC              1
      PE             13
      PF             70
      PP            100
      RM            103
      SF              3
      SO              6
      SS              1
      ST              1
1994  AB              7
      AH             19
      CB              1
      DM            293
      DO             25
      DS              9
      DX              2
      NL             10
      OL             21
      OT             21
      PC              1
      PE              3
      PF             73
      PP             74
      PU              2
      RM             40
      SO              3
      SS              7
      SU              1
      UL              2
      UR              1
1995  AB              4
      AH             36
      CB              2
      DM            436
      DO             58
      DX              3
      NL              8
      OL             29
      OT             38
      PB              7
      PC              1
      PE             14
      PF            158
      PH              3
      PI              1
      PL              3
      PM              8
      PP            277
      PU              1
      RM             81
      RX              1
      SS              7
      SU              4
1996  AH             25
      DM            492
      DO            174
      DX              1
      NL              7
      OL             13
      OT            108
      PB             39
      PC              1
      PE             36
      PF            330
      PL              6
      PM             50
      PP            298
      PX              2
      RM             90
      SA              1
      SS             16
1997  AH             37
      CB              3
      DM            576
      DO            253
      DS              6
      NL             48
      OL              8
      OT            258
      PB            259
      PE             57
      PF            186
      PH              1
      PL             19
      PM            271
      PP            325
      PX              2
      RF              1
      RM            158
      RX              1
      SA              1
      SH              7
      SO              3
      SS             12
1998  AB              2
      AH             33
      CB              4
      CT              1
      DM            503
      DO            111
      DS              9
      DX              2
      NL             32
      OT            164
      PB            329
      PC              1
      PE             24
      PF             26
      PL              7
      PM            103
      PP            208
      PX              1
      RM             13
      SA              2
      SS             15
1999  AH             14
      DM            348
      DO             84
      DS              7
      DX              3
      NL             20
      OT            105
      PB            272
      PE              7
      PM             44
      PP            167
      RM             28
      SH              2
      SS              7
2000  AB              3
      AH             12
      DM            233
      DO             91
      DX              4
      NL             29
      OT            154
      PB            555
      PE             15
      PG              1
      PL              1
      PM              2
      PP            381
      PX              1
      RM             15
      SH              8
      SS              4
2001  AB              1
      AH             23
      CB              3
      DM            305
      DO             81
      DX              1
      NL             48
      OT            167
      PB            538
      PE             35
      PF             27
      PI              2
      PM              3
      PP            273
      RM             15
      SH             11
      SS              5
      UR              2
2002  AB              2
      AH             28
      DM            309
      DO            249
      DX              1
      NL             48
      OL              8
      OT            127
      PB            892
      PE             60
      PF             18
      PI              5
      PM              1
      PP            385
      RM             20
      RO              7
      SF              7
      SH             11
      SS              9
      UR              1
      US              4
Name: record_id, dtype: int64

```

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### Show me the solution to challenge 3

What was the average weight of each species in each year?

```python
# Mean weight by species and year
result = surveys.groupby(["year", "species_id"])["weight"].mean()

# Use the option_context context manager to show all rows
with pd.option_context("display.max_rows", None):
    print(result)
```

```{.output}
year  species_id
1977  DM             41.141304
      DO             42.666667
      DS            121.437500
      NL                   NaN
      OL             21.666667
      OT             21.000000
      OX             21.333333
      PE             19.500000
      PF              7.173913
      PP             15.333333
      RM             10.000000
      SH                   NaN
      SS                   NaN
1978  AH                   NaN
      DM             40.795455
      DO             45.000000
      DS            115.198653
      NL            184.656250
      OL             31.027027
      OT             23.220000
      OX                   NaN
      PE             20.428571
      PF              7.088235
      PM             20.666667
      PP             14.869565
      RM              7.500000
      SA                   NaN
      SH             89.000000
      SS            130.000000
1979  DM             43.507317
      DO             45.862069
      DS            111.796954
      NL            138.000000
      OL             33.717391
      OT             23.075758
      PE             20.529412
      PF              7.529412
      PM             23.666667
      PP             15.105263
      RM              8.333333
      SS                   NaN
1980  AB                   NaN
      CB                   NaN
      CM                   NaN
      CQ                   NaN
      DM             44.136082
      DO             48.058824
      DS            120.725664
      DX                   NaN
      NL            158.982143
      OL             33.107143
      OT             24.083333
      PE             22.450000
      PF              7.455556
      PM             21.000000
      PP             14.176471
      RM             10.227273
      SS                   NaN
1981  AB                   NaN
      CB                   NaN
      CQ                   NaN
      DM             44.032907
      DO             49.111111
      DS            125.818444
      NL            165.903226
      OL             33.296296
      OT             24.415385
      PE             20.558140
      PF              7.152542
      PM             19.933333
      PP             13.950000
      RM             11.178571
      SA                   NaN
      SS             57.000000
1982  AB                   NaN
      AH                   NaN
      CQ                   NaN
      DM             41.975042
      DO             47.919643
      DS            115.647929
      NL            160.613208
      OL             35.590361
      OT             24.925532
      OX             24.000000
      PC                   NaN
      PE             21.173077
      PF              6.918919
      PM             21.391304
      PP             16.125000
      RF             11.500000
      RM             10.436242
      SA                   NaN
      SH             79.000000
      SS                   NaN
1983  AB                   NaN
      AH                   NaN
      CB                   NaN
      DM             40.944551
      DO             47.150602
      DS            122.033088
      DX                   NaN
      NL            156.691489
      OL             34.584615
      OT             24.697674
      PC                   NaN
      PE             20.864865
      PF              6.833333
      PG                   NaN
      PM             22.023810
      PP             15.468750
      RM              9.872000
      SA                   NaN
      SH                   NaN
      SS                   NaN
1984  AB                   NaN
      AH                   NaN
      CB                   NaN
      CQ                   NaN
      DM             40.765306
      DO             48.415094
      DS            124.082192
      NL            150.095238
      OL             32.550725
      OT             22.416667
      OX             18.000000
      PE             20.210526
      PF              7.428571
      PH             28.000000
      PM             19.545455
      PP             15.307692
      PU                   NaN
      RM             11.152542
      SA                   NaN
      SS                   NaN
1985  AB                   NaN
      AH                   NaN
      CB                   NaN
      DM             41.507645
      DO             47.956731
      DS            124.326316
      NL            148.829268
      OL             32.108696
      OT             22.064516
      PE             20.360000
      PF                   NaN
      PH             32.666667
      PM             19.000000
      PP             15.764706
      RM              8.371429
      SA                   NaN
      SS                   NaN
1986  AB                   NaN
      AH                   NaN
      CB                   NaN
      DM             43.361596
      DO             49.372727
      DS            128.071429
      DX                   NaN
      NL            159.724138
      OL             30.880952
      OT             21.500000
      PE             22.520000
      PF              8.000000
      PH             39.000000
      PM             21.696970
      PP             16.750000
      RM             10.750000
      SA                   NaN
      SH             55.000000
      SS                   NaN
1987  AB                   NaN
      AH                   NaN
      CB                   NaN
      CM                   NaN
      CV                   NaN
      DM             43.232609
      DO             50.087379
      DS            126.383838
      NL            158.840000
      OL             30.779221
      OT             23.069767
      PC                   NaN
      PE             21.625899
      PF              7.500000
      PM             22.297710
      PP             17.840909
      RM             10.657609
      SA                   NaN
      SH             73.800000
      SS                   NaN
      UP                   NaN
      UR                   NaN
1988  AB                   NaN
      AH                   NaN
      CB                   NaN
      DM             43.397790
      DO             51.463768
      DS            129.490566
      DX                   NaN
      NL            163.104167
      OL             30.306122
      OT             24.070588
      PE             22.625668
      PF              8.000000
      PG                   NaN
      PH             33.000000
      PM             21.759259
      PP             18.280000
      RF             13.818182
      RM             10.322115
      SA                   NaN
      SH             72.806452
      SS                   NaN
      UL                   NaN
      UP                   NaN
      UR                   NaN
      ZL                   NaN
1989  AB                   NaN
      AH                   NaN
      BA              7.000000
      CB                   NaN
      CS                   NaN
      DM             44.349206
      DO             51.025641
      DS            121.896552
      NL            151.278689
      OL             31.947368
      OT             24.663366
      OX             20.000000
      PC                   NaN
      PE             21.935673
      PF              7.230769
      PH             30.500000
      PM             20.222222
      PP             17.409091
      RF             13.346939
      RM             10.411311
      SA                   NaN
      SC                   NaN
      SF             54.800000
      SH             76.345455
      SS                   NaN
      UP                   NaN
1990  AB                   NaN
      AH                   NaN
      BA              8.000000
      DM             41.769912
      DO             48.512048
      DS            121.187500
      NL            154.275862
      OL             31.200000
      OT             23.675325
      PC                   NaN
      PE             21.671233
      PF              7.117647
      PG                   NaN
      PH             31.142857
      PP             16.029412
      RF             12.916667
      RM             10.305677
      SF             52.611111
      SH             76.888889
      SS                   NaN
      UP                   NaN
1991  AB                   NaN
      AH                   NaN
      AS                   NaN
      BA              9.240000
      CB                   NaN
      DM             43.148338
      DO             49.695652
      DS            113.000000
      DX                   NaN
      NL            148.785714
      OL             28.171429
      OT             24.588235
      PC                   NaN
      PE             21.435484
      PF              7.827586
      PP             17.904762
      RM             10.498305
      RO             11.000000
      SA                   NaN
      SF             93.166667
      SH             63.000000
      SO             53.909091
      SS                   NaN
      UR                   NaN
1992  AB                   NaN
      AH                   NaN
      BA              7.833333
      CB                   NaN
      DM             43.877966
      DO             48.367816
      DS            112.352941
      DX                   NaN
      NL            139.000000
      OL             28.454545
      OT             24.928571
      PC                   NaN
      PE             22.750000
      PF              8.767857
      PH             31.142857
      PI             18.000000
      PP             17.479675
      RM             10.904762
      SF             43.000000
      SO             55.263158
      SS                   NaN
      UL                   NaN
      UR                   NaN
1993  AB                   NaN
      AH                   NaN
      AS                   NaN
      CB                   NaN
      CU                   NaN
      DM             43.373984
      DO             48.461538
      DS            105.722222
      DX                   NaN
      NL            127.391304
      OL             27.545455
      OT             22.363636
      OX                   NaN
      PC                   NaN
      PE             19.230769
      PF              8.238806
      PP             17.954023
      RM             10.747475
      SF             44.000000
      SO             55.600000
      SS                   NaN
      ST                   NaN
1994  AB                   NaN
      AH                   NaN
      CB                   NaN
      DM             42.373288
      DO             47.750000
      DS            106.625000
      DX                   NaN
      NL            186.875000
      OL             21.900000
      OT             25.285714
      PC                   NaN
      PE             18.000000
      PF              7.855072
      PP             17.585714
      PU                   NaN
      RM             10.675000
      SO             62.333333
      SS                   NaN
      SU                   NaN
      UL                   NaN
      UR                   NaN
1995  AB                   NaN
      AH                   NaN
      CB                   NaN
      DM             44.806147
      DO             49.592593
      DX                   NaN
      NL            155.833333
      OL             27.296296
      OT             24.868421
      PB             34.000000
      PC                   NaN
      PE             21.230769
      PF              8.780645
      PH             35.333333
      PI                   NaN
      PL             22.333333
      PM             27.375000
      PP             16.844444
      PU                   NaN
      RM             12.653846
      RX             20.000000
      SS                   NaN
      SU                   NaN
1996  AH                   NaN
      DM             44.506173
      DO             47.234940
      DX                   NaN
      NL            148.000000
      OL             27.769231
      OT             23.453704
      PB             32.578947
      PC                   NaN
      PE             22.027778
      PF              8.393846
      PL             21.166667
      PM             20.224490
      PP             18.095563
      PX                   NaN
      RM             11.455556
      SA                   NaN
      SS                   NaN
1997  AH                   NaN
      CB                   NaN
      DM             44.708551
      DO             48.177866
      DS            111.000000
      NL            150.688889
      OL             33.625000
      OT             24.785156
      PB             31.085603
      PE             20.929825
      PF              8.448649
      PH             22.000000
      PL             18.789474
      PM             21.126394
      PP             18.175000
      PX             19.000000
      RF             20.000000
      RM             11.230769
      RX             11.000000
      SA                   NaN
      SH             50.857143
      SO             54.666667
      SS                   NaN
1998  AB                   NaN
      AH                   NaN
      CB                   NaN
      CT                   NaN
      DM             43.131403
      DO             49.731183
      DS            116.000000
      DX                   NaN
      NL            159.466667
      OT             24.675676
      PB             30.082237
      PC                   NaN
      PE             20.304348
      PF              8.720000
      PL             16.714286
      PM             20.591398
      PP             16.266990
      PX                   NaN
      RM             13.100000
      SA                   NaN
      SS                   NaN
1999  AH                   NaN
      DM             43.945402
      DO             48.012048
      DS            120.714286
      DX                   NaN
      NL            182.200000
      OT             25.723810
      PB             31.710037
      PE             25.428571
      PM             22.523810
      PP             16.521212
      RM             10.555556
      SH             54.000000
      SS                   NaN
2000  AB                   NaN
      AH                   NaN
      DM             43.126638
      DO             49.224719
      DX                   NaN
      NL            179.307692
      OT             25.303448
      PB             30.878899
      PE             21.615385
      PG                   NaN
      PL             21.000000
      PM             20.500000
      PP             16.788618
      PX                   NaN
      RM             11.400000
      SH             73.375000
      SS                   NaN
2001  AB                   NaN
      AH                   NaN
      CB                   NaN
      DM             45.442177
      DO             52.233766
      DX                   NaN
      NL            167.851064
      OT             23.707792
      PB             32.798851
      PE             20.400000
      PF              8.538462
      PI             18.000000
      PM             26.666667
      PP             17.752896
      RM             11.333333
      SH             79.900000
      SS                   NaN
      UR                   NaN
2002  AB                   NaN
      AH                   NaN
      DM             46.168317
      DO             49.514403
      DX                   NaN
      NL            182.159091
      OL             25.428571
      OT             23.833333
      PB             32.359447
      PE             21.719298
      PF              7.388889
      PI             20.000000
      PM             19.000000
      PP             17.018617
      RM             10.000000
      RO             10.142857
      SF             62.166667
      SH             64.666667
      SS                   NaN
      UR                   NaN
      US                   NaN
Name: weight, dtype: float64

```

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### Show me the solution to challenge 4

How many individuals were counted for each species that was observed
more than 10 times?

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

Calculate the number of individuals observed and the average weight for
each species in each year.

Note that weight contains NaNs, so counts for record_id and weight
differ.

```python
# Counts and mean weight by species and year
surveys.groupby(["year", "species_id"]).agg(
    {"record_id": "count", "weight": ["count", "mean"]}
)
```

```{.output}
```

<style>
  table.dataframe { display: block; overflow-x: auto; white-space: nowrap; }
  table.dataframe tbody tr:hover { background-color: #ccffff !important; }
  table.dataframe tr:nth-child(even) { background-color: #f5f5f5; }
  table.dataframe th { text-align: right; font-weight: bold; }
  table.dataframe td { text-align: right; }
</style>

<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th>record_id</th>
      <th colspan="2" halign="left">weight</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>count</th>
      <th>count</th>
      <th>mean</th>
    </tr>
    <tr>
      <th>year</th>
      <th>species_id</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">1977</th>
      <th>DM</th>
      <td>264</td>
      <td>184</td>
      <td>41.141304</td>
    </tr>
    <tr>
      <th>DO</th>
      <td>12</td>
      <td>12</td>
      <td>42.666667</td>
    </tr>
    <tr>
      <th>DS</th>
      <td>98</td>
      <td>32</td>
      <td>121.437500</td>
    </tr>
    <tr>
      <th>NL</th>
      <td>31</td>
      <td>0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>OL</th>
      <td>10</td>
      <td>3</td>
      <td>21.666667</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">2002</th>
      <th>SF</th>
      <td>7</td>
      <td>6</td>
      <td>62.166667</td>
    </tr>
    <tr>
      <th>SH</th>
      <td>11</td>
      <td>9</td>
      <td>64.666667</td>
    </tr>
    <tr>
      <th>SS</th>
      <td>9</td>
      <td>0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>UR</th>
      <td>1</td>
      <td>0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>US</th>
      <td>4</td>
      <td>0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>509 rows × 3 columns</p>

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## Handling missing data

As we've discussed, some columns in the surveys dataframe have the value
NaN instead of text or numbers. NaN, short for "not a number," is a
special type of float used by pandas to represent missing data. When
reading from a CSV, pandas interpret certains values as NaN. NaNs are
excluded from groups and most aggregation calculations in pandas. Below,
we'll see how they can also cause issues when plotting.

::: callout ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## Defaults

See *na_values* in the [pd.read_csv()
documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
for the values that pandas interprets as NaN by default.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

When analyzing a dataset, it is critical to understand how missing data
is represented. Failing to do so may introduce errors into the analysis.
The ecology dataset used in this lesson uses empty cells to represent
missing data, but other disciplines have different conventions. For
example, some geographic datasets use -9999 to represent null values.
Failure to convert such values to NaN will result in significant errors
on any calculations performed on that dataset.

In some cases, it can be useful to fill in cells containing NaN with a
non-null value. Recall that the `groupby()` method excludes NaN cells.
When looking at sex, the following code counts only those cells with
either F (female) or M (male):

```python
surveys.groupby("sex")["record_id"].count()
```

```{.output}
sex
F    15690
M    17348
Name: record_id, dtype: int64
```

But not all records specify a sex. To include records where sex was not
specified, we can use the `fillna()` method on the sex column. This
method replaces each NaN with the first argument passed to the function
call. To replace all NaN values in sex with "U", use:

```python
surveys["sex"] = surveys["sex"].fillna("U")
```

The aggregation calculation now includes all records in the dataframe:

```python
surveys.groupby("sex")["record_id"].count()
```

```{.output}
sex
F    15690
M    17348
U     2511
Name: record_id, dtype: int64
```

In other cases, we may want to ignore rows that contain NaNs. This can
be done using `dropna()`:

```python
surveys = surveys.dropna()
```

This method returns a copy of the dataframe containing only those rows
that have non-NaN data in every field.

## Visualizing groups and statistics

Plots can be a useful way to identify patterns, commonalities, and
differences within a dataset. For example, they can use color, shape,
and size to highlight features of interest. Plotly allows us to style
the markers on a scatter plot in much the same way as we selected x and
y variables to plot at the end of the last lesson. To color the markers
on a scatter plot based on species_id, we can use the color keyword
argument:

```python
import plotly.express as px

px.scatter(surveys, x="weight", y="hindfoot_length", color="species_id")
```

```{.output}
```

<embed src="files/fig-6c9b8a7490eacbd3c686340a3a0e8134.html" width=760 height=570>

Now we have a much more colorful plot that shows more clearly how the
sizes of individual species produce some of the patterns we noted
earlier on the single-color plot. When hovering over a point, we can now
quickly see the exact weight, hindfoot length, and species_id (although
it remains unclear exactly what each ID means).

Scatter plots help us understand how parameters within a dataset covary.
Other plots, like box and violin plots, can be used to show the
distribution of a single parameter. Plotly can create a box plot using
almost the same syntax that we used above to create the scatter plot.
Let's make one for hindfoot length by changing the method to `px.box()`
and changing the x variable to `species_id`:

```python
px.box(surveys, x="species_id", y="hindfoot_length", color="species_id")
```

```{.output}
```

<embed src="files/fig-81b50ac778849616cb1b3c826a32b9de.html" width=760 height=570>

By default, this plot includes boxes (which show the distribution of
each species) and points (for outliers). When we hover over any of the
boxes on the plot above, the tooltip now shows aggregate statistics for
the species, including the minimum, median, maximum, upper, Q1, Q3,
upper fence, and lower fence values for hindfoot length.

Aesthetically, these plots could still use some work. They list species
in an arbitrary order, repeat colors, and include species with no
associated data. We'll return to this plot in [lesson
6](06-visualizing-data.html) to look at how we can address those issues.

::: keypoints ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   Calculate individual summary statistics using dataframe methods like
    `mean()`, `max()`, and `min()`
-   Calculate multiple summary statistics at once using the dataframe
    methods `describe()` and `agg()`
-   Group data by one or more columns using the `groupby()` method
-   Failing to consider how missing data is interpreted in a dataset can
    introduce significant errors
-   Box plots can be used to visualize the distribution of a single
    parameter

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
