python-ecology-lesson-alt
=========================

This is the lesson repository for python-ecology-lesson-alt. It adapts
the [Carpentries
Workbench](https://carpentries.github.io/sandpaper-docs/instructor/index.html)
R Markdown template to work with Python and allows lesson content to be
created and edited using JupyterLab.

**The Carpentries Workbench is still experimental, and this project is
itself very much a work in progress.**

To get started, first clone the repo:

    git clone https://github.com/adamancer/python-ecology-lesson-alt
    cd python-ecology-lesson-alt
    conda env create --file environment.yml

Then open the project folder using JupyterLab:

    conda activate py-lesson-dev
    jupyter-lab

Creating and editing episodes
-----------------------------

The Jupyter notebooks live in the notebooks folder. Each notebook can be
formatted more or less normally with a mix of markdown and code blocks.
Code cells will appear in the lesson website as input plus output, while
markdown cells are interpreted as normal text or fences.

Use
[create_markdown_from_notebooks.ipynb](https://github.com/adamancer/python-ecology-lesson-alt/blob/main/create_markdown_from_notebooks.ipynb)
to generate markdown files for each notebook. Markdown files are saved
to the episodes folder, unless there is a notebook named
**setup.ipynb**, which creates the index page for the lesson and is
saved to the learners folder.

### Notebook structure

-   Notebooks must use hashes for headers
-   The first H1 tag will be the title of the episode. There should be
    only one H1 tag and it should be at the top of the document.

### Using fences

The Carpentries Workbench uses fenced divs to highlight challenges,
callouts, and other content that authors want to emphasize. Notebooks
can use a mix of headers and tags to identify fences. Guidance for
formatting fences includes:

-   Each fence should start in a new cell
-   If a cell has a header matching one of the fence types, it will be
    interpreted as a fence. Header level does not matter, and the header
    will be omitted when that cell is printed. If you save a Notebook
    object as a Jupyter notebook, it will update fence cells that have
    not been tagged with the name of the fence.
-   Sometimes fences need to be broken into multiple cells (for example,
    if you want to mix markdown and code blocks). You can combine
    adjacent cells into a single fence by adding the continue tag to
    each cell you want to include.
-   The solution fence type should be nested inside another fence.
    Solution fences are automatically appended to the previous cell,
    which should always be a fence. They can still use the continue tag
    to combine markdown and code cells, for example, to provide a custom
    title for the dropdown.

Generating the lesson locally
-----------------------------

When changes to the repo are pushed to git, the Carpentries Workbench
creates or updates a GitHub Page automatically. You can also generate
the lesson website locally using sandpaper. You will need git,
Miniconda, and RStudio to create the lesson.

### Setup

Using the Anaconda Prompt or a built-in command prompt, create the
py-lesson-dev environment:

    git clone https://github.com/adamancer/python-ecology-lesson-alt
    cd python-ecology-lesson-alt
    conda env create --file environment

After the environment is in place, open RStudio using the Rprog file in
the project directory and install sandpaper:

``` r
options(repos = c(
  carpentries = "https://carpentries.r-universe.dev/",
  CRAN = "https://cran.rstudio.com/"
))
install.packages("sandpaper", dep = TRUE)
```

### Generate the lesson

To generate a local copy of the lesson, run the following in the RStudio
project:

``` r
sandpaper::build_lesson()
```

To build the lesson from scratch, use:

``` r
sandpaper::reset_site()
```
