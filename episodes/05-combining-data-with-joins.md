---
title: Combining Dataframes
---

::: questions ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   How do we combine data from multiple sources using pandas?
-   How do we add data to an existing dataframe?
-   How do we split and combine data columns?

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: objectives :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   Use `pd.merge()` to add species info to the survey dataset
-   Use `pd.concat()` to add additional rows the dataset
-   Use string methods to combine, split, and modify text columns
    using the `str` accessor

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Dataframes can be used to organize and group data by common
characteristics. Often, we need to combine elements from separate
dataframes into one for analysis and visualization. A merge (or join)
allows use to combine two dataframes using values common to each.
Likewise, we may need to append data collected under different
circumstances. In this chapter, we will show how to merge, concatenate,
and split data using pandas.

## Merging dataframes

The survey dataframe we've been using throughout this lesson has a
column called species_id. We used this column in the previous lesson to
calculate summary statistics about observations of each species. But the
species_id is just a two-letter code—what does each code stand for? To
find out, we'll now load both the survey dataset and a second dataset
containing more detailed information about the various species observed.
Read the second dataframe from a file called species.csv:

```python
import pandas as pd

surveys = pd.read_csv("data/surveys.csv")
species = pd.read_csv("data/species.csv")

species
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
      <th>species_id</th>
      <th>genus</th>
      <th>species</th>
      <th>taxa</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>AB</td>
      <td>Amphispiza</td>
      <td>bilineata</td>
      <td>Bird</td>
    </tr>
    <tr>
      <th>1</th>
      <td>AH</td>
      <td>Ammospermophilus</td>
      <td>harrisi</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>2</th>
      <td>AS</td>
      <td>Ammodramus</td>
      <td>savannarum</td>
      <td>Bird</td>
    </tr>
    <tr>
      <th>3</th>
      <td>BA</td>
      <td>Baiomys</td>
      <td>taylori</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CB</td>
      <td>Campylorhynchus</td>
      <td>brunneicapillus</td>
      <td>Bird</td>
    </tr>
    <tr>
      <th>5</th>
      <td>CM</td>
      <td>Calamospiza</td>
      <td>melanocorys</td>
      <td>Bird</td>
    </tr>
    <tr>
      <th>6</th>
      <td>CQ</td>
      <td>Callipepla</td>
      <td>squamata</td>
      <td>Bird</td>
    </tr>
    <tr>
      <th>7</th>
      <td>CS</td>
      <td>Crotalus</td>
      <td>scutalatus</td>
      <td>Reptile</td>
    </tr>
    <tr>
      <th>8</th>
      <td>CT</td>
      <td>Cnemidophorus</td>
      <td>tigris</td>
      <td>Reptile</td>
    </tr>
    <tr>
      <th>9</th>
      <td>CU</td>
      <td>Cnemidophorus</td>
      <td>uniparens</td>
      <td>Reptile</td>
    </tr>
    <tr>
      <th>10</th>
      <td>CV</td>
      <td>Crotalus</td>
      <td>viridis</td>
      <td>Reptile</td>
    </tr>
    <tr>
      <th>11</th>
      <td>DM</td>
      <td>Dipodomys</td>
      <td>merriami</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>12</th>
      <td>DO</td>
      <td>Dipodomys</td>
      <td>ordii</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>13</th>
      <td>DS</td>
      <td>Dipodomys</td>
      <td>spectabilis</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>14</th>
      <td>DX</td>
      <td>Dipodomys</td>
      <td>sp.</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>15</th>
      <td>EO</td>
      <td>Eumeces</td>
      <td>obsoletus</td>
      <td>Reptile</td>
    </tr>
    <tr>
      <th>16</th>
      <td>GS</td>
      <td>Gambelia</td>
      <td>silus</td>
      <td>Reptile</td>
    </tr>
    <tr>
      <th>17</th>
      <td>NL</td>
      <td>Neotoma</td>
      <td>albigula</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>18</th>
      <td>NX</td>
      <td>Neotoma</td>
      <td>sp.</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>19</th>
      <td>OL</td>
      <td>Onychomys</td>
      <td>leucogaster</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>20</th>
      <td>OT</td>
      <td>Onychomys</td>
      <td>torridus</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>21</th>
      <td>OX</td>
      <td>Onychomys</td>
      <td>sp.</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>22</th>
      <td>PB</td>
      <td>Chaetodipus</td>
      <td>baileyi</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>23</th>
      <td>PC</td>
      <td>Pipilo</td>
      <td>chlorurus</td>
      <td>Bird</td>
    </tr>
    <tr>
      <th>24</th>
      <td>PE</td>
      <td>Peromyscus</td>
      <td>eremicus</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>25</th>
      <td>PF</td>
      <td>Perognathus</td>
      <td>flavus</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>26</th>
      <td>PG</td>
      <td>Pooecetes</td>
      <td>gramineus</td>
      <td>Bird</td>
    </tr>
    <tr>
      <th>27</th>
      <td>PH</td>
      <td>Perognathus</td>
      <td>hispidus</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>28</th>
      <td>PI</td>
      <td>Chaetodipus</td>
      <td>intermedius</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>29</th>
      <td>PL</td>
      <td>Peromyscus</td>
      <td>leucopus</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>30</th>
      <td>PM</td>
      <td>Peromyscus</td>
      <td>maniculatus</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>31</th>
      <td>PP</td>
      <td>Chaetodipus</td>
      <td>penicillatus</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>32</th>
      <td>PU</td>
      <td>Pipilo</td>
      <td>fuscus</td>
      <td>Bird</td>
    </tr>
    <tr>
      <th>33</th>
      <td>PX</td>
      <td>Chaetodipus</td>
      <td>sp.</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>34</th>
      <td>RF</td>
      <td>Reithrodontomys</td>
      <td>fulvescens</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>35</th>
      <td>RM</td>
      <td>Reithrodontomys</td>
      <td>megalotis</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>36</th>
      <td>RO</td>
      <td>Reithrodontomys</td>
      <td>montanus</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>37</th>
      <td>RX</td>
      <td>Reithrodontomys</td>
      <td>sp.</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>38</th>
      <td>SA</td>
      <td>Sylvilagus</td>
      <td>audubonii</td>
      <td>Rabbit</td>
    </tr>
    <tr>
      <th>39</th>
      <td>SB</td>
      <td>Spizella</td>
      <td>breweri</td>
      <td>Bird</td>
    </tr>
    <tr>
      <th>40</th>
      <td>SC</td>
      <td>Sceloporus</td>
      <td>clarki</td>
      <td>Reptile</td>
    </tr>
    <tr>
      <th>41</th>
      <td>SF</td>
      <td>Sigmodon</td>
      <td>fulviventer</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>42</th>
      <td>SH</td>
      <td>Sigmodon</td>
      <td>hispidus</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>43</th>
      <td>SO</td>
      <td>Sigmodon</td>
      <td>ochrognathus</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>44</th>
      <td>SS</td>
      <td>Spermophilus</td>
      <td>spilosoma</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>45</th>
      <td>ST</td>
      <td>Spermophilus</td>
      <td>tereticaudus</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>46</th>
      <td>SU</td>
      <td>Sceloporus</td>
      <td>undulatus</td>
      <td>Reptile</td>
    </tr>
    <tr>
      <th>47</th>
      <td>SX</td>
      <td>Sigmodon</td>
      <td>sp.</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>48</th>
      <td>UL</td>
      <td>Lizard</td>
      <td>sp.</td>
      <td>Reptile</td>
    </tr>
    <tr>
      <th>49</th>
      <td>UP</td>
      <td>Pipilo</td>
      <td>sp.</td>
      <td>Bird</td>
    </tr>
    <tr>
      <th>50</th>
      <td>UR</td>
      <td>Rodent</td>
      <td>sp.</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>51</th>
      <td>US</td>
      <td>Sparrow</td>
      <td>sp.</td>
      <td>Bird</td>
    </tr>
    <tr>
      <th>52</th>
      <td>ZL</td>
      <td>Zonotrichia</td>
      <td>leucophrys</td>
      <td>Bird</td>
    </tr>
    <tr>
      <th>53</th>
      <td>ZM</td>
      <td>Zenaida</td>
      <td>macroura</td>
      <td>Bird</td>
    </tr>
  </tbody>
</table>

We can see that the species dataframe includes a genus, species, and
taxon for each species_id. This is much more useful than the species_id
included in the original dataframe--how can we add that data to our
surveys dataframe? Adding it by hand would be tedious and error prone.
Fortunately, pandas provides the `pd.merge()` function to join two
dataframes.

::: callout ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## Managing repetitive data

Why store species data in a separate table in the first place? Species
information is repetitive: Every observation of the same species has the
same genus, species, and taxa. Storing it in the original survey table
would require including that data in every record, increasing the
complexity of the table and creating the possibility of errors. Storing
that data in a separate table means we only have to enter and validate
it once. A tool like pandas then allows us to access that data when we
need it.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

To merge the surveys and species dataframes, use:

```python
merged = pd.merge(surveys, species)
merged
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
      <td>Neotoma</td>
      <td>albigula</td>
      <td>Rodent</td>
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
      <td>Neotoma</td>
      <td>albigula</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>2</th>
      <td>22</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>15</td>
      <td>NL</td>
      <td>F</td>
      <td>31.0</td>
      <td>NaN</td>
      <td>Neotoma</td>
      <td>albigula</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>3</th>
      <td>38</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>17</td>
      <td>NL</td>
      <td>M</td>
      <td>33.0</td>
      <td>NaN</td>
      <td>Neotoma</td>
      <td>albigula</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>4</th>
      <td>72</td>
      <td>8</td>
      <td>19</td>
      <td>1977</td>
      <td>2</td>
      <td>NL</td>
      <td>M</td>
      <td>31.0</td>
      <td>NaN</td>
      <td>Neotoma</td>
      <td>albigula</td>
      <td>Rodent</td>
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
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>34781</th>
      <td>28988</td>
      <td>12</td>
      <td>23</td>
      <td>1998</td>
      <td>6</td>
      <td>CT</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Cnemidophorus</td>
      <td>tigris</td>
      <td>Reptile</td>
    </tr>
    <tr>
      <th>34782</th>
      <td>35512</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>11</td>
      <td>US</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sparrow</td>
      <td>sp.</td>
      <td>Bird</td>
    </tr>
    <tr>
      <th>34783</th>
      <td>35513</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>11</td>
      <td>US</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sparrow</td>
      <td>sp.</td>
      <td>Bird</td>
    </tr>
    <tr>
      <th>34784</th>
      <td>35528</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>13</td>
      <td>US</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sparrow</td>
      <td>sp.</td>
      <td>Bird</td>
    </tr>
    <tr>
      <th>34785</th>
      <td>35544</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>US</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sparrow</td>
      <td>sp.</td>
      <td>Bird</td>
    </tr>
  </tbody>
</table>
<p>34786 rows × 12 columns</p>

Following the merge, the genus, species, and taxa columns have all been
added to the survey dataframe. We can now use those columns to filter
and summarize our data.

::: callout ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### Joins

The `pd.merge()` method is equivalent to the JOIN operation in SQL

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: challenge ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Filter the merged dataframe to show the genus, the species name, and the
weight for every individual captured at the site

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

```python
merged[["genus", "species", "weight"]]
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
      <th>genus</th>
      <th>species</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Neotoma</td>
      <td>albigula</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Neotoma</td>
      <td>albigula</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Neotoma</td>
      <td>albigula</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Neotoma</td>
      <td>albigula</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Neotoma</td>
      <td>albigula</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>34781</th>
      <td>Cnemidophorus</td>
      <td>tigris</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>34782</th>
      <td>Sparrow</td>
      <td>sp.</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>34783</th>
      <td>Sparrow</td>
      <td>sp.</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>34784</th>
      <td>Sparrow</td>
      <td>sp.</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>34785</th>
      <td>Sparrow</td>
      <td>sp.</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>34786 rows × 3 columns</p>

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

In the example above, we didn't provide any information about how we
wanted to merge the dataframes together, so pandas used its default
arguments to make an educated guess. It looked at the columns in each of
the dataframes, then merged them based on the columns that appear in
both. Here, the only shared name is species_id, so that's the column
pandas used to merge. For more complex tables, we may want to specify
the columns are used for merging. We can do so by passing one or more
column names using the *on* keyword argument:

```python
pd.merge(surveys, species, on="species_id")
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
      <td>Neotoma</td>
      <td>albigula</td>
      <td>Rodent</td>
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
      <td>Neotoma</td>
      <td>albigula</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>2</th>
      <td>22</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>15</td>
      <td>NL</td>
      <td>F</td>
      <td>31.0</td>
      <td>NaN</td>
      <td>Neotoma</td>
      <td>albigula</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>3</th>
      <td>38</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>17</td>
      <td>NL</td>
      <td>M</td>
      <td>33.0</td>
      <td>NaN</td>
      <td>Neotoma</td>
      <td>albigula</td>
      <td>Rodent</td>
    </tr>
    <tr>
      <th>4</th>
      <td>72</td>
      <td>8</td>
      <td>19</td>
      <td>1977</td>
      <td>2</td>
      <td>NL</td>
      <td>M</td>
      <td>31.0</td>
      <td>NaN</td>
      <td>Neotoma</td>
      <td>albigula</td>
      <td>Rodent</td>
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
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>34781</th>
      <td>28988</td>
      <td>12</td>
      <td>23</td>
      <td>1998</td>
      <td>6</td>
      <td>CT</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Cnemidophorus</td>
      <td>tigris</td>
      <td>Reptile</td>
    </tr>
    <tr>
      <th>34782</th>
      <td>35512</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>11</td>
      <td>US</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sparrow</td>
      <td>sp.</td>
      <td>Bird</td>
    </tr>
    <tr>
      <th>34783</th>
      <td>35513</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>11</td>
      <td>US</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sparrow</td>
      <td>sp.</td>
      <td>Bird</td>
    </tr>
    <tr>
      <th>34784</th>
      <td>35528</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>13</td>
      <td>US</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sparrow</td>
      <td>sp.</td>
      <td>Bird</td>
    </tr>
    <tr>
      <th>34785</th>
      <td>35544</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>US</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sparrow</td>
      <td>sp.</td>
      <td>Bird</td>
    </tr>
  </tbody>
</table>
<p>34786 rows × 12 columns</p>

::: challenge ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Compare the number of rows in the original and merged survey dataframes.
How do they differ? Why do you think that might be?

**Hint:** Use `pd.unique()` method to look at the species_id column in
each dataframe.

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

```python
pd.unique(surveys["species_id"].sort_values())
```

```{.output}
array(['AB', 'AH', 'AS', 'BA', 'CB', 'CM', 'CQ', 'CS', 'CT', 'CU', 'CV',
       'DM', 'DO', 'DS', 'DX', 'NL', 'OL', 'OT', 'OX', 'PB', 'PC', 'PE',
       'PF', 'PG', 'PH', 'PI', 'PL', 'PM', 'PP', 'PU', 'PX', 'RF', 'RM',
       'RO', 'RX', 'SA', 'SC', 'SF', 'SH', 'SO', 'SS', 'ST', 'SU', 'UL',
       'UP', 'UR', 'US', 'ZL', nan], dtype=object)
```

```python
pd.unique(species["species_id"].sort_values())
```

```{.output}
array(['AB', 'AH', 'AS', 'BA', 'CB', 'CM', 'CQ', 'CS', 'CT', 'CU', 'CV',
       'DM', 'DO', 'DS', 'DX', 'EO', 'GS', 'NL', 'NX', 'OL', 'OT', 'OX',
       'PB', 'PC', 'PE', 'PF', 'PG', 'PH', 'PI', 'PL', 'PM', 'PP', 'PU',
       'PX', 'RF', 'RM', 'RO', 'RX', 'SA', 'SB', 'SC', 'SF', 'SH', 'SO',
       'SS', 'ST', 'SU', 'SX', 'UL', 'UP', 'UR', 'US', 'ZL', 'ZM'],
      dtype=object)
```

Some records in the surveys dataframe do not specify a species. By
default, only records with a value that occurs in both the surveys and
species dataframes appear in the merged dataframe, so rows without a
species_id are excluded.

The built-in `set` type can be used to quickly assess differences like
this:

```python
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

By default, `pd.merge()` performs an **inner join**. This means that a
row will only appear if the value in the shared column appears in both
of the datasets being merged. In this case, that means that survey
observations that don't have a species_id or have a species_id that does
not appear in the species dataframe will be dropped.

This is not always desirable behavior. Fortunately, pandas supports
additional types of merges:

-   **Inner:** Include all rows with common values in the join
    column. This is the default behavior.
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
pd.merge(surveys, species, how="left")
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
      <td>Neotoma</td>
      <td>albigula</td>
      <td>Rodent</td>
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
      <td>Neotoma</td>
      <td>albigula</td>
      <td>Rodent</td>
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
      <td>Dipodomys</td>
      <td>merriami</td>
      <td>Rodent</td>
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
      <td>Dipodomys</td>
      <td>merriami</td>
      <td>Rodent</td>
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
      <td>Dipodomys</td>
      <td>merriami</td>
      <td>Rodent</td>
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
      <td>Ammospermophilus</td>
      <td>harrisi</td>
      <td>Rodent</td>
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
      <td>Ammospermophilus</td>
      <td>harrisi</td>
      <td>Rodent</td>
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
      <td>Reithrodontomys</td>
      <td>megalotis</td>
      <td>Rodent</td>
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
      <td>Dipodomys</td>
      <td>ordii</td>
      <td>Rodent</td>
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
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>35549 rows × 12 columns</p>

Now all 35,549 rows appear in the merged dataframe.

## Appending rows to a dataframe

Merges address the case where information about the same set of
observations is spread across multiple files. What about when the
observations themselves are split into more than one file? For a survey
like the one we've been looking at in this lesson, we might get a new
file once a year with the same columns but a completely new set of
observations. How can we add those new observations to our dataframe?

We'll simulate this operation by splitting data from two different
years, 2001 and 2002, into separate dataframes. We can do this using
conditionals, as we saw in lesson 3:

```python
surveys_2001 = surveys[surveys["year"] == 2001].copy()
surveys_2001
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
      <th>31710</th>
      <td>31711</td>
      <td>1</td>
      <td>21</td>
      <td>2001</td>
      <td>1</td>
      <td>PB</td>
      <td>F</td>
      <td>26.0</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>31711</th>
      <td>31712</td>
      <td>1</td>
      <td>21</td>
      <td>2001</td>
      <td>1</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>43.0</td>
    </tr>
    <tr>
      <th>31712</th>
      <td>31713</td>
      <td>1</td>
      <td>21</td>
      <td>2001</td>
      <td>1</td>
      <td>PB</td>
      <td>M</td>
      <td>29.0</td>
      <td>44.0</td>
    </tr>
    <tr>
      <th>31713</th>
      <td>31714</td>
      <td>1</td>
      <td>21</td>
      <td>2001</td>
      <td>1</td>
      <td>DO</td>
      <td>M</td>
      <td>34.0</td>
      <td>53.0</td>
    </tr>
    <tr>
      <th>31714</th>
      <td>31715</td>
      <td>1</td>
      <td>21</td>
      <td>2001</td>
      <td>2</td>
      <td>OT</td>
      <td>M</td>
      <td>20.0</td>
      <td>27.0</td>
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
      <th>33315</th>
      <td>33316</td>
      <td>12</td>
      <td>16</td>
      <td>2001</td>
      <td>11</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33316</th>
      <td>33317</td>
      <td>12</td>
      <td>16</td>
      <td>2001</td>
      <td>13</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33317</th>
      <td>33318</td>
      <td>12</td>
      <td>16</td>
      <td>2001</td>
      <td>14</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33318</th>
      <td>33319</td>
      <td>12</td>
      <td>16</td>
      <td>2001</td>
      <td>15</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33319</th>
      <td>33320</td>
      <td>12</td>
      <td>16</td>
      <td>2001</td>
      <td>16</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>1610 rows × 9 columns</p>

```python
surveys_2002 = surveys[surveys["year"] == 2002].copy()
surveys_2002
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
      <th>33320</th>
      <td>33321</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>1</td>
      <td>DM</td>
      <td>M</td>
      <td>38.0</td>
      <td>44.0</td>
    </tr>
    <tr>
      <th>33321</th>
      <td>33322</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>1</td>
      <td>DO</td>
      <td>M</td>
      <td>37.0</td>
      <td>58.0</td>
    </tr>
    <tr>
      <th>33322</th>
      <td>33323</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>1</td>
      <td>PB</td>
      <td>M</td>
      <td>28.0</td>
      <td>45.0</td>
    </tr>
    <tr>
      <th>33323</th>
      <td>33324</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>1</td>
      <td>AB</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33324</th>
      <td>33325</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>1</td>
      <td>DO</td>
      <td>M</td>
      <td>35.0</td>
      <td>29.0</td>
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
<p>2229 rows × 9 columns</p>

We now have two different dataframes with the same columns but different
data, one with 1,610 rows, the other with 2,229 rows. We can combine
them into a new dataframe using `pd.concat()`, which stacks the
dataframes vertically (that is, it appends records from the 2002 dataset
to the 2001 dataset). This method accepts a list and will concatenate
each item moving from left to right. We're only combining two dataframes
here but could do more if needed.

```python
surveys_2001_2002 = pd.concat([surveys_2001, surveys_2002])
surveys_2001_2002
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
      <th>31710</th>
      <td>31711</td>
      <td>1</td>
      <td>21</td>
      <td>2001</td>
      <td>1</td>
      <td>PB</td>
      <td>F</td>
      <td>26.0</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>31711</th>
      <td>31712</td>
      <td>1</td>
      <td>21</td>
      <td>2001</td>
      <td>1</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>43.0</td>
    </tr>
    <tr>
      <th>31712</th>
      <td>31713</td>
      <td>1</td>
      <td>21</td>
      <td>2001</td>
      <td>1</td>
      <td>PB</td>
      <td>M</td>
      <td>29.0</td>
      <td>44.0</td>
    </tr>
    <tr>
      <th>31713</th>
      <td>31714</td>
      <td>1</td>
      <td>21</td>
      <td>2001</td>
      <td>1</td>
      <td>DO</td>
      <td>M</td>
      <td>34.0</td>
      <td>53.0</td>
    </tr>
    <tr>
      <th>31714</th>
      <td>31715</td>
      <td>1</td>
      <td>21</td>
      <td>2001</td>
      <td>2</td>
      <td>OT</td>
      <td>M</td>
      <td>20.0</td>
      <td>27.0</td>
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
<p>3839 rows × 9 columns</p>

The combined dataframe includes all rows from both dataframes.

In some cases, the exact columns may change from year to year even
within the same project. For example, researchers may decide to add an
additional column to track a new piece of data or to provide a quality
check. If a column is present in only one dataset, you can still
concatenate the datasets. Any column that does not appear in a given
dataset will be set to NaN for those rows in the combined dataframe.

To illustrate this, we'll add a validated column to the 2002 survey,
then re-run `pd.concat()`:

```python
surveys_2002["validated"] = True

surveys_2001_2002 = pd.concat([surveys_2001, surveys_2002])
surveys_2001_2002
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
      <th>validated</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>31710</th>
      <td>31711</td>
      <td>1</td>
      <td>21</td>
      <td>2001</td>
      <td>1</td>
      <td>PB</td>
      <td>F</td>
      <td>26.0</td>
      <td>25.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>31711</th>
      <td>31712</td>
      <td>1</td>
      <td>21</td>
      <td>2001</td>
      <td>1</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>43.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>31712</th>
      <td>31713</td>
      <td>1</td>
      <td>21</td>
      <td>2001</td>
      <td>1</td>
      <td>PB</td>
      <td>M</td>
      <td>29.0</td>
      <td>44.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>31713</th>
      <td>31714</td>
      <td>1</td>
      <td>21</td>
      <td>2001</td>
      <td>1</td>
      <td>DO</td>
      <td>M</td>
      <td>34.0</td>
      <td>53.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>31714</th>
      <td>31715</td>
      <td>1</td>
      <td>21</td>
      <td>2001</td>
      <td>2</td>
      <td>OT</td>
      <td>M</td>
      <td>20.0</td>
      <td>27.0</td>
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
      <td>True</td>
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
      <td>True</td>
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
      <td>True</td>
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
      <td>True</td>
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
      <td>True</td>
    </tr>
  </tbody>
</table>
<p>3839 rows × 10 columns</p>

As expected, the validated column has a value of NaN for the 2001 data
in the combined dataframe.

## Joining and splitting columns

Sometimes we'd like to combine values from two or more columns into a
single column. For example, we might want to refer to the species in
each record by both its genus and species names. In Python, we use the
`+` operator to concatenate (or join) strings, and pandas works the same
way:

```python
species["genus_species"] = species["genus"] + " " + species["species"]
species["genus_species"]
```

```{.output}
0                Amphispiza bilineata
1            Ammospermophilus harrisi
2               Ammodramus savannarum
3                     Baiomys taylori
4     Campylorhynchus brunneicapillus
5             Calamospiza melanocorys
6                 Callipepla squamata
7                 Crotalus scutalatus
8                Cnemidophorus tigris
9             Cnemidophorus uniparens
10                   Crotalus viridis
11                 Dipodomys merriami
12                    Dipodomys ordii
13              Dipodomys spectabilis
14                      Dipodomys sp.
15                  Eumeces obsoletus
16                     Gambelia silus
17                   Neotoma albigula
18                        Neotoma sp.
19              Onychomys leucogaster
20                 Onychomys torridus
21                      Onychomys sp.
22                Chaetodipus baileyi
23                   Pipilo chlorurus
24                Peromyscus eremicus
25                 Perognathus flavus
26                Pooecetes gramineus
27               Perognathus hispidus
28            Chaetodipus intermedius
29                Peromyscus leucopus
30             Peromyscus maniculatus
31           Chaetodipus penicillatus
32                      Pipilo fuscus
33                    Chaetodipus sp.
34         Reithrodontomys fulvescens
35          Reithrodontomys megalotis
36           Reithrodontomys montanus
37                Reithrodontomys sp.
38               Sylvilagus audubonii
39                   Spizella breweri
40                  Sceloporus clarki
41               Sigmodon fulviventer
42                  Sigmodon hispidus
43              Sigmodon ochrognathus
44             Spermophilus spilosoma
45          Spermophilus tereticaudus
46               Sceloporus undulatus
47                       Sigmodon sp.
48                         Lizard sp.
49                         Pipilo sp.
50                         Rodent sp.
51                        Sparrow sp.
52             Zonotrichia leucophrys
53                   Zenaida macroura
Name: genus_species, dtype: object
```

Note that the `+` operator is also used to add numeric columns. In
Python, the same operator can be used to perform different operations
for different data types (but keep reading for an important caveat.)

Another common need is to join or split dates. In the ecology dataset,
the date is split across year, month, and day columns. However, pandas
has a special data type, `datetime64`, for representing dates that is
useful for plotting, comparing, and resampling time series data. To make
use of that functionality, we can concatenate the date columns and
convert them to a datetime object. For clarity, we'll use an unambiguous
date format: YYYY-MM-DD.

We need to perform an additional step before combining the date columns.
Year, month, and day are all stored as integers in our dataframe
(specifically, they use the `int64` data type). If we try to concatenate
them as they are, we'll receive an error. This is because the `+`
operator only works when each object has a similar type, that is, all
objects are either the same type or can be coerced to a common type
(like `int` and `float`, which are distinct types that generally play
well together). In this case, the columns are integers and the hyphens
are strings. pandas cannot determine exactly how the user wants to
combine the values, so it gives an error.

To resolve the error, we can use the `astype()` method to convert each
column to a string before combining the columns:

```python
year = surveys["year"].astype(str)
month = surveys["month"].astype(str)
day = surveys["day"].astype(str)

surveys["date"] = year + "-" + month + "-" + day
surveys["date"]
```

```{.output}
0         1977-7-16
1         1977-7-16
2         1977-7-16
3         1977-7-16
4         1977-7-16
            ...    
35544    2002-12-31
35545    2002-12-31
35546    2002-12-31
35547    2002-12-31
35548    2002-12-31
Name: date, Length: 35549, dtype: object
```

Note that some of the dates look a little funny because single-digit
days and months do not include a leading zero. For example, in the first
row we have **1977-7-16** instead of **1977-07-16**. This is usually not
a big deal but can be neatened up using the `str` accessor.

In pandas, an accessor is an attribute that provides additional
functionality to an object. Here, the `str` accessor allows us to access
many of the methods from the built-in `str` data type, including
`zfill()`, which pads a string to a given length by adding zeroes to the
start of the string:

```python
text = "2"
text.zfill(3)
```

```{.output}
'002'
```

Using the `str` accessor, we can use that method to zero-pad the data
in a `Series`:

```python
# Pad month and day to two characters
month = month.str.zfill(2)
day = day.str.zfill(2)

surveys["date"] = year + "-" + month + "-" + day
surveys["date"]
```

```{.output}
0        1977-07-16
1        1977-07-16
2        1977-07-16
3        1977-07-16
4        1977-07-16
            ...    
35544    2002-12-31
35545    2002-12-31
35546    2002-12-31
35547    2002-12-31
35548    2002-12-31
Name: date, Length: 35549, dtype: object
```

The month and date values in date are now padded to a length of two,
allowing us to create a well-formed YYYY-MM-DD date string. Other string
methods, like `upper()` and `lower()`, can be used in the same way.

Before we convert the date column to a datetime, we're going to use the
date string to show the opposite operation: Splitting a value stored in
one column into multiple columns. One way to do this in pandas is to use
`str.split()`, which splits each value in a series based on a
*delimiter*, a character used as a boundary between parts of a string.
Here, a hyphen is used to delimit the year, month, and date in each
date. By splitting the column on a hyphen, we can extract each of those
components into its own column. We also pass `True` to the *expand*
keyword argument, which makes the `str.split()` method return a
dataframe:

```python
surveys["date"].str.split("-", expand=True)
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1977</td>
      <td>07</td>
      <td>16</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1977</td>
      <td>07</td>
      <td>16</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1977</td>
      <td>07</td>
      <td>16</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1977</td>
      <td>07</td>
      <td>16</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1977</td>
      <td>07</td>
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

Now let's go ahead and convert our date column into a datetime object
using `pd.to_datetime()`:

```python
surveys["date"] = pd.to_datetime(surveys["date"])
surveys["date"]
```

```{.output}
0       1977-07-16
1       1977-07-16
2       1977-07-16
3       1977-07-16
4       1977-07-16
           ...    
35544   2002-12-31
35545   2002-12-31
35546   2002-12-31
35547   2002-12-31
35548   2002-12-31
Name: date, Length: 35549, dtype: datetime64[ns]
```

::: challenge ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

pandas can help us ask specific questions which we want to answer about
our data. The real skill is to know how to translate our scientific
questions into a sensible approach (and subsequently visualize and
interpret our results).

Try using pandas to answer the following questions.

1.  How many specimens of each sex are there for each year,
    including those whose sex is unknown?
2.  What is the average weight of each taxa?
3.  What are the minimum, maximum and average weight for each
    species of Rodent?
4.  What is the average hindfoot length for male and female rodent
    of each species? Is there a male/female difference?
5.  What is the average weight of each rodent species over the
    course of the years? Is there any noticeable trend for any of
    the species?

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### Show me the solution to challenge 1

How many specimens of each sex are there for each year, including those
whose sex is unknown?

```python
# Fill in NaN values in sex with U
surveys["sex"] = surveys["sex"].fillna("U")

# Count records by sex
result = surveys.groupby(["year", "sex"])["record_id"].count()

# Use the option_context context manager to show all rows
with pd.option_context("display.max_rows", None):
    print(result)
```

```{.output}
year  sex
1977  F       204
      M       214
      U        85
1978  F       503
      M       433
      U       112
1979  F       327
      M       324
      U        68
1980  F       605
      M       727
      U        83
1981  F       631
      M       745
      U        96
1982  F       823
      M      1027
      U       128
1983  F       771
      M       797
      U       105
1984  F       445
      M       443
      U        93
1985  F       636
      M       716
      U        86
1986  F       414
      M       455
      U        73
1987  F       677
      M       862
      U       132
1988  F       604
      M       737
      U       128
1989  F       678
      M       780
      U       111
1990  F       581
      M       636
      U        94
1991  F       606
      M       637
      U       104
1992  F       443
      M       477
      U       118
1993  F       285
      M       380
      U        85
1994  F       243
      M       327
      U        98
1995  F       574
      M       534
      U       114
1996  F       725
      M       910
      U        71
1997  F      1071
      M      1357
      U        65
1998  F       717
      M       798
      U        95
1999  F       545
      M       530
      U        60
2000  F       690
      M       779
      U        83
2001  F       743
      M       744
      U       123
2002  F      1149
      M       979
      U       101
Name: record_id, dtype: int64

```

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### Show me the solution to challenge 2

What is the average weight of each taxa?

```python
# Create the merged dataframe
merged = pd.merge(surveys, species, how="left")

# Group by taxa
grouped = merged.groupby("taxa")

# Calculate the min, max, and mean weight
grouped["weight"].mean()
```

```{.output}
taxa
Bird             NaN
Rabbit           NaN
Reptile          NaN
Rodent     42.672428
Name: weight, dtype: float64
```

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### Show me the solution to challenge 3

What are the minimum, maximum and average weight for each species of
Rodent?

```python
# Create the merged dataframe
merged = pd.merge(surveys, species, how="left")

# Limit merged dataframe to rodents
rodents = merged[merged["taxa"] == "Rodent"]

# Group rodents by species
grouped = rodents.groupby("species_id")

# Calculate the min, max, and mean weight
grouped.agg({"weight": ["min", "max", "mean"]})
```

<style>
  table.dataframe tbody tr:hover { background-color: #ccffff !important; }
  table.dataframe tr:nth-child(even) { background-color: #f5f5f5; }
  table.dataframe th { text-align: right; font-weight: bold; }
  table.dataframe td { text-align: right; }
</style>

<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">weight</th>
    </tr>
    <tr>
      <th></th>
      <th>min</th>
      <th>max</th>
      <th>mean</th>
    </tr>
    <tr>
      <th>species_id</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>AH</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>BA</th>
      <td>6.0</td>
      <td>18.0</td>
      <td>8.600000</td>
    </tr>
    <tr>
      <th>DM</th>
      <td>10.0</td>
      <td>66.0</td>
      <td>43.157864</td>
    </tr>
    <tr>
      <th>DO</th>
      <td>12.0</td>
      <td>76.0</td>
      <td>48.870523</td>
    </tr>
    <tr>
      <th>DS</th>
      <td>12.0</td>
      <td>190.0</td>
      <td>120.130546</td>
    </tr>
    <tr>
      <th>DX</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>NL</th>
      <td>30.0</td>
      <td>280.0</td>
      <td>159.245660</td>
    </tr>
    <tr>
      <th>OL</th>
      <td>10.0</td>
      <td>56.0</td>
      <td>31.575258</td>
    </tr>
    <tr>
      <th>OT</th>
      <td>5.0</td>
      <td>46.0</td>
      <td>24.230556</td>
    </tr>
    <tr>
      <th>OX</th>
      <td>18.0</td>
      <td>24.0</td>
      <td>21.000000</td>
    </tr>
    <tr>
      <th>PB</th>
      <td>12.0</td>
      <td>55.0</td>
      <td>31.735943</td>
    </tr>
    <tr>
      <th>PE</th>
      <td>8.0</td>
      <td>40.0</td>
      <td>21.586508</td>
    </tr>
    <tr>
      <th>PF</th>
      <td>4.0</td>
      <td>25.0</td>
      <td>7.923127</td>
    </tr>
    <tr>
      <th>PH</th>
      <td>18.0</td>
      <td>48.0</td>
      <td>31.064516</td>
    </tr>
    <tr>
      <th>PI</th>
      <td>17.0</td>
      <td>21.0</td>
      <td>19.250000</td>
    </tr>
    <tr>
      <th>PL</th>
      <td>8.0</td>
      <td>27.0</td>
      <td>19.138889</td>
    </tr>
    <tr>
      <th>PM</th>
      <td>7.0</td>
      <td>49.0</td>
      <td>21.364155</td>
    </tr>
    <tr>
      <th>PP</th>
      <td>4.0</td>
      <td>74.0</td>
      <td>17.173942</td>
    </tr>
    <tr>
      <th>PX</th>
      <td>18.0</td>
      <td>20.0</td>
      <td>19.000000</td>
    </tr>
    <tr>
      <th>RF</th>
      <td>9.0</td>
      <td>20.0</td>
      <td>13.386667</td>
    </tr>
    <tr>
      <th>RM</th>
      <td>4.0</td>
      <td>29.0</td>
      <td>10.585010</td>
    </tr>
    <tr>
      <th>RO</th>
      <td>8.0</td>
      <td>13.0</td>
      <td>10.250000</td>
    </tr>
    <tr>
      <th>RX</th>
      <td>11.0</td>
      <td>20.0</td>
      <td>15.500000</td>
    </tr>
    <tr>
      <th>SF</th>
      <td>24.0</td>
      <td>199.0</td>
      <td>58.878049</td>
    </tr>
    <tr>
      <th>SH</th>
      <td>16.0</td>
      <td>140.0</td>
      <td>73.148936</td>
    </tr>
    <tr>
      <th>SO</th>
      <td>15.0</td>
      <td>105.0</td>
      <td>55.414634</td>
    </tr>
    <tr>
      <th>SS</th>
      <td>57.0</td>
      <td>130.0</td>
      <td>93.500000</td>
    </tr>
    <tr>
      <th>ST</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>UR</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### Show me the solution to challenge 4

What is the average hindfoot length for male and female rodent of each
species? Is there a male/female difference?

```python
# Create the merged dataframe
merged = pd.merge(surveys, species, how="left")

# Limit merged dataframe to rodents
rodents = merged[merged["taxa"] == "Rodent"]

# Group rodents by species and sex
grouped = rodents.groupby(["species_id", "sex"])

# Calculate the mean hindfoot length, plus count and standard deviation
# to better assess the question
with pd.option_context("display.max_rows", None):
    print(grouped["hindfoot_length"].agg(["count", "mean", "std"]))
```

```{.output}
                count       mean        std
species_id sex                             
AH         M        0        NaN        NaN
           U        2  33.000000   2.828427
BA         F       31  13.161290   1.529636
           M       14  12.642857   2.097880
           U        0        NaN        NaN
DM         F     4302  35.712692   1.433067
           M     5658  36.188229   1.455396
           U       12  35.583333   0.996205
DO         F     1244  35.486334   1.726414
           M     1640  35.698780   1.611656
           U        3  36.000000   0.000000
DS         F     1046  49.583174   1.973573
           M     1083  50.301939   2.128120
           U        3  50.000000   1.732051
DX         U        0        NaN        NaN
NL         F      620  32.024194   1.669181
           M      452  32.577434   1.903603
           U        2  52.000000  25.455844
OL         F      438  20.287671   1.101022
           M      480  20.758333   1.651195
           U        2  20.000000   0.000000
OT         F     1019  20.281649   1.519412
           M     1115  20.257399   1.087354
           U        5  19.600000   1.140175
OX         F        3  19.666667   1.154701
           M        5  18.800000   3.346640
           U        0        NaN        NaN
PB         F     1645  25.882675   0.928842
           M     1213  26.431987   1.444130
           U        6  26.166667   0.983192
PE         F      544  20.272059   1.156084
           M      666  20.132132   1.177721
           U        2  20.500000   0.707107
PF         F      721  15.550624   1.381627
           M      770  15.620779   1.142208
           U        2  13.000000   4.242641
PH         F       20  25.900000   1.293709
           M       11  25.545455   1.752920
PI         M        8  22.500000   0.534522
           U        1  20.000000        NaN
PL         F       16  19.750000   2.720294
           M       19  20.263158   0.933459
           U        1  20.000000        NaN
PM         F      361  20.279778   1.162782
           M      483  20.530021   1.275621
           U        3  21.333333   4.041452
PP         F     1574  21.676620   1.316529
           M     1444  21.838643   1.201006
           U        9  20.888889   2.027588
PX         F        1  19.000000        NaN
           M        1  20.000000        NaN
           U        0        NaN        NaN
RF         F       55  17.527273   0.813191
           M       18  17.500000   0.985184
RM         F     1133  16.391880   1.123946
           M     1296  16.491512   1.134202
           U       13  15.846154   2.444250
RO         F        4  14.750000   0.957427
           M        4  16.000000   1.154701
RX         M        2  18.500000   2.121320
SF         F       16  27.500000   2.683282
           M       23  26.347826   3.524056
           U        2  24.500000   0.707107
SH         F       71  29.028169   2.298893
           M       60  27.983333   2.801281
           U        0        NaN        NaN
SO         F       30  25.633333   4.139660
           M       11  25.727273   1.954017
SS         F        0        NaN        NaN
           M        0        NaN        NaN
           U        0        NaN        NaN
ST         U        0        NaN        NaN
UR         U        0        NaN        NaN

```

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### Show me the solution to challenge 5

What is the average weight of each rodent species over the course of the
years? Is there any noticeable trend for any of the species?

```python
# Create the merged dataframe
merged = pd.merge(surveys, species, how="left")

# Limit merged dataframe to rodents
rodents = merged[merged["taxa"] == "Rodent"]

# Group rodents by species and year
grouped = rodents.groupby(["species_id", "year"])

# Calculate the mean weight by year
result = grouped["weight"].mean()

# Use the option_context context manager to show all rows
with pd.option_context("display.max_rows", None):
    print(result)
```

```{.output}
species_id  year
AH          1978           NaN
            1982           NaN
            1983           NaN
            1984           NaN
            1985           NaN
            1986           NaN
            1987           NaN
            1988           NaN
            1989           NaN
            1990           NaN
            1991           NaN
            1992           NaN
            1993           NaN
            1994           NaN
            1995           NaN
            1996           NaN
            1997           NaN
            1998           NaN
            1999           NaN
            2000           NaN
            2001           NaN
            2002           NaN
BA          1989      7.000000
            1990      8.000000
            1991      9.240000
            1992      7.833333
DM          1977     41.141304
            1978     40.795455
            1979     43.507317
            1980     44.136082
            1981     44.032907
            1982     41.975042
            1983     40.944551
            1984     40.765306
            1985     41.507645
            1986     43.361596
            1987     43.232609
            1988     43.397790
            1989     44.349206
            1990     41.769912
            1991     43.148338
            1992     43.877966
            1993     43.373984
            1994     42.373288
            1995     44.806147
            1996     44.506173
            1997     44.708551
            1998     43.131403
            1999     43.945402
            2000     43.126638
            2001     45.442177
            2002     46.168317
DO          1977     42.666667
            1978     45.000000
            1979     45.862069
            1980     48.058824
            1981     49.111111
            1982     47.919643
            1983     47.150602
            1984     48.415094
            1985     47.956731
            1986     49.372727
            1987     50.087379
            1988     51.463768
            1989     51.025641
            1990     48.512048
            1991     49.695652
            1992     48.367816
            1993     48.461538
            1994     47.750000
            1995     49.592593
            1996     47.234940
            1997     48.177866
            1998     49.731183
            1999     48.012048
            2000     49.224719
            2001     52.233766
            2002     49.514403
DS          1977    121.437500
            1978    115.198653
            1979    111.796954
            1980    120.725664
            1981    125.818444
            1982    115.647929
            1983    122.033088
            1984    124.082192
            1985    124.326316
            1986    128.071429
            1987    126.383838
            1988    129.490566
            1989    121.896552
            1990    121.187500
            1991    113.000000
            1992    112.352941
            1993    105.722222
            1994    106.625000
            1997    111.000000
            1998    116.000000
            1999    120.714286
DX          1980           NaN
            1983           NaN
            1986           NaN
            1988           NaN
            1991           NaN
            1992           NaN
            1993           NaN
            1994           NaN
            1995           NaN
            1996           NaN
            1998           NaN
            1999           NaN
            2000           NaN
            2001           NaN
            2002           NaN
NL          1977           NaN
            1978    184.656250
            1979    138.000000
            1980    158.982143
            1981    165.903226
            1982    160.613208
            1983    156.691489
            1984    150.095238
            1985    148.829268
            1986    159.724138
            1987    158.840000
            1988    163.104167
            1989    151.278689
            1990    154.275862
            1991    148.785714
            1992    139.000000
            1993    127.391304
            1994    186.875000
            1995    155.833333
            1996    148.000000
            1997    150.688889
            1998    159.466667
            1999    182.200000
            2000    179.307692
            2001    167.851064
            2002    182.159091
OL          1977     21.666667
            1978     31.027027
            1979     33.717391
            1980     33.107143
            1981     33.296296
            1982     35.590361
            1983     34.584615
            1984     32.550725
            1985     32.108696
            1986     30.880952
            1987     30.779221
            1988     30.306122
            1989     31.947368
            1990     31.200000
            1991     28.171429
            1992     28.454545
            1993     27.545455
            1994     21.900000
            1995     27.296296
            1996     27.769231
            1997     33.625000
            2002     25.428571
OT          1977     21.000000
            1978     23.220000
            1979     23.075758
            1980     24.083333
            1981     24.415385
            1982     24.925532
            1983     24.697674
            1984     22.416667
            1985     22.064516
            1986     21.500000
            1987     23.069767
            1988     24.070588
            1989     24.663366
            1990     23.675325
            1991     24.588235
            1992     24.928571
            1993     22.363636
            1994     25.285714
            1995     24.868421
            1996     23.453704
            1997     24.785156
            1998     24.675676
            1999     25.723810
            2000     25.303448
            2001     23.707792
            2002     23.833333
OX          1977     21.333333
            1978           NaN
            1982     24.000000
            1984     18.000000
            1989     20.000000
            1993           NaN
PB          1995     34.000000
            1996     32.578947
            1997     31.085603
            1998     30.082237
            1999     31.710037
            2000     30.878899
            2001     32.798851
            2002     32.359447
PE          1977     19.500000
            1978     20.428571
            1979     20.529412
            1980     22.450000
            1981     20.558140
            1982     21.173077
            1983     20.864865
            1984     20.210526
            1985     20.360000
            1986     22.520000
            1987     21.625899
            1988     22.625668
            1989     21.935673
            1990     21.671233
            1991     21.435484
            1992     22.750000
            1993     19.230769
            1994     18.000000
            1995     21.230769
            1996     22.027778
            1997     20.929825
            1998     20.304348
            1999     25.428571
            2000     21.615385
            2001     20.400000
            2002     21.719298
PF          1977      7.173913
            1978      7.088235
            1979      7.529412
            1980      7.455556
            1981      7.152542
            1982      6.918919
            1983      6.833333
            1984      7.428571
            1985           NaN
            1986      8.000000
            1987      7.500000
            1988      8.000000
            1989      7.230769
            1990      7.117647
            1991      7.827586
            1992      8.767857
            1993      8.238806
            1994      7.855072
            1995      8.780645
            1996      8.393846
            1997      8.448649
            1998      8.720000
            2001      8.538462
            2002      7.388889
PH          1984     28.000000
            1985     32.666667
            1986     39.000000
            1988     33.000000
            1989     30.500000
            1990     31.142857
            1992     31.142857
            1995     35.333333
            1997     22.000000
PI          1992     18.000000
            1995           NaN
            2001     18.000000
            2002     20.000000
PL          1995     22.333333
            1996     21.166667
            1997     18.789474
            1998     16.714286
            2000     21.000000
PM          1978     20.666667
            1979     23.666667
            1980     21.000000
            1981     19.933333
            1982     21.391304
            1983     22.023810
            1984     19.545455
            1985     19.000000
            1986     21.696970
            1987     22.297710
            1988     21.759259
            1989     20.222222
            1995     27.375000
            1996     20.224490
            1997     21.126394
            1998     20.591398
            1999     22.523810
            2000     20.500000
            2001     26.666667
            2002     19.000000
PP          1977     15.333333
            1978     14.869565
            1979     15.105263
            1980     14.176471
            1981     13.950000
            1982     16.125000
            1983     15.468750
            1984     15.307692
            1985     15.764706
            1986     16.750000
            1987     17.840909
            1988     18.280000
            1989     17.409091
            1990     16.029412
            1991     17.904762
            1992     17.479675
            1993     17.954023
            1994     17.585714
            1995     16.844444
            1996     18.095563
            1997     18.175000
            1998     16.266990
            1999     16.521212
            2000     16.788618
            2001     17.752896
            2002     17.018617
PX          1996           NaN
            1997     19.000000
            1998           NaN
            2000           NaN
RF          1982     11.500000
            1988     13.818182
            1989     13.346939
            1990     12.916667
            1997     20.000000
RM          1977     10.000000
            1978      7.500000
            1979      8.333333
            1980     10.227273
            1981     11.178571
            1982     10.436242
            1983      9.872000
            1984     11.152542
            1985      8.371429
            1986     10.750000
            1987     10.657609
            1988     10.322115
            1989     10.411311
            1990     10.305677
            1991     10.498305
            1992     10.904762
            1993     10.747475
            1994     10.675000
            1995     12.653846
            1996     11.455556
            1997     11.230769
            1998     13.100000
            1999     10.555556
            2000     11.400000
            2001     11.333333
            2002     10.000000
RO          1991     11.000000
            2002     10.142857
RX          1995     20.000000
            1997     11.000000
SF          1989     54.800000
            1990     52.611111
            1991     93.166667
            1992     43.000000
            1993     44.000000
            2002     62.166667
SH          1977           NaN
            1978     89.000000
            1982     79.000000
            1983           NaN
            1986     55.000000
            1987     73.800000
            1988     72.806452
            1989     76.345455
            1990     76.888889
            1991     63.000000
            1997     50.857143
            1999     54.000000
            2000     73.375000
            2001     79.900000
            2002     64.666667
SO          1991     53.909091
            1992     55.263158
            1993     55.600000
            1994     62.333333
            1997     54.666667
SS          1977           NaN
            1978    130.000000
            1979           NaN
            1980           NaN
            1981     57.000000
            1982           NaN
            1983           NaN
            1984           NaN
            1985           NaN
            1986           NaN
            1987           NaN
            1988           NaN
            1989           NaN
            1990           NaN
            1991           NaN
            1992           NaN
            1993           NaN
            1994           NaN
            1995           NaN
            1996           NaN
            1997           NaN
            1998           NaN
            1999           NaN
            2000           NaN
            2001           NaN
            2002           NaN
ST          1993           NaN
UR          1987           NaN
            1988           NaN
            1991           NaN
            1992           NaN
            1994           NaN
            2001           NaN
            2002           NaN
Name: weight, dtype: float64

```

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: keypoints ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   Combine two dataframes on one or more common values using
    `pd.merge()`
-   Append rows from one dataframe to another using `pd.concat()`
-   Combine multiple text columns into one using the `+` operator
-   Use the `str` accessor to use string methods like `split()` and
    `zfill()` on text columns
-   Convert date strings to datetime objects using
    `pd.to_datetime()`

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
