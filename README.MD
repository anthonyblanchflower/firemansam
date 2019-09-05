# Fireman Sam

*lib2to3 analysis functions*

## Background

**lib2to3** is a standard Python library for reading Python 2.x source code and identifying a series of fixes to transform it into valid Python 3.x code. The standard library contains a rich set of fixers that will handle almost all code.
 
I wrote the **firemansam** library to provide functions for analysing directories or individual python files (.py) and extracting a scale metric representing the quantity of code lines which would need to be rewritten for the Python code to be compatible with Python 3.
 
## Getting Started

These instructions will allow you to import fireman as a Python module.
For creating a distribution see the Deployment section of this document.

### Prerequisites

If you do not have git installed, install it from https://git-scm.com/downloads.
If you do not have pip3 installed, install it from https://pip.pypa.io.

Make sure you have the latest versions of setuptools and wheel installed.

If you have trouble installing setuptools and wheel visit
https://packaging.python.org/tutorials/installing-packages/

### Installing

firemansam can be installed as a python module using the pip installer.

```
$ pip3 install git+git://github.com/anthonyblanchflower/firemansam.git
```

### Uninstalling

firemansam can be uninstalled as a python module using the pip installer.

```
$ pip3 uninstall firemansam
```

## Documentation

These instructions will demonstrate how to call functions from the fireman module.

### Using firemansam

First import modules:

```
from firemansam.firedir import firedir
from firemansam.firecheck import firecheck
from firemansam.firedir import firedict
```

Now you can use the firemansam functions.

### Module functions

*firecheck(local filename or file path)*

Return the fix recommendations from lib2to3 as a text string.

```
firecheck(example.py)
```

returns

```
--- example.py	(original)
+++ example.py	(refactored)
@@ -1 +1 @@
-print "not compatible"
+print("not compatible")
```

*firedict(local filename or file path)*

Return the fix recommendations from lib2to3 as a dictionary with a key value containing the scale of fixes.

```
firedict(/example/example.py)
```

returns

```
{'file': '/example/example.py', 'scale': 4}
```

*firedir(directory)*

Return a list containing a dictionary for every file in the directory with a *.py extension. Each dictionary contains the filename and the scale of fixes for that file.

```
firedir(/example)
```

returns

```
{'file': '/example/example1.py', 'scale': 4}
{'file': '/example/example/example2.py', 'scale': 0}
```

## Running the tests

Tests can be run using the following command:

```
python3 setup.py test
```

## Deployment

A distribution package can be generated using the following command:

```
python3 setup.py sdist bdist_wheel
```

## Acknowledgments

* https://docs.python.org/3.1/library/2to3.html