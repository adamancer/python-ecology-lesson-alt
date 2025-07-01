---
title: Visualizing data in a dataframe
teaching: 60
exercises: 0
---

::: questions ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   How can we look at individual rows and columns in a dataframe?
-   How can we perform calculations?
-   How can we modify the table and data?

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: objectives :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   Review processes for reading, modifying, and combining dataframes
-   Make and customize scatter, box, and bar plots

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

We'll begin by loading and preparing the data we'd like to plot. This
will include operations introduced in previous lessons, including
reading CSVs into dataframes, creating a date column, merging
dataframes, sorting a dataframe, and removing records including null
values.

```python
import pandas as pd
```

```python
surveys = pd.read_csv("data/surveys.csv")
```

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

```python
surveys["date"] = pd.to_datetime(surveys[["year", "month", "day"]])
surveys = surveys.sort_values("plot_type")
```

```python
surveys["taxa"].unique()
```

```{.output}
array(['Rodent'], dtype=object)
```

In honor of this, we will rename our dataframe:

```python
rodents = surveys
```

surveys.sample(5)

Finally we will save the rodents dataframe to a file:

```python
rodents.to_csv("data/rodents.csv", index=False)
```

We can load that dataframe directly in the future.

## Using plotly

We've already used plotly.

-   **Customizable.**
-   **Interactive.** You can pan and zoom across plots and hover over
    elements to get additional information about them.

Plotly has two main ways of making plots:

-   plotly.express provides a simplified interface for quickly building
    and customizing plots
-   plotly.graph_objects uses a more complex interface to provide more
    granular control over the exact appearance of a plot

We will use plotly.express in this lesson.

::: callout ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## Other plotting libraries

The R community has largely coalesced around the gg2plot library for
plotting. By contract, Python has a wider variety of commonly used
libraries. Some common alternatives include:

-   altair
-   bokeh
-   matplotlib
-   seaborn

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## Thinking about plots

What numeric data is included in the dataset? What categories of data
might we be interested in plotting?

For the plots below, we will focus on rodent data.

We want to include clear, human-readable labels for the data. Consistent
colors and symbols: When creating multiple plots, it is useful to use
the same styles to

We'll begin by loading and preparing the data we'd like to plot. This
will include operations introduced in previous lessons, including
reading CSVs into dataframes, creating a date column, merging
dataframes, sorting a dataframe, and removing records including null
values.

```python
import plotly.express as px

px.scatter(surveys, x="weight", y="hindfoot_length")
```

```{.output}
```

<embed src="files/fig-bc9a572edafa6c7a1e482b048bdfd859.html" width=760 height=570>

Let's take a quick look at the interactive elements on this plot. When
you hover over a plotly plot, a toolbar appears in the upper right
corner. Each icon on the toolbar is a widget that allows you to interact
with the plot. By default, the toolbar includes the following widgets:

-   The camera allows you to save the current view as a PNG file
-   The next four widgets control how click-and-drag affects the plot:
    -   The magnifying glass allows you to draw a box and zoom
    -   The crossing arrows allw you to pan
    -   The dotted box allows you to select data by drawing a box
    -   The dotted lasso allows you to select data by drawing a shape
-   The plus box allows you to zoom in
-   The minus box allows you to zoom out
-   The crossing arrows autoscale the plot to show all adata
-   The house resets the view to the original view

The default appearance of the plot has some drawbacks. One is that many
of the points overlap, making it difficult to understand how the data is
distributed. We can partially address this issue by making the point
semitransparent using the opacity keyword argument.

```python
px.scatter(surveys, x="weight", y="hindfoot_length", opacity=0.2)
```

```{.output}
```

<embed src="files/fig-b1611b036822e93155adf6c6d6f2e8cf.html" width=760 height=570>

With the points now partially transparent, we can get a better sense of
how the data is distributed.

```python
px.scatter(surveys, x="weight", y="hindfoot_length", color="plot_type", opacity=0.2)
```

```{.output}
```

<embed src="files/fig-1815d1eb8e724ef1d0450030dd3918b1.html" width=760 height=570>

```python
px.scatter(
    surveys,
    x="weight",
    y="hindfoot_length",
    color="plot_type",
    opacity=0.2,
    color_discrete_sequence=px.colors.qualitative.Safe,
)
```

```{.output}
```

<embed src="files/fig-4b47c4efad024d1aff63df7a70932d42.html" width=760 height=570>

## Making a box plot

```python
px.box(surveys, x="plot_type", y="hindfoot_length")
```

```{.output}
```

<embed src="files/fig-ae736a9ee93cea679eaf576c4d9ab989.html" width=760 height=570>

```python
px.box(
    surveys,
    x="plot_type",
    y="hindfoot_length",
    color="plot_type",
    color_discrete_sequence=px.colors.qualitative.Safe,
)
```

```{.output}
```

<embed src="files/fig-f758a59a4e6fca47485dbeca79316098.html" width=760 height=570>

```python
px.box(
    surveys,
    x="plot_type",
    y="hindfoot_length",
    color="plot_type",
    color_discrete_sequence=px.colors.qualitative.Safe,
    points="all",
)
```

```{.output}
```

<embed src="files/fig-2b50f852a8b45635d8fbfcdd7f2b4adc.html" width=760 height=570>

To update, we can use the update_traces() method.

```python
fig = px.box(
    surveys,
    x="plot_type",
    y="hindfoot_length",
    color="plot_type",
    color_discrete_sequence=px.colors.qualitative.Safe,
    points="all",
)
fig.update_traces(marker={"opacity": 0.2})
```

```{.output}
```

<embed src="files/fig-5cf1ec9469c574f9e904d1e65d017659.html" width=760 height=570>

A similar plot is a violin plot. Try changing `px.box` to `px.violin` in
the code above.

## Changing labels

```python
fig = px.box(
    surveys,
    x="plot_type",
    y="hindfoot_length",
    color="plot_type",
    color_discrete_sequence=px.colors.qualitative.Safe,
    points="all",
    title="Rodent hindfoot length by plot type",
    labels={
        "hindfoot_length": "Hindfoot length (mm)",
        "plot_type": "Plot type",
    }
)
fig.update_traces(marker={"opacity": 0.2})
```

```{.output}
```

<embed src="files/fig-be5e42e690afc63c7e9c647ffe0c2413.html" width=760 height=570>

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

<embed src="files/fig-81c7ee3dd50c4971423c5998cbe9cb2f.html" width=760 height=570>

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

<embed src="files/fig-0855e2a3e8080a3eee30698559e50dab.html" width=760 height=570>

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
