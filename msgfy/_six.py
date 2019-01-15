"""
Code from six:
    https://github.com/benjaminp/six/blob/master/LICENSE
"""

from __future__ import absolute_import

import sys


PY3 = sys.version_info[0] == 3


if PY3:
    text_type = str
else:
    text_type = unicode
