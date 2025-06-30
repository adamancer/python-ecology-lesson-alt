---
title: Setup
---

This lesson uses Python to analyze and visualize data from an ecology
dataset. It was adapted (and currently includes huge chunks of text
lifted directly from) [Data Management with SQL for
Ecologists](https://datacarpentry.org/sql-ecology-lesson/) and covers
similar material to [Data Analysis and Visualization in Python for
Ecologists](https://datacarpentry.org/python-ecology-lesson/). The idea
was to create parallel lessons for SQL and Python for use by the
Smithsonian Carpentries.

This lesson is designed to use Jupyter notebooks, an interactive
development environment widely used for doing data science with Python.
**The rest of this page provides instructions for setting up the
software and data needed to complete this lesson. Please complete setup
prior to your scheduled lesson.**

## Setup

This lesson requires two pieces of software: Visual Studio Code and
Miniforge.

### Visual Studio Code

Visual Studio Code, also known as VS Code, is a code editor developed by
Microsoft.

1.  Download the [VS Code
    installer](https://code.visualstudio.com/download)
2.  Run the installer

### Miniforge

Miniforge is a package manager used to manage software related to
Python. To install:

1.  Download the Miniforge installer for your system from
    [conda-forge](https://conda-forge.org/download/)
    - **Windows:** Choose the User Installer version
2.  Run the installer

::: callout ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#### Anaconda

You may already be familiar with Anaconda, which includes similar
package management software as Miniforge and a whole lot more. We
**strongly recommend** sticking to the installation instructions and
software presented here for this training. The Anaconda distribution
includes additional programs that may affect the output of some of the
code presented in this lesson, which can be confusing for people new to
Python.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### Setting up the Python environment

Once Miniforge is installed, you're ready to set up the Python
environment. You'll need to use a command-line interface, or CLI, to do
so. A CLI is an application that runs commands that are provided as
text. Examples of command-line interfaces include the Windows command
prompt and Unix shells, including bash. We'll be using the CLI to
install and run JupyterLab.

Each operating system has one or more command-line interfaces available.
We recommend using the following applications for this lesson:

- **Windows:** Use the Miniforge Prompt, which was installed as part of
  Miniforge. You can find it by searching for Miniforge Prompt in the
  search box on the Windows toolbar.
- **macOS:** Use the Terminal. You can find it in the
  Applications/Utilities folder or by searching for Terminal using
  Spotlight.

Type or copy the following command into the CLI to set up the
environment:

mamba create --name python-ecology-lesson ipykernel pandas plotly jupyterlab

### Downloading data to the lesson folder

This lesson uses specific data files from the [Portal Project Teaching
Database](https://figshare.com/articles/Portal_Project_Teaching_Database/1314459).
Here, we'll create the lesson folder and download the files we need for
the lesson.

1.  Create a folder called **python-ecology-lesson** on your desktop
2.  Create a folder called **data** inside the folder from step 1
3.  Download the following files into the data folder:
    - surveys.csv: https://figshare.com/ndownloader/files/10717177
    - species.csv: https://figshare.com/ndownloader/files/3299483
    - plots.csv: https://figshare.com/ndownloader/files/3299474

## Using VS Code

Find and open VS Code using the search interface in your operating
system.

1.  Click File \> Open Folder
2.  Select the **python-ecology-lesson** folder on your desktop

The contents of the folder should now appear in the left sidebar of the
VS Code window.

Your instructor will explain how to work with VS Code as part of the
lesson.
