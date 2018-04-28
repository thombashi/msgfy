
# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import unicode_literals

from .__version__ import __author__, __copyright__, __email__, __license__, __version__
import inspect
import os.path


DEFAULT_ERROR_MESSAGE_FORMAT = "{exception}: {error_msg}"
DEFAULT_DEBUG_MESSAGE_FORMAT = "{exception} {file_name}({line_no}) {func_name}: {error_msg}"

error_message_format = DEFAULT_ERROR_MESSAGE_FORMAT
debug_message_format = DEFAULT_DEBUG_MESSAGE_FORMAT


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
        format_str = error_message_format

    return _to_message(exception_obj, format_str, inspect.currentframe().f_back)


def to_debug_message(exception_obj, format_str=None):
    if not format_str:
        format_str = debug_message_format

    return _to_message(exception_obj, format_str, inspect.currentframe().f_back)
