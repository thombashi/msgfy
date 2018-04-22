#!/usr/bin/env python
# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import print_function, unicode_literals

import sys

import msgfy


def main():
    try:
        raise ValueError("example message")
    except ValueError as e:
        print(msgfy.to_error_message(e, "{func_name}: {error_msg}"))

    return 0


if __name__ == "__main__":
    sys.exit(main())
