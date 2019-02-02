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

"""DotDot test"""

import os.path
import sys

DOT = sys.path[0]
DOTDOT = os.path.dirname(DOT)
DOTDOTDOT = os.path.dirname(DOTDOT)
DOTDOTDOTDOT = os.path.dirname(DOTDOTDOT)


def teardown_function():
    sys.path[0] = DOT


def test_dot():
    import dot
    assert sys.path[0] == DOT


def test_dotdot():
    import dotdot
    assert sys.path[0] == DOTDOT


def test_dotdotdot():
    import dotdotdot
    assert sys.path[0] == DOTDOTDOT


def test_dotdotdotdot():
    import dotdotdotdot
    assert sys.path[0] == DOTDOTDOTDOT
