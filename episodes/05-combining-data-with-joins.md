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
Fortunately, `pandas` provides the `merge()` method to join two
dataframes.

To merge the surveys and species dataframes, use:

```python
merged = surveys.merge(species)
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
wanted to merge the dataframes together, so pandas made an educated
guess. It looked at the columns in each of the dataframes, then merged
them based on the columns that appear in both. Here, the only shared
name is species_id. If we want to control what columns are used to
merge, we can use the *on* keyword argument:

```python
surveys.merge(species, on="species_id")
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
them using `pd.concat()`, which stacks the dataframes horizontally (that
is, it appends the 2002 dataset to the 2001 dataset):

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
concatenate the datasets. Any column that does not appear in one of the
datasets will be set to NaN for those rows in the combined dataframe.

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

As expected, validated has a value of NaN for the 2001 data in the
combined dataframe.
