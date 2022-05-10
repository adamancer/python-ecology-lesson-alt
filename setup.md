---
title: Setup
---

This lesson uses JupyterLab and pandas to analyze and visualize data
from an ecology dataset. It was adapted (and currently includes huge
chunks of text lifted directly from) [Data Management with SQL for
Ecologists](https://datacarpentry.org/sql-ecology-lesson/) and covers
similar material to [Data Analysis and Visualization in Python for
Ecologists](https://datacarpentry.org/python-ecology-lesson/). The idea
was to create parallel lessons for SQL and Python for use by the
Smithsonian Carpentries.

This lesson is designed to use JupyterLab, an interactive development
environment widely used for doing data science with Python. **The rest
of this page provides instructions for setting up the software and data
needed to complete this lesson. Please complete the setup prior to your
scheduled lesson.**

## Setup

We will use a program called Miniconda to set up JupyterLab, so first we
need to download and install [Miniconda (64
bit)](https://docs.conda.io/en/latest/miniconda.html).

### Using the command prompt

Once Miniconda is intalled, we can use the command prompt to install and
run JupyterLab. Each operating system has one or more command prompts
available. We recommend using the following applications for this
lesson:

-   **Windows:** Use the Anaconda Prompt, which was installed as
    part of Miniconda. You can
  find it by searching for Anaconda Prompt in the search box on the
Windows toolbar.

-   **macOS:** Use the Terminal. You can find it by searching for
    Terminal using Spotlight.

The commands given below may not work if a different command prompt
application is used, so we'd strongly encourage you to use the
recommended applications.

### Installing JupyterLab

Once the command prompt is open, run the following command to install
the software needed for this course:

```
conda create -c conda-forge --yes --name py-ecology altair jupyterlab
pandas
```

::: callout ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

To run any of the commands presented here, copy-paste them into the
command prompt, then press enter to run the command.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### Downloading data to the lesson folder

Create the lesson folder and download the necessary data as follows:

1.  Create a folder called **python-ecology-lesson** on your desktop
2.  Create a folder called **data** inside the folder created in
    step 1
3.  Download the following files into the data folder:
    -   surveys.csv:
        https://figshare.com/ndownloader/files/10717177
    -   species.csv:
        https://figshare.com/ndownloader/files/3299483

Alternatively, we can run the following commands in the command prompt
to create the lesson folders and download the necessary data:

```
cd ~/Desktop
mkdir python-ecology-lesson/data
cd python-ecology-lesson/data
wget -O surveys.csv https://figshare.com/ndownloader/files/10717177
wget -O species.csv https://figshare.com/ndownloader/files/3299483
```

## Running JupyterLab

Once JupyterLab has been installed, we can run it by opening the command
prompt and running the following commands:

```
conda activate python-ecology-lesson
cd ~/Desktop/python-ecology-lesson
jupyter-lab
```

JupyterLab should now open in a new browser window.

::: callout ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Try running this command before the scheduled lesson -- does JupyterLab
appear as expected?

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
