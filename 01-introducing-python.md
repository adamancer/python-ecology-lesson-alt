---
title: Introducing Python
teaching: 60
exercises: 0
---

::: questions ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   What is Python?
-   How do we assign variables in Python?
-   How do we perform actions in Python?
-   How does Python handle different types of data?

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: objectives :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   Introduce some Python terminology
-   Learn how to assign values to variables
-   Learn how to use functions and methods
-   Introduce the built-in Python data types and functions
-   Introduce the Python Standard Library

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## About Python

Python is a high-level, general purpose language. In practical terms,
that means it dispenses with many of the complexities of writing code.
It is widely used and has an active community of developers, making it
suitable for a large number of tasks.

A core philosophical tenet of Python is that code is read more often
than it is written. Best practices for coding in Python therefore
emphasize writing well-documented, consistently formatted code that
follows language-wide standards. **In a Pythonic world, everyone's code
would look the same.**

::: callout ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#### Whitespace

One feature to be aware of going in is that Python uses whitespace (as
opposed to braces) to organize blocks of code. This can be a sticking
point for people used to other languages.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## Getting started

Everything in Python is an *object*. Each object has a type, which
controls what the object can do. For example, we can add integers
together or append a string to a list. An object can be *assigned* to a
*variable*, and a *function* performs an action.

Python is an *object-oriented language*. This means that each object
includes built-in variables and functions that can be used from the
object itself. Whe use different terms to refer to variables and
functions associated with an object:

-   an *attribute* stores a piece of data
-   a *method* performs an action

Let's look at one of the main built-in types, `str`, to see how this
works in practice. In Python, `str`, short for string, is used to store
and manipulate text. To get started, we'll assign the string "hello
world" to the variable **text**. In Python, we use a single equal sign
for assignment and quotes to create a string.

```python
text = "hello world"
```

::: callout ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### Using quotes

Either single or double quotes can be used to create strings, but try to
use them consistently! We will use double quotes in the examples here.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Now, instead of retyping the full string every time we need it, we can
access that string by referring to the variable:

```python
text
```

```{.output}
'hello world'
```

We can check the type of the variable using the `type()` function:

```python
type(text)
```

```{.output}
str
```

A `str` is also an object, which means that it includes methods and
attributes that we can use. Let's use the `upper()` method to convert
the text to upper case. We call methods by adding a period and the name
of the method to the variable:

```python
text.upper()
```

```{.output}
'HELLO WORLD'
```

After running a cell, the notebook displays the object that appears in
the last line of a cell (but note that some actions, like assigning to a
variable, have no output). Some cells will have more than one line, and
it is often useful to display output from earlier in a cell. This can be
accomplished using the built-in `print()` function. In the cell below,
we'll use `print()` to show a series of strings:

```python
"hello"
print("h")
print("e")
print("l")
print("l")
print("o")
"world"
```

```{.output}
h
e
l
l
o

'world'
```

Note that the string "hello" at the top of the cell lacks a print
statement and does not appear in the output, whereas the text "world"
*does* appear in the output because it is the last line of the cell.

Each object may contain many attributes and methods. Use the `help()`
function on any object, including functions or methods, to show a
description of the object and list the available methods.

```python
help(str)
```

```{.output}
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to 'utf-8'.
 |  errors defaults to 'strict'.
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __contains__(self, key, /)
 |      Return bool(key in self).
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getitem__(self, key, /)
 |      Return self[key].
 |
 |  __getnewargs__(self, /)
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __hash__(self, /)
 |      Return hash(self).
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __len__(self, /)
 |      Return len(self).
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __mod__(self, value, /)
 |      Return self%value.
 |
 |  __mul__(self, value, /)
 |      Return self*value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __rmod__(self, value, /)
 |      Return value%self.
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  __sizeof__(self, /)
 |      Return the size of the string in memory, in bytes.
 |
 |  __str__(self, /)
 |      Return str(self).
 |
 |  capitalize(self, /)
 |      Return a capitalized version of the string.
 |
 |      More specifically, make the first character have upper case and the rest lower
 |      case.
 |
 |  casefold(self, /)
 |      Return a version of the string suitable for caseless comparisons.
 |
 |  center(self, width, fillchar=' ', /)
 |      Return a centered string of length width.
 |
 |      Padding is done using the specified fill character (default is a space).
 |
 |  count(self, sub[, start[, end]], /)
 |      Return the number of non-overlapping occurrences of substring sub in string S[start:end].
 |
 |      Optional arguments start and end are interpreted as in slice notation.
 |
 |  encode(self, /, encoding='utf-8', errors='strict')
 |      Encode the string using the codec registered for encoding.
 |
 |      encoding
 |        The encoding in which to encode the string.
 |      errors
 |        The error handling scheme to use for encoding errors.
 |        The default is 'strict' meaning that encoding errors raise a
 |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
 |        'xmlcharrefreplace' as well as any other name registered with
 |        codecs.register_error that can handle UnicodeEncodeErrors.
 |
 |  endswith(self, suffix[, start[, end]], /)
 |      Return True if the string ends with the specified suffix, False otherwise.
 |
 |      suffix
 |        A string or a tuple of strings to try.
 |      start
 |        Optional start position. Default: start of the string.
 |      end
 |        Optional stop position. Default: end of the string.
 |
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |
 |  find(self, sub[, start[, end]], /)
 |      Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].
 |
 |      Optional arguments start and end are interpreted as in slice notation.
 |      Return -1 on failure.
 |
 |  format(self, /, *args, **kwargs)
 |      Return a formatted version of the string, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |
 |  format_map(self, mapping, /)
 |      Return a formatted version of the string, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |
 |  index(self, sub[, start[, end]], /)
 |      Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].
 |
 |      Optional arguments start and end are interpreted as in slice notation.
 |      Raises ValueError when the substring is not found.
 |
 |  isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
 |
 |  isalpha(self, /)
 |      Return True if the string is an alphabetic string, False otherwise.
 |
 |      A string is alphabetic if all characters in the string are alphabetic and there
 |      is at least one character in the string.
 |
 |  isascii(self, /)
 |      Return True if all characters in the string are ASCII, False otherwise.
 |
 |      ASCII characters have code points in the range U+0000-U+007F.
 |      Empty string is ASCII too.
 |
 |  isdecimal(self, /)
 |      Return True if the string is a decimal string, False otherwise.
 |
 |      A string is a decimal string if all characters in the string are decimal and
 |      there is at least one character in the string.
 |
 |  isdigit(self, /)
 |      Return True if the string is a digit string, False otherwise.
 |
 |      A string is a digit string if all characters in the string are digits and there
 |      is at least one character in the string.
 |
 |  isidentifier(self, /)
 |      Return True if the string is a valid Python identifier, False otherwise.
 |
 |      Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
 |      such as "def" or "class".
 |
 |  islower(self, /)
 |      Return True if the string is a lowercase string, False otherwise.
 |
 |      A string is lowercase if all cased characters in the string are lowercase and
 |      there is at least one cased character in the string.
 |
 |  isnumeric(self, /)
 |      Return True if the string is a numeric string, False otherwise.
 |
 |      A string is numeric if all characters in the string are numeric and there is at
 |      least one character in the string.
 |
 |  isprintable(self, /)
 |      Return True if all characters in the string are printable, False otherwise.
 |
 |      A character is printable if repr() may use it in its output.
 |
 |  isspace(self, /)
 |      Return True if the string is a whitespace string, False otherwise.
 |
 |      A string is whitespace if all characters in the string are whitespace and there
 |      is at least one character in the string.
 |
 |  istitle(self, /)
 |      Return True if the string is a title-cased string, False otherwise.
 |
 |      In a title-cased string, upper- and title-case characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |
 |  isupper(self, /)
 |      Return True if the string is an uppercase string, False otherwise.
 |
 |      A string is uppercase if all cased characters in the string are uppercase and
 |      there is at least one cased character in the string.
 |
 |  join(self, iterable, /)
 |      Concatenate any number of strings.
 |
 |      The string whose method is called is inserted in between each given string.
 |      The result is returned as a new string.
 |
 |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
 |
 |  ljust(self, width, fillchar=' ', /)
 |      Return a left-justified string of length width.
 |
 |      Padding is done using the specified fill character (default is a space).
 |
 |  lower(self, /)
 |      Return a copy of the string converted to lowercase.
 |
 |  lstrip(self, chars=None, /)
 |      Return a copy of the string with leading whitespace removed.
 |
 |      If chars is given and not None, remove characters in chars instead.
 |
 |  partition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |
 |      This will search for the separator in the string.  If the separator is found,
 |      returns a 3-tuple containing the part before the separator, the separator
 |      itself, and the part after it.
 |
 |      If the separator is not found, returns a 3-tuple containing the original string
 |      and two empty strings.
 |
 |  removeprefix(self, prefix, /)
 |      Return a str with the given prefix string removed if present.
 |
 |      If the string starts with the prefix string, return string[len(prefix):].
 |      Otherwise, return a copy of the original string.
 |
 |  removesuffix(self, suffix, /)
 |      Return a str with the given suffix string removed if present.
 |
 |      If the string ends with the suffix string and that suffix is not empty,
 |      return string[:-len(suffix)]. Otherwise, return a copy of the original
 |      string.
 |
 |  replace(self, old, new, /, count=-1)
 |      Return a copy with all occurrences of substring old replaced by new.
 |
 |        count
 |          Maximum number of occurrences to replace.
 |          -1 (the default value) means replace all occurrences.
 |
 |      If the optional argument count is given, only the first count occurrences are
 |      replaced.
 |
 |  rfind(self, sub[, start[, end]], /)
 |      Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].
 |
 |      Optional arguments start and end are interpreted as in slice notation.
 |      Return -1 on failure.
 |
 |  rindex(self, sub[, start[, end]], /)
 |      Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].
 |
 |      Optional arguments start and end are interpreted as in slice notation.
 |      Raises ValueError when the substring is not found.
 |
 |  rjust(self, width, fillchar=' ', /)
 |      Return a right-justified string of length width.
 |
 |      Padding is done using the specified fill character (default is a space).
 |
 |  rpartition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |
 |      This will search for the separator in the string, starting at the end. If
 |      the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it.
 |
 |      If the separator is not found, returns a 3-tuple containing two empty strings
 |      and the original string.
 |
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the substrings in the string, using sep as the separator string.
 |
 |        sep
 |          The separator used to split the string.
 |
 |          When set to None (the default value), will split on any whitespace
 |          character (including \n \r \t \f and spaces) and will discard
 |          empty strings from the result.
 |        maxsplit
 |          Maximum number of splits.
 |          -1 (the default value) means no limit.
 |
 |      Splitting starts at the end of the string and works to the front.
 |
 |  rstrip(self, chars=None, /)
 |      Return a copy of the string with trailing whitespace removed.
 |
 |      If chars is given and not None, remove characters in chars instead.
 |
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the substrings in the string, using sep as the separator string.
 |
 |        sep
 |          The separator used to split the string.
 |
 |          When set to None (the default value), will split on any whitespace
 |          character (including \n \r \t \f and spaces) and will discard
 |          empty strings from the result.
 |        maxsplit
 |          Maximum number of splits.
 |          -1 (the default value) means no limit.
 |
 |      Splitting starts at the front of the string and works to the end.
 |
 |      Note, str.split() is mainly useful for data that has been intentionally
 |      delimited.  With natural text that includes punctuation, consider using
 |      the regular expression module.
 |
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the string, breaking at line boundaries.
 |
 |      Line breaks are not included in the resulting list unless keepends is given and
 |      true.
 |
 |  startswith(self, prefix[, start[, end]], /)
 |      Return True if the string starts with the specified prefix, False otherwise.
 |
 |      prefix
 |        A string or a tuple of strings to try.
 |      start
 |        Optional start position. Default: start of the string.
 |      end
 |        Optional stop position. Default: end of the string.
 |
 |  strip(self, chars=None, /)
 |      Return a copy of the string with leading and trailing whitespace removed.
 |
 |      If chars is given and not None, remove characters in chars instead.
 |
 |  swapcase(self, /)
 |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
 |
 |  title(self, /)
 |      Return a version of the string where each word is titlecased.
 |
 |      More specifically, words start with uppercased characters and all remaining
 |      cased characters have lower case.
 |
 |  translate(self, table, /)
 |      Replace each character in the string using the given translation table.
 |
 |        table
 |          Translation table, which must be a mapping of Unicode ordinals to
 |          Unicode ordinals, strings, or None.
 |
 |      The table must implement lookup/indexing via __getitem__, for instance a
 |      dictionary or list.  If this operation raises LookupError, the character is
 |      left untouched.  Characters mapped to None are deleted.
 |
 |  upper(self, /)
 |      Return a copy of the string converted to uppercase.
 |
 |  zfill(self, width, /)
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |
 |      The string is never truncated.
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.
 |
 |  maketrans(x, y=<unrepresentable>, z=<unrepresentable>, /)
 |      Return a translation table usable for str.translate().
 |
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.


```

### Data types

Python includes data types for representing other types of data,
including numbers or collections of data. The core Python data types are
introduced in the table below. We'll talk more about some of these as we
encounter them in the lesson:

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Type                                                                             Definition              Example
  -------------------------------------------------------------------------------- ----------------------- ----------------------------------------------------------------------
  [str](https://docs.python.org/3/library/stdtypes.html#textseq)                   Character string        `"hello world"`

  [int](https://docs.python.org/3/library/functions.html#int)                      Integer numerical       `42`

  [float](https://docs.python.org/3/library/functions.html#float)                  Approximate numerical   `0.406`

  [bool](https://docs.python.org/3/library/functions.html#bool)                    Stores True or False    `True` or `False`
                                                                                   values                  

  [list](https://docs.python.org/3/library/stdtypes.html#lists)                    Sequence that can be    `["a", "b", "c"]`
                                                                                   modified                

  [tuple](https://docs.python.org/3/library/stdtypes.html#tuples)                  Sequence that cannot be `("a", "b", "c")`
                                                                                   modified                

  [dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)       Mapping of keys to      `{"DC": "District of Columbia", "MD": "Maryland", "VA": "Virginia"}`
                                                                                   values                  

  [set](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)   Collection of unique    `{"1", "2", 1}`
                                                                                   values                  
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Libraries

Python includes a number of [built-in
functions](https://docs.python.org/3/library/functions.html) that are
available wherever Python is installed. See the table below for some
examples.

### Examples of built-in functions

  ----------------------------------------------------------------------------------------------------------------------------
  Name                                                                  Description             Example
  --------------------------------------------------------------------- ----------------------- ------------------------------
  [`abs()`](https://docs.python.org/3/library/functions.html#abs)       Gets the absolute value `abs(-1.5) # returns 1.5`
                                                                        of a number             

  [`max()`](https://docs.python.org/3/library/functions.html#max)       Gets the highest value  `min([1, 2, 3]) # returns 3`
                                                                        in a sequence           

  [`min()`](https://docs.python.org/3/library/functions.html#min)       Gets the lowest value   `min([1, 2, 3]) # returns 1`
                                                                        in a sequence           

  [`round()`](https://docs.python.org/3/library/functions.html#round)   Rounds a number to the  `round(5.4) # returns 5`
                                                                        nearest integer         
  ----------------------------------------------------------------------------------------------------------------------------

Python also includes a number of built-in modules. A *module* bundles
functions and other code related to a single task or data type. They are
used to simplify the performance of common tasks. By using a common,
well-tested code base, modules allow coders to work more quickly and
with fewer errors.

::: callout ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#### Modules, packages, and libraries

A module is generally a single file. Collections of modules are referred
to as packages or libraries.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

The modules built into Python are referred to as the [Python Standard
Library](https://docs.python.org/3/library/index.html). They can be
accessed through a typical Python installation and do not require any
additional downloads. A few examples are included in the table below,
but as with the table of built-in functions, there are more where those
came from.

### Examples from the Python Standard Library

  -------------------------------------------------------------------------------------------------
  Library                                                       Description
  ------------------------------------------------------------- -----------------------------------
  [datetime](https://docs.python.org/3/library/datetime.html)   Read, write, and analyze dates and
                                                                times

  [os](https://docs.python.org/3/library/os.html)               Create, manipulate, and get
                                                                information about files and paths

  [random](https://docs.python.org/3/library/random.html)       Generate pseudo-random numbers
  -------------------------------------------------------------------------------------------------

::: callout ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## Documentation

The documentation for each module can be viewed by clicking the link in
the table. Documentation is an invaluable resource. It provides
descriptions of what a module does and detailed information about how it
can be used, often including examples.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Unlike the built-in functions, we must import a library before we can
use it. We do so using the `import` statement:

```python
import datetime
```

Once imported, the module is available for use anywhere in the current
document. A module is itself an object, and we must include the name of
the module to access any functions it defines. For example, to create a
`datetime.date` object (that is, a `date` object defined by the
`datetime` module), we include both the module and method name:

```python
date = datetime.date(1970, 1, 1)
```

As with the built-in types, the `datetime.date` object includes its own
suite of attributes and methods. We can, for example, use the year
attribute to get the year:

```python
date.year
```

```{.output}
1970
```

Or convert the date to a string using the
[`strftime()`](https://docs.python.org/3/library/datetime.html#datetime.date.strftime)
method and Python's [date format
codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes).
Here, %Y corresponds to YYYY, %m to MM, and %d to DD.

```python
date.strftime("%Y-%m-%d")
```

```{.output}
'1970-01-01'
```

Like Python itself, the Python Standard Library is maintained by the
Python Software Foundation. The built-in modules are limited to a
relatively small set of operations expected to be useful to a broad
population of users. However, Python allows users to create their own
packages to perform actions that are beyond the scope of core Python.
The rest of this lesson will focus on an external package called pandas.

::: keypoints ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-   Python is a widely used language that can be used for a variety of
    tasks, including analyzing data
-   Python uses different data types to handle text, numbers,
    collections, and other kinds of data
-   Assign values to variables using the `=` operator
-   Use functions and methods to perform specific actions
-   Python's functionality can be extended using packages developed by
    the community
-   Use the `help()` function and developer documentation to learn more
    about Python modules and packages

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
