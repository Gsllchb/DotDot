# coding: utf-8

# Copyright (c) 2019 Gsllchb
#
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""DotDot: Make it easy to import the modules in parent directories.

This module replaces `sys.path[0]` with its own grandparent directory in import
time if it is the first import amongst `dot`, `dotdot`, `dotdotdot`, and
`dotdotdotdot` in chronological order in a Python session, otherwise, does
nothing.

The scripts in the grandchild directories of project roots should import
`dotdotdot` before importing any local module.

See also `dot`, `dotdot`, and `dotdotdotdot`."""

import _dotdot
from _dotdot import do_nothing

__version__ = _dotdot.__version__

_dotdot.set_level_if_valid(2)
