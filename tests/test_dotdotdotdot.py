# coding: utf-8
import os.path
import sys

DOT = sys.path[0]
DOTDOT = os.path.dirname(DOT)
DOTDOTDOT = os.path.dirname(DOTDOT)
DOTDOTDOTDOT = os.path.dirname(DOTDOTDOT)

sys.path.append(DOTDOT)


def test_dotdotdotdot():
    import dotdotdotdot
    import dotdotdot
    import dotdot
    import dot
    import dotdotdot
    assert sys.path[0] == DOTDOTDOTDOT
