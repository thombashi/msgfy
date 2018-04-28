# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import print_function, unicode_literals

import msgfy
import pytest


class Test_to_error_message(object):

    def test_normal_smoke(self):
        assert msgfy.to_error_message(ValueError("test"))

    @pytest.mark.parametrize(["format_str"], [
        ["{exception} {file_name}({line_no}) {func_name}: {error_msg}"],
        ["{exception}"],
        ["{file_name}"],
        ["{line_no}"],
        ["{func_name}"],
        ["{error_msg}"],
    ])
    def test_normal_format_str(self, format_str):
        assert msgfy.to_error_message(ValueError("test"), format_str) != format_str

    @pytest.mark.parametrize(["exception_obj", "expected"], [
        [None, ValueError],
    ])
    def test_exception_e_object(self, exception_obj, expected):
        with pytest.raises(expected):
            assert msgfy.to_error_message(exception_obj)

    @pytest.mark.parametrize(["format_str", "expected"], [
        [1, ValueError],
    ])
    def test_exception_format_str(self, format_str, expected):
        with pytest.raises(expected):
            assert msgfy.to_error_message(ValueError("test"), format_str)


class Test_to_debug_message(object):

    def test_normal_smoke(self):
        assert msgfy.to_debug_message(ValueError("test"))

    @pytest.mark.parametrize(["format_str"], [
        ["{exception} {file_name}({line_no}) {func_name}: {error_msg}"],
        ["{exception}"],
        ["{file_name}"],
        ["{line_no}"],
        ["{func_name}"],
        ["{error_msg}"],
    ])
    def test_normal_format_str(self, format_str):
        assert msgfy.to_debug_message(ValueError("test"), format_str) != format_str

    @pytest.mark.parametrize(["exception_obj", "expected"], [
        [None, ValueError],
    ])
    def test_exception_e_object(self, exception_obj, expected):
        with pytest.raises(expected):
            assert msgfy.to_debug_message(exception_obj)

    @pytest.mark.parametrize(["format_str", "expected"], [
        [1, ValueError],
    ])
    def test_exception_format_str(self, format_str, expected):
        with pytest.raises(expected):
            assert msgfy.to_debug_message(ValueError("test"), format_str)
