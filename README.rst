.. contents:: **msgfy**
   :backlinks: top
   :depth: 2


Summary
====================================
msgfy is a Python library for convert Exception instance to a human-readable error message.


.. image:: https://badge.fury.io/py/msgfy.svg
    :target: https://badge.fury.io/py/msgfy
    :alt: PyPI package version

.. image:: https://img.shields.io/pypi/pyversions/msgfy.svg
    :target: https://pypi.org/project/msgfy
    :alt: Supported Python versions

.. image:: https://img.shields.io/travis/thombashi/msgfy/master.svg?label=Linux%20CI
    :target: https://travis-ci.org/thombashi/msgfy
    :alt: Linux CI status

.. image:: https://img.shields.io/appveyor/ci/thombashi/msgfy/master.svg?label=Windows%20CI
    :target: https://ci.appveyor.com/project/thombashi/msgfy
    :alt: Windows CI status

.. image:: https://coveralls.io/repos/github/thombashi/msgfy/badge.svg?branch=master
    :target: https://coveralls.io/github/thombashi/msgfy?branch=master
    :alt: Test coverage


Usage
====================================

Convert from Exception instance to an error message
------------------------------------------------------------------------
:Sample Code:
    .. code:: python

        import msgfy

        def error_message_example():
            try:
                raise ValueError("example message")
            except ValueError as e:
                print(msgfy.to_error_message(e))

        error_message_example()

:Output:
    ::

        ValueError: example error message

Specify message format
------------------------------------
:Sample Code:
    .. code:: python

        import msgfy

        def error_message_format_example():
            try:
                raise ValueError("example error message")
            except ValueError as e:
                print(msgfy.to_error_message(e, "{exception} {func_name}: {error_msg}"))

        error_message_format_example()

:Output:
    ::

        ValueError error_message_format_example: example error message


Convert from Exception instance to a debug message
------------------------------------------------------------------------
:Sample Code:
    .. code:: python

        import msgfy

        def debug_message_example():
            try:
                raise ValueError("example debug message")
            except ValueError as e:
                print(msgfy.to_debug_message(e))

        debug_message_example()

:Output:
    ::

        ValueError <ipython-input-4-bdd569af197b>(5) debug_message_example: example debug message


Available keywords for message formats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------+-----------------------------------------------+
| Keyword             | Replaced to                                   |
+=====================+===============================================+
| ``"{exception}"``   | Exception class name                          |
+---------------------+-----------------------------------------------+
| ``"{file_name}"``   | File name that exception raised               |
+---------------------+-----------------------------------------------+
| ``"{line_no}"``     | Line number where the exception raised        |
+---------------------+-----------------------------------------------+
| ``"{func_name}"``   | Function name that exception raised           |
+---------------------+-----------------------------------------------+
| ``"{error_msg}"``   | Message that passed to the exception instance |
+---------------------+-----------------------------------------------+


Installation
====================================

Install from PyPI
------------------------------
::

    pip install msgfy

Install from PPA (for Ubuntu)
------------------------------
::

    sudo add-apt-repository ppa:thombashi/ppa
    sudo apt update
    sudo apt install python3-msgfy


Dependencies
====================================
Python 3.5+
No external dependencies.

Test dependencies
-----------------
- `pytest <https://docs.pytest.org/en/latest/>`__
- `tox <https://testrun.org/tox/latest/>`__
