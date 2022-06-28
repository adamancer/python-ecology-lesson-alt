"""Defines command to create chapter markdown from Jupyter notebooks"""
import argparse
import base64
import glob
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile

import yaml


#: List of available fences
FENCES = {
    "callout",
    "challenge",
    "checklist",
    "discussion",
    "instructor",
    "keypoints",
    "objectives",
    "prereq",
    "questions",
    "solution",
    "testimonial",
    "continue",
}


class Cell:
    """Formats a notebook cell for a carpentries lesson"""

    lesson_root = "."
    md_format = "md"
    html_output = False

    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        if self.fence == self.title.lower():
            return "\n".join(self.text.splitlines()[1:]).strip()
        return self.text.strip()

    @property
    def cell_type(self):
        """Gets the value for cell_type from the cell_dict"""
        return self.cell["cell_type"]

    @property
    def source(self):
        """Gets and trimes the value for source from the cell_dict"""
        source = self.cell["source"]
        while source and not source[0].strip():
            del source[0]
        return source

    @property
    def tags(self):
        """Gets the value for metadata.tags from the cell_dict"""
        return self.cell["metadata"].get("tags", [])

    @tags.setter
    def tags(self, tags):
        self.cell["metadata"]["tags"] = tags

    @property
    def title(self):
        """Gets the text of a markdown header"""
        return self.header.lstrip("# ")

    @property
    def header(self):
        """Gets the header of a markdown cell"""
        if (
            self.cell_type == "markdown"
            and self.source
            and self.source[0].startswith("#")
        ):
            return self.source[0].rstrip()
        return ""

    @property
    def header_level(self):
        """Gets the header level"""
        return len(re.match("#*", self.header).group())

    @property
    def text(self):
        """Gets the text of the cell"""

        if "hide_input" in self.tags:
            return ""

        text = "".join(self.source)
        if self.cell_type == "code":
            return text

        # Wrap markdown using pandoc
        with tempfile.NamedTemporaryFile(
            "w", encoding="utf-8", suffix=".md", delete=False
        ) as f:
            f.write(text)
            path = f.name
        subprocess.run(
            ["pandoc", path, "-o", path, "-t", "markdown+yaml_metadata_block", "-s"]
        )
        with open(path, encoding="utf-8") as f:
            text = f.read().replace("``` ", "```").replace("```output", "```{.output}")
        os.remove(path)

        # Single space code blocks
        for code_block in re.findall("```.*?```", text, flags=re.DOTALL):
            text = text.replace(code_block, re.sub(r"\n+", "\n", code_block), 1)

        return re.sub(r"\n{2,}", "\n\n", text)

    @property
    def fence(self):
        """Gets the name of the fence"""
        fences = list(set(self.tags) & set(FENCES))
        other = list(set(self.tags) - set(FENCES))
        if not fences and self.title.lower() in FENCES:
            self.tags = [self.title.lower()] + other
            return self.tags[0]
        return fences[0] if fences else None

    @property
    def output(self):

        if "hide_output" in self.tags or not self.cell["outputs"]:
            return ""

        keys = ["image/png", "text/plain", "text"]
        if self.html_output:
            keys.insert(1, "text/html")

        output = []
        for row in self.cell["outputs"]:

            # Get the content of the row
            data = row.get("data", row)
            for key in keys:
                try:
                    content = data[key]
                    break
                except KeyError:
                    pass
            else:
                continue

            # Always output streamed text
            if row["output_type"] == "stream":
                output.append("".join(content))

            # Store image as file and output an image tag
            elif key.startswith("image"):
                img_bytes = base64.b64decode(content)
                filename = f"fig_output_{hashlib.md5(img_bytes).hexdigest()}.png"
                path = os.path.join(self.lesson_root, "episodes", "fig", filename)
                try:
                    open(path)
                except FileNotFoundError:
                    with open(path, "wb") as f:
                        f.write(img_bytes)
                output.append(
                    f'<img src="fig/{filename}" width="672" style="display: block; margin: auto;" />'
                )

            # Pretty print HTML if possible. This is just for pandas tables so far.
            elif key == "text/html":

                # Check for pandas tables
                pattern = r"<div.*?>\s*<style.*?</style>\s*(.*)\s*</div>"
                if re.match(pattern, "".join(content), flags=re.DOTALL):

                    # Approximate the style of a pandas table
                    style = (
                        "<style>\n"
                        "  table.dataframe tbody tr:hover { background-color: #ccffff !important; }\n"
                        "  table.dataframe tr:nth-child(even) { background-color: #f5f5f5; }\n"
                        "  table.dataframe th { text-align: right; font-weight: bold; }\n"
                        "  table.dataframe td { text-align: right; }\n"
                        "</style>\n\n"
                    )

                    output.append(
                        style
                        + re.search(pattern, "".join(content), flags=re.DOTALL).group(1)
                    )

                else:
                    # Output non-table HTML
                    output.append("".join(content))

            # Output text inside output fence
            else:
                output.append("".join(content))

        # Wrap non-HTML output in an output fence
        if not re.search(r"</[a-z]+>", output[0]):
            output.insert(0, "```{.output}")

            for i, content in enumerate(output[1:]):
                if re.search(r"</[a-z]+>", content):
                    output[i + 1] = "```\n\n" + content
                    break
            else:
                output.append("```")

        return "\n".join(output)

    def is_part_of(self, block, always_part=None):
        """Checks if a cell is part of another block

        Parameters
        ----------
        block : Block
            the preceding block in the notebook
        always_part : list
            fence names that are always part of the preceding block

        Returns
        -------
        bool
            True if cell if part of the preceding block
        """
        return (
            self.fence == "continue"
            or always_part
            and self.fence in always_part
            or not block.fence
            and not self.fence
            and block.cell_type == self.cell_type
        )

    def to_markdown(self, include_fence=True):
        """Converts the cell to markdown

        Currently assumes all code cells are python.

        Parameters
        ----------
        include_fence : bool
            whether to fence the cell. Fences should generally be their
            cells. The exception is "solution", which are nested inside
            other fences.

        Returns
        -------
        str
            the cell formatted in Markdown
        """
        if self.text or self.output:
            if self.cell_type == "code" and self.md_format == "md":
                text = ""
                if self.text:
                    text += f"```python\n{str(self)}\n```"
                if self.output:
                    text += f"\n\n{self.output}"
            elif self.cell_type == "code" and self.md_format == "Rmd":
                text = f"```{{python, error=TRUE}}\n{str(self)}\n```"
            else:
                text = str(self)
            if self.fence and include_fence:
                return fence(text.strip(), self.fence)
            return text.strip() + "\n"
        return ""


class Block:
    """Formats cell a group of notebook cells for a carpentries lesson"""

    def __init__(self, cells):
        self.cells = cells

    def __str__(self):
        return "\n".join([str(c) for c in self.cells])

    def __iter__(self):
        return iter(self.cells)

    @property
    def cell_type(self):
        """The cell_type of the first cell in the block"""
        return self.cells[0].cell_type

    @property
    def fence(self):
        """The fence type of the first cell in the block"""
        return self.cells[0].fence

    def to_markdown(self, include_fence=True):
        """Converts the block to markdown"""
        if self.fence != "solution" and "solution" in [c.fence for c in self.cells]:
            markdown = []
            for block in cells_to_blocks(self.cells):
                block_md = "\n".join([c.to_markdown(False) for c in block.cells])
                if block.fence == "solution":
                    block_md = fence(block_md, block.fence)
                markdown.append(block_md)
            return fence("\n".join(markdown), self.fence)
        markdown = "\n".join([c.to_markdown(False) for c in self.cells])
        if self.fence and include_fence:
            markdown = fence(markdown, self.fence)
        return markdown.rstrip() + "\n"


class Notebook:
    """Formats a notebook as a carpentries lesson chapter"""

    def __init__(self, path, **kwargs):
        self.path = path
        kwargs.setdefault("encoding", "utf-8")
        with open(path, **kwargs) as f:
            self.json = json.load(f)
        self.blocks = cells_to_blocks(self.json["cells"], always_part=["solution"])

    def __str__(self):
        content = "\n".join([b.to_markdown().rstrip("\n") + "\n" for b in self.blocks])
        content = re.sub("^# .*", "", content).strip()
        return f"---\n{yaml.dump(self.metadata)}---\n\n" + content.rstrip() + "\n"

    def __iter__(self):
        return iter(self.blocks)

    @property
    def metadata(self):
        """Extracts metadata about the chapter"""
        metadata = {}
        for block in self.blocks:
            for cell in block:
                if cell.cell_type == "markdown" and cell.header_level == 1:
                    metadata["title"] = cell.title
        return metadata

    def to_markdown(self, path=None):
        """Writes notebook to markdown

        Parameters
        ----------
        path : str
            path for the markdown file

        Returns
        -------
        str
            notebook content as markdown
        """
        with open(path, "w", encoding="utf-8") as f:
            f.write(str(self))
        return str(self)

    def to_notebook(self, path):
        """Writes notebook to notebook file

        Parameters
        ----------
        path : str
            path for the notebook file
        """
        cells = []
        for block in self.blocks:
            cells.extend([c.cell for c in block.cells])

        obj = self.json.copy()
        obj["cells"] = cells

        with open(path, "w", encoding="utf-8") as f:
            json.dump(obj, f, indent=1, ensure_ascii=False)
            f.write("\n")


def cells_to_blocks(cells, **kwargs):
    """Organizes individual cells into multi-cell blocks

    Parameters
    ----------
    cells : list
        a list of cells
    kwargs :
        keyword arguments to pass to cell.is_part_of()

    Returns
    -------
    list of Block
        list of cells grouped into blocks
    """
    blocks = []
    for cell in cells:
        if not isinstance(cell, Cell):
            cell = Cell(cell)
        if blocks and cell.is_part_of(blocks[-1], **kwargs):
            blocks[-1].cells.append(cell)
        else:
            blocks.append(Block([cell]))
    return blocks


def fence(text, fence, length=80):
    """Wraps text in a pretty-printed pandoc fence

    Parameters
    ----------
    text : str
        content of the fence
    fence : str
        name of the fence
    length : int
        total length of the fence divier

    Returns
    -------
    str
        fence
    """
    open_fence = f"::: {fence} " + ":" * (length - len(fence) - 5)
    return f"{open_fence}\n\n{text.rstrip()}\n\n{':' * length}\n"


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs=1, help="Path to the lesson directory")
    parser.add_argument(
        "--to",
        "-t",
        default="md",
        choices=["md", "Rmd"],
        help="Markdown format of the output files",
    )
    parser.add_argument(
        "--html_output", action="store_true", help="Outputs HTML when present"
    )
    parser.add_argument("--reset", action="store_true", help="Clears previous output")

    args = parser.parse_args()

    # Get lesson root
    lesson_root = args.path[0]

    # Set cell parameters
    Cell.lesson_root = lesson_root
    Cell.md_format = args.to
    Cell.html_output = args.html_output

    # Remove previously generated files
    if args.reset:
        # Remove markdown files
        for ext in ("*.md", "*.Rmd"):
            for dirname in ("episodes", "learners"):
                for path in glob.iglob(os.path.join(lesson_root, dirname, ext)):
                    try:
                        os.remove(path)
                    except FileNotFoundError:
                        pass

        # Remove images
        for path in glob.iglob(
            os.path.join(lesson_root, "episodes", "fig", "fig_output_*.png")
        ):
            os.remove(path)

    # Create new markdown files from the notebooks folder
    for nb_path in sorted(
        glob.iglob(os.path.join(lesson_root, "notebooks", "*.ipynb"))
    ):

        root = os.path.splitext(os.path.basename(nb_path))[0]

        # The setup file lives in a different directory and has to be plain markdown
        if root in ("profiles", "reference", "setup"):
            md_path = os.path.join(lesson_root, "learners", f"{root}.{args.to}")
        else:
            md_path = os.path.join(lesson_root, "episodes", f"{root}.md")

        # Save chapters as markdown
        try:
            if os.path.getmtime(nb_path) > os.path.getmtime(md_path):
                raise FileNotFoundError
        except FileNotFoundError:

            # Write the tagged notebook back to the original path
            Notebook(nb_path).to_notebook(nb_path)

            # Run the notebook so that output is populated
            subprocess.run(
                [
                    "jupyter",
                    "nbconvert",
                    "--to",
                    "notebook",
                    "--execute",
                    "--inplace",
                    nb_path,
                ]
            )

            # Write the markdown file
            print(f"Writing {md_path}")
            Notebook(nb_path).to_markdown(md_path)
