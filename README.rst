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
:Sample Code:
    .. code:: python

        import msgfy

        def main():
            try:
                raise ValueError("example message")
            except ValueError as e:
                print(msgfy.to_error_message(e))

        main()

:Output:
    ::

        ValueError error_message_basic.py(19) main: example message

Specify message format
------------------------------------
:Sample Code:
    .. code:: python

        import msgfy

        def main():
            try:
                raise ValueError("example message")
            except ValueError as e:
                print(msgfy.to_error_message(e, "{func_name}: {error_msg}"))

        main()

:Output:
    ::

        main: example message


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
