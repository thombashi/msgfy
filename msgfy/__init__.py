
# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import unicode_literals

from .__version__ import __author__, __copyright__, __email__, __license__, __version__
import inspect
import os.path


default_error_format_string = "{exception} {file_name}({line_no}) {func_name}: {error_msg}"


def _to_message(exception_obj, format_str, frame):
    if not isinstance(exception_obj, Exception):
        raise ValueError("exception_obj must be an instance of a subclass of the Exception class")

    try:
        return format_str.replace(
            "{exception}", exception_obj.__class__.__name__).replace(
            "{file_name}", os.path.basename(frame.f_code.co_filename)).replace(
            "{line_no}", str(frame.f_lineno)).replace(
            "{func_name}", frame.f_code.co_name).replace(
            "{error_msg}", str(exception_obj))
    except AttributeError:
        raise ValueError("format_str must be a string")


def to_error_message(exception_obj, format_str=None):
    if not format_str:
        format_str = default_error_format_string

    return _to_message(exception_obj, format_str, inspect.currentframe().f_back)
