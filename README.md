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

## Example
```
root dir
    ├── apple.py *****************
    │   * import dot             *
    │   * import dir.boy         *
    │   * import dir.subdir.cat  *
    │   * script code ...        *
    │   **************************
    │
    └── dir
         ├── boy.py *******************
         │   * import dotdot          *
         │   * import apple           *
         │   * import dir.subdir.cat  *
         │   * script code ...        *
         │   **************************
         │    
         └── subdir
                └── cat.py *******************
                    * import dotdotdot       *
                    * import apple           *
                    * import dir.boy         *
                    * script code ...        *
                    **************************
```


## How It Works
DotDot does this magic by changing `sys.path[0]` in __import time__.
