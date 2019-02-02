# DotDot
___Make it easy to import the modules in parent directories___

[![released version](https://img.shields.io/pypi/v/DotDot.svg)](https://pypi.org/project/dotdot)
[![license](https://img.shields.io/github/license/Gsllchb/DotDot.svg)](https://github.com/Gsllchb/DotDot/blob/master/LICENSE.txt)
[![Build Status](https://travis-ci.org/Gsllchb/DotDot.svg?branch=master)](https://travis-ci.org/Gsllchb/DotDot)
[![downloads](https://img.shields.io/pypi/dm/DotDot.svg)](https://pypistats.org/packages/dotdot)

If you want to solve `ValueError: attempted relative import beyond top-level package`, DotDot may be helpful for you.

## Installation
If it can be installed and imported successfully, it should work correctly.
```console
pip install dotdot
```

## Quick Start
Consider a common project structure as following:
```
FooProject
    ├── foo
    │    ├── script.py
    │    └── util0.py
    └── util1.py
```
Now, `script.py` can import `util1` by importing `dotdot` first. Like this:
```python
import dotdot
import foo.util0
import util1
```
Moreover, you can import the modules in grandparent or even great grandparent directory by importing `dotdotdot` or `dotdotdotdot` first.

## How it work
DotDot does this magic by changing `sys.path[0]` in __import time__.
