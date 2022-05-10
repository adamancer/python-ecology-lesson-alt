---
title: Combining Dataframes
---

::: questions ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   How do we combine data from multiple sources using pandas?
-   How do we add data to an existing dataframe?

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: objectives :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   Use merge to add species info to the survey dataset
-   Use concat to add additional rows the dataset

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Dataframes are used to organize and group data by common characteristics
or principles. Often, we need to combine elements from separate tables
into a single tables or queries for analysis and visualization. A join
allows use to combine two dataframes using values common to each.

The survey dataframe we've been using throughout this lesson has a
column called species_id. We used this column in the previous lesson to
calculate summary statistics about observations of each species. But the
species_id is just a two-letter code--what does each code stand for? To
find out, we'll now load both the survey dataset and a second dataset
containing more detailed information about the various species observed:


```python
import pandas as pd

surveys = pd.read_csv("data/surveys.csv")
species = pd.read_csv("data/species.csv")

species
```

```{.output}
   species_id             genus          species     taxa
0          AB        Amphispiza        bilineata     Bird
1          AH  Ammospermophilus          harrisi   Rodent
2          AS        Ammodramus       savannarum     Bird
3          BA           Baiomys          taylori   Rodent
4          CB   Campylorhynchus  brunneicapillus     Bird
5          CM       Calamospiza      melanocorys     Bird
6          CQ        Callipepla         squamata     Bird
7          CS          Crotalus       scutalatus  Reptile
8          CT     Cnemidophorus           tigris  Reptile
9          CU     Cnemidophorus        uniparens  Reptile
10         CV          Crotalus          viridis  Reptile
11         DM         Dipodomys         merriami   Rodent
12         DO         Dipodomys            ordii   Rodent
13         DS         Dipodomys      spectabilis   Rodent
14         DX         Dipodomys              sp.   Rodent
15         EO           Eumeces        obsoletus  Reptile
16         GS          Gambelia            silus  Reptile
17         NL           Neotoma         albigula   Rodent
18         NX           Neotoma              sp.   Rodent
19         OL         Onychomys      leucogaster   Rodent
20         OT         Onychomys         torridus   Rodent
21         OX         Onychomys              sp.   Rodent
22         PB       Chaetodipus          baileyi   Rodent
23         PC            Pipilo        chlorurus     Bird
24         PE        Peromyscus         eremicus   Rodent
25         PF       Perognathus           flavus   Rodent
26         PG         Pooecetes        gramineus     Bird
27         PH       Perognathus         hispidus   Rodent
28         PI       Chaetodipus      intermedius   Rodent
29         PL        Peromyscus         leucopus   Rodent
30         PM        Peromyscus      maniculatus   Rodent
31         PP       Chaetodipus     penicillatus   Rodent
32         PU            Pipilo           fuscus     Bird
33         PX       Chaetodipus              sp.   Rodent
34         RF   Reithrodontomys       fulvescens   Rodent
35         RM   Reithrodontomys        megalotis   Rodent
36         RO   Reithrodontomys         montanus   Rodent
37         RX   Reithrodontomys              sp.   Rodent
38         SA        Sylvilagus        audubonii   Rabbit
39         SB          Spizella          breweri     Bird
40         SC        Sceloporus           clarki  Reptile
41         SF          Sigmodon      fulviventer   Rodent
42         SH          Sigmodon         hispidus   Rodent
43         SO          Sigmodon     ochrognathus   Rodent
44         SS      Spermophilus        spilosoma   Rodent
45         ST      Spermophilus     tereticaudus   Rodent
46         SU        Sceloporus        undulatus  Reptile
47         SX          Sigmodon              sp.   Rodent
48         UL            Lizard              sp.  Reptile
49         UP            Pipilo              sp.     Bird
50         UR            Rodent              sp.   Rodent
51         US           Sparrow              sp.     Bird
52         ZL       Zonotrichia       leucophrys     Bird
53         ZM           Zenaida         macroura     Bird
```

We can see that the species dataframe includes a genus, species, and
taxon for each species_id. This is much more useful than the species_id
included in the original dataframe--how can we add that data to our
surveys dataframe? Adding it by hand would be tedious and error prone.
Fortunately, `pandas` provides the `merge()` method to join two
dataframes.

To merge the surveys and species dataframes, use:


```python
merged = surveys.merge(species)
merged
```

```{.output}
       record_id  month  day  year  ...  weight          genus   species     taxa
0              1      7   16  1977  ...     NaN        Neotoma  albigula   Rodent
1              2      7   16  1977  ...     NaN        Neotoma  albigula   Rodent
2             22      7   17  1977  ...     NaN        Neotoma  albigula   Rodent
3             38      7   17  1977  ...     NaN        Neotoma  albigula   Rodent
4             72      8   19  1977  ...     NaN        Neotoma  albigula   Rodent
...          ...    ...  ...   ...  ...     ...            ...       ...      ...
34781      28988     12   23  1998  ...     NaN  Cnemidophorus    tigris  Reptile
34782      35512     12   31  2002  ...     NaN        Sparrow       sp.     Bird
34783      35513     12   31  2002  ...     NaN        Sparrow       sp.     Bird
34784      35528     12   31  2002  ...     NaN        Sparrow       sp.     Bird
34785      35544     12   31  2002  ...     NaN        Sparrow       sp.     Bird

[34786 rows x 12 columns]
```

Following the merge, the genus, species, and taxa columns have all been
added to the survey dataframe. We can now use those columns to filter
and summarize our data.

::: callout ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

The `pd.merge()` method is equivalent to the JOIN operation in SQL

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: challenge ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Filter the merged dataframe to show the genus, the species name, and the
weight for every individual captured at the site

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


```python
merged[["genus", "species", "weight"]]
```

```{.output}
               genus   species  weight
0            Neotoma  albigula     NaN
1            Neotoma  albigula     NaN
2            Neotoma  albigula     NaN
3            Neotoma  albigula     NaN
4            Neotoma  albigula     NaN
...              ...       ...     ...
34781  Cnemidophorus    tigris     NaN
34782        Sparrow       sp.     NaN
34783        Sparrow       sp.     NaN
34784        Sparrow       sp.     NaN
34785        Sparrow       sp.     NaN

[34786 rows x 3 columns]
```

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

In the example above, we didn't provide any information about how we
wanted to merge the dataframes together, so pandas made an educated
guess. It looked at the columns in each of the dataframes, then merged
them based on the columns that appear in both. Here, the only shared
name is species_id. If we want to control what columns are used to
merge, we can use the *on* keyword argument:


```python
surveys.merge(species, on="species_id")
```

```{.output}
       record_id  month  day  year  ...  weight          genus   species     taxa
0              1      7   16  1977  ...     NaN        Neotoma  albigula   Rodent
1              2      7   16  1977  ...     NaN        Neotoma  albigula   Rodent
2             22      7   17  1977  ...     NaN        Neotoma  albigula   Rodent
3             38      7   17  1977  ...     NaN        Neotoma  albigula   Rodent
4             72      8   19  1977  ...     NaN        Neotoma  albigula   Rodent
...          ...    ...  ...   ...  ...     ...            ...       ...      ...
34781      28988     12   23  1998  ...     NaN  Cnemidophorus    tigris  Reptile
34782      35512     12   31  2002  ...     NaN        Sparrow       sp.     Bird
34783      35513     12   31  2002  ...     NaN        Sparrow       sp.     Bird
34784      35528     12   31  2002  ...     NaN        Sparrow       sp.     Bird
34785      35544     12   31  2002  ...     NaN        Sparrow       sp.     Bird

[34786 rows x 12 columns]
```

::: challenge ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Compare the number of rows in the original and merged survey dataframes.
How do they differ? Why do you think that might be?

**Hint:** Use `pd.unique()` method to look at the species_id column in
each dataframe.

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


```python
# Some columns in survey are missing species_id
set(surveys["species_id"]) - set(species["species_id"])
```

```{.output}
{nan}
```

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

In practice, the values in the columns used to join two dataframes may
not align exactly. Above, the surveys dataframe contains a few hundred
rows where species_id is NaN. These are the rows that were dropped when
the dataframes were merged.

By default, `merge()` performs an **inner join**. This means that a row
will only appear if the value in the shared column appears in both of
the datasets being merged. In this case, that means that survey
observations that don't have a species_id or have a species_id that does
not appear in the species dataframe will be dropped.

This is not always desirable behavior. Fortunately, `pandas` allows us
to control how the merge is done.

-   **Inner:** Includes all rows with common values in the join
    column
-   **Left:** Include all rows from the left dataframe. Columns from
    the right dataframe are populated if a common value exists and
    set to NaN if not.
-   **Right:** Include all rows from the right dataframe. Columns
    from the left dataframe are populated if a common value exists
    and set to NaN if not.
-   **Outer:** Includes all rows from both dataframes

We want to keep all of our observations, so let's do a left join
instead. To specify the type of merge, we use the *how* keyword
argument:


```python
surveys.merge(species, how="left")
```

```{.output}
       record_id  month  day  year  ...  weight             genus    species    taxa
0              1      7   16  1977  ...     NaN           Neotoma   albigula  Rodent
1              2      7   16  1977  ...     NaN           Neotoma   albigula  Rodent
2              3      7   16  1977  ...     NaN         Dipodomys   merriami  Rodent
3              4      7   16  1977  ...     NaN         Dipodomys   merriami  Rodent
4              5      7   16  1977  ...     NaN         Dipodomys   merriami  Rodent
...          ...    ...  ...   ...  ...     ...               ...        ...     ...
35544      35545     12   31  2002  ...     NaN  Ammospermophilus    harrisi  Rodent
35545      35546     12   31  2002  ...     NaN  Ammospermophilus    harrisi  Rodent
35546      35547     12   31  2002  ...    14.0   Reithrodontomys  megalotis  Rodent
35547      35548     12   31  2002  ...    51.0         Dipodomys      ordii  Rodent
35548      35549     12   31  2002  ...     NaN               NaN        NaN     NaN

[35549 rows x 12 columns]
```

Now all 35,549 rows appear in the merged dataframe.

## Appending rows to a dataframe

Merges address the case where information about the same set of
observations is spread across multiple files. What about when the
observations themselves are split into more than one file? For a survey
like the one we've been looking at in this lesson, we might get a new
file once a year with the same columns that represent a completely new
set of observations. How can we add those new observations to our
dataframe?

We'll simulate this kind of thing by splitting two years worth of data
into separate dataframes. We can do this using conditionals, as we saw
in lesson 3:


```python
surveys_2001 = surveys[surveys["year"] == 2001].copy()
surveys_2001
```

```{.output}
       record_id  month  day  year  ...  species_id  sex hindfoot_length  weight
31710      31711      1   21  2001  ...          PB    F            26.0    25.0
31711      31712      1   21  2001  ...          DM    M            37.0    43.0
31712      31713      1   21  2001  ...          PB    M            29.0    44.0
31713      31714      1   21  2001  ...          DO    M            34.0    53.0
31714      31715      1   21  2001  ...          OT    M            20.0    27.0
...          ...    ...  ...   ...  ...         ...  ...             ...     ...
33315      33316     12   16  2001  ...         NaN  NaN             NaN     NaN
33316      33317     12   16  2001  ...         NaN  NaN             NaN     NaN
33317      33318     12   16  2001  ...         NaN  NaN             NaN     NaN
33318      33319     12   16  2001  ...         NaN  NaN             NaN     NaN
33319      33320     12   16  2001  ...         NaN  NaN             NaN     NaN

[1610 rows x 9 columns]
```


```python
surveys_2002 = surveys[surveys["year"] == 2002].copy()
surveys_2002
```

```{.output}
       record_id  month  day  year  ...  species_id  sex hindfoot_length  weight
33320      33321      1   12  2002  ...          DM    M            38.0    44.0
33321      33322      1   12  2002  ...          DO    M            37.0    58.0
33322      33323      1   12  2002  ...          PB    M            28.0    45.0
33323      33324      1   12  2002  ...          AB  NaN             NaN     NaN
33324      33325      1   12  2002  ...          DO    M            35.0    29.0
...          ...    ...  ...   ...  ...         ...  ...             ...     ...
35544      35545     12   31  2002  ...          AH  NaN             NaN     NaN
35545      35546     12   31  2002  ...          AH  NaN             NaN     NaN
35546      35547     12   31  2002  ...          RM    F            15.0    14.0
35547      35548     12   31  2002  ...          DO    M            36.0    51.0
35548      35549     12   31  2002  ...         NaN  NaN             NaN     NaN

[2229 rows x 9 columns]
```

We now have two different dataframes with the same columns but different
data, one with 1,610 rows, the other with 2,229 rows. We can combine
them using `pd.concat()`, which stacks the dataframes horizontally (that
is, it appends the 2002 dataset to the 2001 dataset):


```python
surveys_2001_2002 = pd.concat([surveys_2001, surveys_2002])
surveys_2001_2002
```

```{.output}
       record_id  month  day  year  ...  species_id  sex hindfoot_length  weight
31710      31711      1   21  2001  ...          PB    F            26.0    25.0
31711      31712      1   21  2001  ...          DM    M            37.0    43.0
31712      31713      1   21  2001  ...          PB    M            29.0    44.0
31713      31714      1   21  2001  ...          DO    M            34.0    53.0
31714      31715      1   21  2001  ...          OT    M            20.0    27.0
...          ...    ...  ...   ...  ...         ...  ...             ...     ...
35544      35545     12   31  2002  ...          AH  NaN             NaN     NaN
35545      35546     12   31  2002  ...          AH  NaN             NaN     NaN
35546      35547     12   31  2002  ...          RM    F            15.0    14.0
35547      35548     12   31  2002  ...          DO    M            36.0    51.0
35548      35549     12   31  2002  ...         NaN  NaN             NaN     NaN

[3839 rows x 9 columns]
```

The combined dataframe includes all rows from both dataframes.

In some cases, the exact columns may change from year to year even
within the same project. For example, researchers may decide to add an
additional column to track a new piece of data or to provide a quality
check. If a column is present in only one dataset, you can still
concatenate the datasets. Any column that does not appear in one of the
datasets will be set to NaN for those rows in the combined dataframe.

To illustrate this, we'll add a validated column to the 2002 survey,
then re-run `pd.concat()`:


```python
surveys_2002["validated"] = True

surveys_2001_2002 = pd.concat([surveys_2001, surveys_2002])
surveys_2001_2002
```

```{.output}
       record_id  month  day  year  ...  sex hindfoot_length weight  validated
31710      31711      1   21  2001  ...    F            26.0   25.0        NaN
31711      31712      1   21  2001  ...    M            37.0   43.0        NaN
31712      31713      1   21  2001  ...    M            29.0   44.0        NaN
31713      31714      1   21  2001  ...    M            34.0   53.0        NaN
31714      31715      1   21  2001  ...    M            20.0   27.0        NaN
...          ...    ...  ...   ...  ...  ...             ...    ...        ...
35544      35545     12   31  2002  ...  NaN             NaN    NaN       True
35545      35546     12   31  2002  ...  NaN             NaN    NaN       True
35546      35547     12   31  2002  ...    F            15.0   14.0       True
35547      35548     12   31  2002  ...    M            36.0   51.0       True
35548      35549     12   31  2002  ...  NaN             NaN    NaN       True

[3839 rows x 10 columns]
```

As expected, validated has a value of NaN for the 2001 data in the
combined dataframe.
