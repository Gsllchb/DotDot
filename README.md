# DotDot
___Make it easy to import the modules in parent directories___

[![released version](https://img.shields.io/pypi/v/DotDot.svg)](https://pypi.org/project/dotdot)
[![license](https://img.shields.io/github/license/Gsllchb/DotDot.svg)](https://github.com/Gsllchb/DotDot/blob/master/LICENSE.txt)

If you want to solve `ValueError: attempted relative import beyond top-level package`, **DotDot** may be helpful for you.

## Installation
If it can be installed and imported successfully, it should work correctly.

Install via **pip**:
```console
pip install dotdot
```

## Quick Start
Consider a common project structure as following:
```
FooProject
    ├── foo
    │    ├── script.py
    │    └── util.py
    └── util.py
```
Now, `script.py` can import those `util`s by importing `dotdot` first. Like this:
```python
import dotdot
import foo.util
import util
```
Moreover, you can import the modules in grandparent or even great grandparent directory by importing `dotdotdot` or `dotdotdotdot` first.

## How It Works
DotDot does this magic by changing `sys.path[0]` in __import time__.
