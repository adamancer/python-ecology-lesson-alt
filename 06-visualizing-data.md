---
title: Visualizing Data
teaching: 60
exercises: 0
---

::: questions ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   How can we create different types of plots using Python?
-   How can we style plots?
-   How can we add descriptive titles to plots and axes?

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: objectives :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   Review processes for reading, modifying, and combining dataframes
-   Make and customize scatter, box, and bar plots

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

We'll begin by loading and preparing the data we'd like to plot. This
will include operations introduced in previous lessons, including
reading CSVs into dataframes, merging dataframes, sorting a dataframe,
and removing records that include null values. We'll begin by importing
pandas:

```python
import pandas as pd
```

Next we'll load the surveys dataset using `pd.read_csv()`:

```python
surveys = pd.read_csv("data/surveys.csv")
```

Now we want to take a quick look at the surveys dataset. Since we're
going to be plotting data, we need to consider how we want to handle any
null values in the dataset. The `info()` method provides an overview,
including counts of non-null values, that we can use to assess the
dataset.

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

There are 35,459 records in the table. Four columns---species_id, sex,
hindfoot_length, and weight---include null values, that is, they contain
fewer non-null values than there are rows in the dataframe. We can us
`fillna()` to replace null values where it makes sense to do so. For
example, some specimens do not specify as sex. We can fill those values
in with the letter U (for unknown):

```python
surveys["sex"] = surveys["sex"].fillna("U")
```

The other three columns that contain null values are all required for
the plots we will create below. This means that we can use `dropna()` to
drop all rows where any column is null:

```python
surveys = surveys.dropna()
```

Now we we'll merge the main surveys dataframe with two other datasets
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

::: callout ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### Chaining

The previous cell performs two merges in the same line of code.
Performing multiple operations on the same object in a single line of
code is called chaining.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

We now have a dataframe that includes all observations from the Portal
dataset that specify a species, weight, and hindfoot length, as well as
descriptive metadata about each species and plot type. The taxa column
contains the general type of animal. If we look at the unique values in
this column--

```python
surveys["taxa"].unique()
```

```{.output}
array(['Rodent'], dtype=object)
```

--we can see that all remaining observations are of rodents. In honor of
this, we will assign our dataframe to a new variable:

```python
rodents = surveys
rodents.sample(5)
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
      <th>14297</th>
      <td>17433</td>
      <td>4</td>
      <td>26</td>
      <td>1990</td>
      <td>6</td>
      <td>PP</td>
      <td>M</td>
      <td>22.0</td>
      <td>18.0</td>
      <td>Chaetodipus</td>
      <td>penicillatus</td>
      <td>Rodent</td>
      <td>Short-term Krat Exclosure</td>
    </tr>
    <tr>
      <th>17172</th>
      <td>20722</td>
      <td>3</td>
      <td>17</td>
      <td>1993</td>
      <td>12</td>
      <td>DM</td>
      <td>M</td>
      <td>34.0</td>
      <td>42.0</td>
      <td>Dipodomys</td>
      <td>merriami</td>
      <td>Rodent</td>
      <td>Control</td>
    </tr>
    <tr>
      <th>24052</th>
      <td>28320</td>
      <td>8</td>
      <td>22</td>
      <td>1998</td>
      <td>1</td>
      <td>PP</td>
      <td>F</td>
      <td>21.0</td>
      <td>15.0</td>
      <td>Chaetodipus</td>
      <td>penicillatus</td>
      <td>Rodent</td>
      <td>Spectab exclosure</td>
    </tr>
    <tr>
      <th>24641</th>
      <td>28948</td>
      <td>12</td>
      <td>22</td>
      <td>1998</td>
      <td>17</td>
      <td>DM</td>
      <td>M</td>
      <td>36.0</td>
      <td>37.0</td>
      <td>Dipodomys</td>
      <td>merriami</td>
      <td>Rodent</td>
      <td>Control</td>
    </tr>
    <tr>
      <th>14456</th>
      <td>17606</td>
      <td>6</td>
      <td>21</td>
      <td>1990</td>
      <td>17</td>
      <td>DO</td>
      <td>M</td>
      <td>36.0</td>
      <td>55.0</td>
      <td>Dipodomys</td>
      <td>ordii</td>
      <td>Rodent</td>
      <td>Control</td>
    </tr>
  </tbody>
</table>

Finally, we'll save the rodents dataframe to a file that we can load
directly in the future if needed:

```python
rodents.to_csv("data/rodents.csv", index=False)
```

Now we're ready to plot.

## Re-introducing plotly

We've already worked with plotly a little in previous lessons, but we
haven't provided a comprehensive introduction. Plotly is a data
visualization package for Python that allows us to create customizable,
interactive plots of a variety of different types. Plotly makes plots
that are:

-   **Customizable.** Allows the appearance of plots to be extensively
    modified.
-   **Interactive.** Pan and zoom across plots, or hover over elements
    to get additional information about them.
-   **Flexible.** Many different plot types can be created, often with
    only a few lines of code. Because plotly uses similar syntax for
    each plot type, it is also easy to quickly change plot types to get
    a different perspective on a dataset.
-   **Embeddable.** Interactive plots can be embedded on websites using
    ploty's JavaScript library.

::: callout ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## Other plotting libraries

The R community has largely coalesced around gg2plot for plotting. In
contrast, the Python community has no clear consensus pick and makes use
of a number of data visualization packages. Some other commonly used
packages include:

-   [Bokeh](https://bokeh.org/)
-   [Matplotlib](https://matplotlib.org/)
-   [seaborn](https://seaborn.pydata.org/)
-   [Vega-Altair](https://altair-viz.github.io/)

The functionality of this packages overlaps to a large degree, and which
one to use depends in large part on personal preference.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Plotly has two main ways of making plots:

-   `plotly.express` provides a simplified interface for quickly
    building and customizing plots
-   `plotly.graph_objects` uses a more complex interface to provide more
    granular control over the contents of a plot

We will use `plotly.express` in this lesson.

We'll begin by reproducing the scatter plot from the [end of lesson
3](03-accessing-and-filtering-data.html#showing-data-on-a-plot), which
included weight on the x axis and hindfoot length on the y axis. Likely
pandas, the developers of `plotly.express` have a preferred alias, px,
that we will use when we import `plotly.express`:

```python
import plotly.express as px

px.scatter(rodents, x="weight", y="hindfoot_length")
```

```{.output}
```

<embed src="files/fig-a5bc67ed89866863a9a8945a8141239c.html" width=760 height=570>

Before diving into the content of this plot, let's take a quick look at
the interactive elements plotly makes available. When we hover over a
plotly plot, a toolbar appears in the upper right corner. Each icon on
the toolbar is a widget that allows us to interact with the plot. By
default, the toolbar includes the following widgets:

-   The camera allows us to save the current view as a PNG file
-   The next four widgets are toggles that control how click-and-drag
    affects the plot. Only one can be active at a time.
    -   The magnifying glass enables drawing a box to zoom
    -   The crossing arrows enable panning
    -   The dotted box enables drawing a box to select data
    -   The dotted lasso enables drawing an arbitrary shape to to select
        data
-   The plus box allows us to zoom in
-   The minus box allows us to zoom out
-   The crossing arrows autoscale the plot to show all adata
-   The house resets the plot to the original view

When we hover over a data point, we get a tooltip that shows information
about that point.

Now let's think about the plot itself.

::: challenge ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

What are some limitations to the plot above? Think about how the data
itself is presented as well as the general appearance of the plot.

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Some issues with the plot include the following:

-   All points are the same color
-   Large number of overlapping points, making it difficult to
    understand how data is distributed
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
using the opacity keyword argument. We'll use a value of 0.2, which
means the points are mostly transparent.

```python
px.scatter(rodents, x="weight", y="hindfoot_length", opacity=0.2)
```

```{.output}
```

<embed src="files/fig-e6e8b7846f1f5308785022397604b063.html" width=760 height=570>

With the points now partially transparent, the places where they overlap
are more obvious, and we can see several clusters. To get a better sense
of what those clusters might be, let's add some color to the plot.

At the end of lesson 4, we colored this scatter plot based on the
species_id column. This revealed that several of the clusters reflected
the species of rodent observed. But the use of species_id was
problematic in other ways. For one, there are so many different species
that colors ended up being re-used. For another, the species codes are
not legible to people who are not intimately familiar with this dataset.

With those concerns in mind, let's use genus for color instead. Genus
information wasn't available in lesson 4, but we can use it now now that
we've merged the surveys and species dataframes.

```python
px.scatter(rodents, x="weight", y="hindfoot_length", color="genus", opacity=0.2)
```

```{.output}
```

<embed src="files/fig-9c621cbf03e5d76575c93439a4277a21.html" width=760 height=570>

## Choosing colors

One concern when making plots is to make sure they are legible to as
broad an audience as possible. Clear, informative labels are one way to
do this. Color is another.

Plotly makes a number of color palettes available via its color module.
Because we are working with categorical data, we will use a
*qualitative* palette, which consists of a list of discrete colors.
Other palette types are also available. For example, plots showing a
range of values might benefit from using a *sequential* or *diverging*
color scheme, which use a continuous range of colors (for example, blue
to red for a heat map).

Qualitative palettes are available under `px.colors.qualitative`. We can
view the available plaettes using the swatches function:

```python
px.colors.qualitative.swatches()
```

```{.output}
```

<embed src="files/fig-20548c05560600010e3e88783aacdd86.html" width=760 height=570>

In the spirit of effective communication with a wide audience, we will
use `px.colors.qualitative.Safe`, a colorblind-safe palette. Because we
will be using the same palette for the rest of the lesson, we will store
the palette as a variable:

```python
colors = px.colors.qualitative.Safe
```

In addition to simplifying the code for future plots a bit, storing the
palette as a variable also allows us to quickly change the color scheme
for all our plots at once if needed.

Let's apply the safe colors to our scatter plot:

```python
px.scatter(
    rodents,
    x="weight",
    y="hindfoot_length",
    color="genus",
    opacity=0.2,
    color_discrete_sequence=colors,
)
```

```{.output}
```

<embed src="files/fig-349b125e7900fc69cfa30682b78779c0.html" width=760 height=570>

## Sorting data

Take a look at the legend of the plot. The genera from the dataset are
all listed, but they are in no apparent order. This makes it difficult
for anyone looking at the plot to quickly pick out a given genus. We can
alphabetize the legend to make it more readable. To do so, we can use
the category_order keyword argument.

This argument requires a `dict`. Recall that a `dict` is a mapping of
keys to values defined using curly braces. The `dict` passed to
category_orders maps a column name from the dataframe to a list of
values in the preferred order.

One approach to creating an alphabetical list would be to simply build
the list manually. That would work well enough here, where we have only
a handful of values, but quickly becomes unwiedly for larger datasets.
Instead, we will used the built-in `sorted()` function to create a
sorted list of values in the genus column. Because we will be using the
same order in all following plots, we will store the dict with the
sorted values in a variable that we can refer to whenever we need to and
can change if needed.

::: challenge ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Create the `dict` needed for category_order. The `dict` should map the
column name, `genus`, to an ordered list of unique values from that
column.

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

```python
vals = rodents["genus"]
unique = vals.unique()
ordered = sorted(unique)
cat_order = {"genus": ordered}
```

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

In addition to the approach used in the challenge, we can create the
`dict` we need with a single line of code:

```python
cat_order = {"genus": sorted(rodents["genus"].unique())}
```

That variable can now be passed to the category_orders keyword argument,
producing a new version of the plot with an alphabetical legend.

```python
px.scatter(
    rodents,
    x="weight",
    y="hindfoot_length",
    color="genus",
    opacity=0.2,
    color_discrete_sequence=colors,
    category_orders=cat_order,
)
```

```{.output}
```

<embed src="files/fig-933d2518a110bd65ab5ebc96e3dcfc7c.html" width=760 height=570>

Note that the colors in the plot have also changed. Colors are assigned
based on the same category order used by the legend.

## Adding plot and axis titles

By default, plotly uses the column names from the dataframe to label the
axes of a plot. Here, the axis labels are adequate but would benefit
from removing the underscore and including units. We can use the labels
keyword argument to assign human-readable labels to our plto.

We will turn again to a `dict` for this, which we will use to map the
underlying column names to preferred display values:

```python
labels = {
    "hindfoot_length": "Hindfoot length (mm)",
    "genus": "Genus",
    "weight": "Weight (g)"
}
```

We can then update the plot itself using the title and labels keyword
arguments:

```python
px.scatter(
    rodents,
    x="weight",
    y="hindfoot_length",
    color="genus",
    opacity=0.2,
    color_discrete_sequence=colors,
    category_orders=cat_order,
    title="Rodent size by genus",
    labels=labels,
)
```

```{.output}
```

<embed src="files/fig-25169cdf2c7196dc94ea79f6aadba526.html" width=760 height=570>

## Create a faceted plot

Even with the semitransparent points, there is a good deal of overlap
among the data on this plot, particularly in the lower left part. It may
be useful to plot each genus separately to see if anyting interesting is
being obscured. We could do so using some of the techniques we've
already covered. For example, we could filter the dataframe by genus and
create a separate plots for each.

Plotly provides a simpler approach called faceting. A facet is a type of
filter, and a faceted plot includes a separate subplot for each unique
value. In plotly, we can create a faceted plot using the facet_col
keyword argument. This argument produces a separate subplot for each
unique value in the specified column. The subplots are arranged in a
single row.

The plots we have created so far have not specified dimensions, but we
will need to consider the size of the faceted plot. Because this plot
includes a number of subplots, it may appear cramped unless it is quite
wide. We can use the height and width keyword arguments to set the size
of the plot. Each of these arguments requires an integer specifying a
size in pixels.

Let's update our plot to facet it by genus and make it 1400 pixels wide
by 400 pixels tall:

```python
px.scatter(
    rodents,
    x="weight",
    y="hindfoot_length",
    color="genus",
    opacity=0.2,
    color_discrete_sequence=colors,
    category_orders=cat_order,
    title="Rodent size by genus",
    labels=labels,
    facet_col="genus",
    width=1400,
    height=400,
)
```

```{.output}
```

<embed src="files/fig-7af8a7c1bc6df4beb06c9a47f54800e5.html" width=760 height=570>

::: callout ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#### Row facets

The facet_col argument produces a single row of subplots. There is
another argument, facet_row, that places each subplot in a separate row
instead. Column and row facets can even be combined, for example, to
produce a grid of subplots with genus as columns and sex as rows.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## Making a box plot

We briefly discussed box plots (also known as box-and-whisker plots) in
[lesson 4](04-aggregating-data.html#visualizing-groups-and-statistics)
as part of the discussion of summary statistics. Box plots are an
effective way to visualize the distribution of data. Plotly uses the
`px.box()` method to generate them.

Some issues raised about the plot created during the earlier
lesson---including the arbitrary order in which data was plotted, the
repeated colors, and the inclusion of species with no data---have
already been addressed above. We can integrate them into the box plot
using the same approaches that we used for the scatter plots previously.
Let's create a box plot of hindfoot length by genus using the same color
and ordering rules we defined earlier:

```python
px.box(
    rodents,
    x="genus",
    y="hindfoot_length",
    color="genus",
    color_discrete_sequence=colors,
    category_orders=cat_order,
    title="Rodent hindfoot length by genus",
    labels=labels,
)
```

```{.output}
```

<embed src="files/fig-88a734bc811c5eb1714bc2bec0cd0a92.html" width=760 height=570>

We now have a box plot with colors corresponding to the scatter plots
above, with an alphabetically ordered x axis and legend.

There are other aspects of the box plot that we may want to tweak. We'll
start with a concern about how the data is being represented. By
default, ploty's box plots show individual points only for outliers,
that is, points that plot outside the upper and lower fences. This works
well enough for normally distributed data but can obscure patterns for
more complex distributions. And indeed, some genera, like *Dipodomys*,
show a large number of outliers on the box pot and multiple clusters of
data on the scatter plot. How might we update the box plot to better
convey these distributions?

The `px.box()` method includes a keyword argument, points, that allows
us to change how the underlying data is displayed. It accepts three
values:

-   *outliers* only shows the outliers (default)
-   *all* shows all points
-   *None* shows no points

Let's try updating the box plot to show all the underlying data:

```python
px.box(
    rodents,
    x="genus",
    y="hindfoot_length",
    color="genus",
    color_discrete_sequence=colors,
    category_orders=cat_order,
    title="Rodent hindfoot length by genus",
    labels=labels,
    points="all",
)
```

```{.output}
```

<embed src="files/fig-5eea0eb0c66c21fc0305194a52809e43.html" width=760 height=570>

A point cloud is now visible to the left of each box-and-whisker. We can
see that plotly has spread the points out a bit along the x axis. This
process, called jitter, is necessary because otherwise the points for
each category would fall in a vertical line. We can also see that we've
run into the same problem we did above with the scatter plot: The large
number of overlapping points for each box makes it hard to see what is
going on inside each point cloud.

We can again address this problem by changing the opacity of the
markers. It's a little more complicated than it was for the scatter
plot, however, because the `px.box()` method does not allow us to set
the marker opacity directly. Instead, we have to build the plot, then
update the existing markers using the `update_traces()` method. (Plotly
refers to markers, lines, and other elements as traces.)

```python
fig = px.box(
    rodents,
    x="genus",
    y="hindfoot_length",
    color="genus",
    color_discrete_sequence=colors,
    category_orders=cat_order,
    title="Rodent hindfoot length by genus",
    labels=labels,
    points="all",
)
fig.update_traces(marker={"opacity": 0.1})
```

```{.output}
```

<embed src="files/fig-868351fb9d246f1d5921e6d6b8303f39.html" width=760 height=570>

With the points now semitransparent, it is possible to see separate
populations among some genera, like *Dipodomys*.

Another way to examine the distribution of data is a violin plot, which
visualizes the distribution of points as a line, similar to a Bell
curve. We can change our box plot to a violin plot by swapping
`px.violin()` in for `px.box()`:

```python
fig = px.violin(
    rodents,
    x="genus",
    y="hindfoot_length",
    color="genus",
    color_discrete_sequence=colors,
    category_orders=cat_order,
    title="Rodent hindfoot length by genus",
    labels=labels,
    points="all",
)
fig.update_traces(marker={"opacity": 0.1})
```

```{.output}
```

<embed src="files/fig-a2b6e5819ae8ea740baeb7e00455bb9c.html" width=760 height=570>

This plot makes it easier to see identify complex distributions, like
the bimodal distribution for *Chaetodipus*, that are visible but not
necessarily obvious in the point clouds.

::: challenge ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Let's return to a question posed all the way back in lesson 2: How has
the weight of *Dipodomys* species changed over time? Make a plot that
tries to answer this question.

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

There are several reasonable approaches to this question using the
scatter plots and boxplots covered so far in this lesson. One
possibility is a faceted plot showing the mean weight of each
*Dipodomys* over the course of the study.

```python
# Create genus_species column
rodents["genus_species"] = rodents["genus"] + " " + rodents["species"]

# Limit to Dipodomys
dipodomys = rodents[rodents["genus"] == "Dipodomys"].copy()

# Group by genus_species
grouped = dipodomys.groupby(["genus_species", "year"])["weight"].mean().reset_index()

# Create scatter plot
px.scatter(grouped, x="year", y="weight", facet_col="genus_species")
```



The plot generated by this code shows that the mean weights for these
species oscillated over the course of the study. Overall, mean weight
increased slightly for the two smaller species but decreased for the
largest species (albeit with a large oscillation that makes determining
a trend difficult.)

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: keypoints ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   Plotly offers a wide variety of ways to build and style scatter
    plots
-   Use scatter plots to visualize how parameters covary
-   Use box and violin plots to visualize the distribution of a
    parameter

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
