
# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import unicode_literals

import inspect
import os.path


default_error_format_string = (
    "{exception} {file_name}({line_no}) {func_name}: {error_msg}")


def to_error_message(exception_obj, format_str=None):
    if not isinstance(exception_obj, Exception):
        raise ValueError("exception_obj must be an instance of a subclass of Exception class")

    if not format_str:
        format_str = default_error_format_string

    frame = inspect.currentframe().f_back

    try:
        return format_str.replace(
            "{exception}", exception_obj.__class__.__name__).replace(
            "{file_name}", os.path.basename(frame.f_code.co_filename)).replace(
            "{line_no}", str(frame.f_lineno)).replace(
            "{func_name}", frame.f_code.co_name).replace(
            "{error_msg}", str(exception_obj))
    except AttributeError:
        raise ValueError("format_str must be a string")
