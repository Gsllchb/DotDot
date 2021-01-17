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

import os.path

import setuptools

import _dotdot


def main():
    setuptools.setup(
        name="dotdot",
        version=_dotdot.__version__,
        author="Gsllchb",
        author_email="gsllchb@qq.com",
        py_modules=(
            "_dotdot",
            "dot",
            "dotdot",
            "dotdotdot",
            "dotdotdotdot"
        ),
        description="Make it easy to import the modules in parent directories",
        long_description=get_long_description(),
        long_description_content_type="text/markdown",
        license="MIT",
        url="https://github.com/Gsllchb/DotDot",
        zip_safe=True,
    )


def get_long_description():
    with open(abs_path("README.md"), encoding="utf-8") as f:
        return f.read()


def abs_path(path):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), path)


if __name__ == "__main__":
    main()
