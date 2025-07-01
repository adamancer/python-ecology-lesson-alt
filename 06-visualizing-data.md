---
title: Visualizing Data
teaching: 60
exercises: 0
---

::: questions ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   How can we look at individual rows and columns in a dataframe?
-   How can we style plots?
-   How can we modify the table and data?

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: objectives :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   Review processes for reading, modifying, and combining dataframes
-   Make and customize scatter, box, and bar plots

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

We'll begin by loading and preparing the data we'd like to plot. This
will include operations introduced in previous lessons, including
reading CSVs into dataframes, merging dataframes, sorting a dataframe,
and removing records that include null values. We'll begin by importing
pands:

```python
import pandas as pd
```

Next we'll load the surveys dataset using `pd.read_csv()`:

```python
surveys = pd.read_csv("data/surveys.csv")
```

Now we want to take a quick look at the surveys dataset. Since we're
going to be plotting data, we need to

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

There are 35,459 records in the table. Four columns--species_id, sex,
hindfoot_length, and weight--include null values.

```python
surveys["sex"] = surveys["sex"].fillna("U")
```

The plots below require records.

```python
surveys = surveys.dropna()
```

Now we will merge the main surveys dataframe with two other datasets
containing additional information:

-   **species.csv** provides the genus and species corresponding to
    species_id
-   **plots.csv** provides the plot type corresponding to plot_id

We will read each CSV and merge it into the main dataframe:

```python
species = pd.read_csv("data/species.csv")
plots = pd.read_csv("data/plots.csv")

surveys = surveys.merge(species, how="left").merge(plots, how="left")
```

### Chaining

The previous cell performs two merges in the same line of code.
Performing multiple operations on the same object in a single line of
code is called chaining.

```python
surveys["taxa"].unique()
```

```{.output}
array(['Rodent'], dtype=object)
```

In honor of this, we will rename our dataframe:

```python
rodents = surveys
rodents.sample(5)
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
      <th>genus</th>
      <th>species</th>
      <th>taxa</th>
      <th>plot_type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8645</th>
      <td>10920</td>
      <td>10</td>
      <td>13</td>
      <td>1985</td>
      <td>2</td>
      <td>DM</td>
      <td>F</td>
      <td>37.0</td>
      <td>40.0</td>
      <td>Dipodomys</td>
      <td>merriami</td>
      <td>Rodent</td>
      <td>Control</td>
    </tr>
    <tr>
      <th>25291</th>
      <td>29628</td>
      <td>5</td>
      <td>16</td>
      <td>1999</td>
      <td>3</td>
      <td>PB</td>
      <td>F</td>
      <td>27.0</td>
      <td>43.0</td>
      <td>Chaetodipus</td>
      <td>baileyi</td>
      <td>Rodent</td>
      <td>Long-term Krat Exclosure</td>
    </tr>
    <tr>
      <th>21521</th>
      <td>25534</td>
      <td>4</td>
      <td>12</td>
      <td>1997</td>
      <td>12</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>45.0</td>
      <td>Dipodomys</td>
      <td>merriami</td>
      <td>Rodent</td>
      <td>Control</td>
    </tr>
    <tr>
      <th>14502</th>
      <td>17652</td>
      <td>6</td>
      <td>22</td>
      <td>1990</td>
      <td>9</td>
      <td>DM</td>
      <td>M</td>
      <td>35.0</td>
      <td>46.0</td>
      <td>Dipodomys</td>
      <td>merriami</td>
      <td>Rodent</td>
      <td>Spectab exclosure</td>
    </tr>
    <tr>
      <th>18901</th>
      <td>22779</td>
      <td>9</td>
      <td>24</td>
      <td>1995</td>
      <td>8</td>
      <td>PP</td>
      <td>F</td>
      <td>20.0</td>
      <td>16.0</td>
      <td>Chaetodipus</td>
      <td>penicillatus</td>
      <td>Rodent</td>
      <td>Control</td>
    </tr>
  </tbody>
</table>

Finally we will save the rodents dataframe to a file:

```python
rodents.to_csv("data/rodents.csv", index=False)
```

We can load that dataframe directly in the future.

## Using plotly

We've already worked a little with plotly in previous lessons.

-   **Customizable.** Allows the appearance of plots to be extensively
    modified.
-   **Interactive.** Pan and zoom across plots, or hover over elements
    to get additional information about them.
-   **Flexible.** Allows creation of many different plot types, often
    with only a few lines of code.
-   **Embeddable.** Interactive plots can be embedded on websites using
    ploty's JavaScript library.

Plotly has two main ways of making plots:

-   plotly.express provides a simplified interface for quickly building
    and customizing plots
-   plotly.graph_objects uses a more complex interface to provide more
    granular control over the exact appearance of a plot

We will use plotly.express in this lesson.

::: callout ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## Other plotting libraries

The R community has largely coalesced around gg2plot for plotting. In
contrast, the Python community uses a number of data visualization
libraries. Some commonly used alternatives to plotly include:

-   [Bokeh](https://bokeh.org/)
-   [Matplotlib](https://matplotlib.org/)
-   [seaborn](https://seaborn.pydata.org/)
-   [Vega-Altair](https://altair-viz.github.io/)

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

We'll begin by reproducing the scatterplot from the end of lesson 4,
which used weight on the x axis and hindfoot length on the y axis.

```python
import plotly.express as px

px.scatter(surveys, x="weight", y="hindfoot_length")
```

```{.output}
```

<embed src="files/fig-a5bc67ed89866863a9a8945a8141239c.html" width=760 height=570>

Let's take a quick look at the interactive elements on this plot. When
we hover over a plotly plot, a toolbar appears in the upper right
corner. Each icon on the toolbar is a widget that allows us to interact
with the plot. By default, the toolbar includes the following widgets:

-   The camera allows us to save the current view as a PNG file
-   The next four widgets are toggles that control how click-and-drag
    affects the plot. Only one can be active at a time.
    -   The magnifying glass enable a zoom box
    -   The crossing arrows enable panning
    -   The dotted box enables drawing a box to select data
    -   The dotted lasso enables drawing an arbitrary shape to to select
        data
-   The plus box allows us to zoom in
-   The minus box allows us to zoom out
-   The crossing arrows autoscale the plot to show all adata
-   The house resets the plot to the original view

::: challenge ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

What are some limitations to the plot above? Think about how the data
itself is presented as well as the general appearance of the plot.

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   All points are the same color
-   Points overlap, making it difficult to understand how data is
    distributed
-   Axis labels include underscores and lack units
-   No plot title

Any others?

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

One issue with the plot is that many of the points in the dataframe
overlap, making it difficult to get a feel for how the data is
distributed. Does it cluster in places? Is it evenly distributed? We
really can't tell.

We can mitigate this issue in part by making the points semitransparent
using the opacity keyword argument:

```python
px.scatter(surveys, x="weight", y="hindfoot_length", opacity=0.2)
```

```{.output}
```

<embed src="files/fig-e6e8b7846f1f5308785022397604b063.html" width=760 height=570>

With the points now partially transparent, the places where they overlap
are clearer, and we can see several areas where the observations
cluster.

```python
px.scatter(surveys, x="weight", y="hindfoot_length", color="genus", opacity=0.2)
```

```{.output}
```

<embed src="files/fig-9c621cbf03e5d76575c93439a4277a21.html" width=760 height=570>

```python
px.scatter(
    surveys,
    x="weight",
    y="hindfoot_length",
    color="genus",
    opacity=0.2,
    color_discrete_sequence=px.colors.qualitative.Safe,
)
```

```{.output}
```

<embed src="files/fig-349b125e7900fc69cfa30682b78779c0.html" width=760 height=570>

The legend of the plot is not ordered. Because we want to use a
consistent color scheme across plots. We can use the category_order
keyword argument to order the legend alphabetically.

This argument uses a `dict`, which is a built-in data type that we have
not discussed yet. That means it can be used in any Python application
without having to import anything. Like a `list`, a `dict` is a
container that can include more than one object. Where as a `list` is a
sequence, a `dict` is a mapping consisting of *keys* that map to
*values*.

Let's see what that looks like in practice. Here we define a `dict`
mapping lowercase to uppercase letters. Each pair of values is separated
by a colon, with the key on the left and the value on the right.

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

The `dict` passed to category_orders maps a column name from the
dataframe to a list of values in the preferred order. We stated above
that we'd like the genera in the plot to appear in alphabetical order.
We can construct that list manually. Instead, we will used the built-in
`sorted()` function to sort the values from the genus column of the
dataframe. Because we will be using the same order in all following
plots, we will store the sorted values in a variable.

```python
order = sorted(surveys["genus"].unique())
order
```

```{.output}
['Baiomys',
 'Chaetodipus',
 'Dipodomys',
 'Neotoma',
 'Onychomys',
 'Perognathus',
 'Peromyscus',
 'Reithrodontomys',
 'Sigmodon']
```

We can then pass the full `dict`---that is, `{"genus": order}`---to the
`px.scatter()` method to put the legend in alphabetical order:

```python
px.scatter(
    surveys,
    x="weight",
    y="hindfoot_length",
    color="genus",
    opacity=0.2,
    color_discrete_sequence=px.colors.qualitative.Safe,
    category_orders={"genus": order}
)
```

```{.output}
```

<embed src="files/fig-933d2518a110bd65ab5ebc96e3dcfc7c.html" width=760 height=570>

## Making a box plot

```python
px.box(
    surveys,
    x="genus",
    y="hindfoot_length",
    color="genus",
    color_discrete_sequence=px.colors.qualitative.Safe,
    category_orders={"genus": order}
)
```

```{.output}
```

<embed src="files/fig-1822cae94d8b2ae13c24587aa9846d13.html" width=760 height=570>

```python
px.box(
    surveys,
    x="genus",
    y="hindfoot_length",
    color="genus",
    color_discrete_sequence=px.colors.qualitative.Safe,
    category_orders={"genus": order},
)
```

```{.output}
```

<embed src="files/fig-1822cae94d8b2ae13c24587aa9846d13.html" width=760 height=570>

```python
px.box(
    surveys,
    x="genus",
    y="hindfoot_length",
    color="genus",
    color_discrete_sequence=px.colors.qualitative.Safe,
    points="all",
)
```

```{.output}
```

<embed src="files/fig-1121e84c510b364cb091c14e4c235f1b.html" width=760 height=570>

To update, we can use the update_traces() method.

```python
fig = px.box(
    surveys,
    x="genus",
    y="hindfoot_length",
    color="genus",
    color_discrete_sequence=px.colors.qualitative.Safe,
    category_orders={"genus": order},
    points="all",
)
fig.update_traces(marker={"opacity": 0.2})
```

```{.output}
```

<embed src="files/fig-7ce43f9683783ab25be1e3c9b9c449d0.html" width=760 height=570>

A similar plot is a violin plot. Try changing `px.box` to `px.violin` in
the code above.

## Changing labels

By default, plotly uses the column names from the dataframe as axis
labels. Column names may be legible but are rarely ideal.

Like category_orders, updating labels requires a `dict`.

```python
fig = px.box(
    surveys,
    x="genus",
    y="hindfoot_length",
    color="genus",
    color_discrete_sequence=px.colors.qualitative.Safe,
    category_orders={"genus": order},
    points="all",
    title="Rodent hindfoot length by genus",
    labels={
        "hindfoot_length": "Hindfoot length (mm)",
        "genus": "Genus",
    }
)
fig.update_traces(marker={"opacity": 0.2})
```

```{.output}
```

<embed src="files/fig-f45c439b56eb033a7459b9373521bc41.html" width=760 height=570>

## Making a bar chart

The stacked bar chart allows us to compare the total number of
observations per year but obscures how counts of individual genera have
varied over time. We can break each category into its own subplot by
adding the `facet-col` keyword argument:

```python
grouped = rodents.groupby(["year", "genus"]).count().reset_index()
px.bar(
    grouped,
    x="year",
    y="weight",
    color="genus",
    color_discrete_sequence=px.colors.qualitative.Safe,
)
```

```{.output}
```

<embed src="files/fig-14499ad0383f30c6d3b5384fff0f3585.html" width=760 height=570>

```python
px.bar(
    grouped,
    x="year",
    y="weight",
    color="genus",
    facet_col="genus",
    color_discrete_sequence=px.colors.qualitative.Safe,
)
```

```{.output}
```

<embed src="files/fig-96cffed241e98e74588ea75b4e02c597.html" width=760 height=570>

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
