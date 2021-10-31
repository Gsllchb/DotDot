# coding: utf-8
import os.path
import sys

DOT = sys.path[0]
DOTDOT = os.path.dirname(DOT)
DOTDOTDOT = os.path.dirname(DOTDOT)
DOTDOTDOTDOT = os.path.dirname(DOTDOTDOT)

sys.path.append(DOTDOT)


def teardown_function():
    import _dotdot
    _dotdot._has_called = False
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
