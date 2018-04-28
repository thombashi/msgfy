msgfy
====================================
.. image:: https://badge.fury.io/py/msgfy.svg
    :target: https://badge.fury.io/py/msgfy

.. image:: https://img.shields.io/travis/thombashi/msgfy/master.svg?label=Linux
    :target: https://travis-ci.org/thombashi/msgfy

.. image:: https://img.shields.io/appveyor/ci/thombashi/msgfy/master.svg?label=Windows
    :target: https://ci.appveyor.com/project/thombashi/msgfy


Summary
====================================
msgfy is a Python library for convert Exception instance to a human-readable error message.


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
::

    pip install msgfy

Dependencies
====================================
Python 2.7+ or 3.4+

Test dependencies
-----------------
- `pytest <http://pytest.org/latest/>`__
- `pytest-runner <https://pypi.python.org/pypi/pytest-runner>`__
- `tox <https://testrun.org/tox/latest/>`__
