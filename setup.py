"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

import os.path

import setuptools


MODULE_NAME = "msgfy"
REPOSITORY_URL = "https://github.com/thombashi/{:s}".format(MODULE_NAME)
REQUIREMENT_DIR = "requirements"
ENCODING = "utf8"

pkg_info = {}


def get_release_command_class():
    try:
        from releasecmd import ReleaseCommand
    except ImportError:
        return {}

    return {"release": ReleaseCommand}


with open(os.path.join(MODULE_NAME, "__version__.py")) as f:
    exec(f.read(), pkg_info)

with open("README.rst", encoding=ENCODING) as f:
    LONG_DESCRIPTION = f.read()

with open(os.path.join(REQUIREMENT_DIR, "test_requirements.txt")) as f:
    TESTS_REQUIRES = [line.strip() for line in f if line.strip()]

SETUPTOOLS_REQUIRES = ["setuptools>=38.3.0"]

setuptools.setup(
    name=MODULE_NAME,
    version=pkg_info["__version__"],
    url=REPOSITORY_URL,
    author=pkg_info["__author__"],
    author_email=pkg_info["__email__"],
    description=(
        "msgfy is a Python library for convert Exception instance to "
        "a human-readable error message."
    ),
    include_package_data=True,
    keywords=["error"],
    license=pkg_info["__license__"],
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",
    packages=setuptools.find_packages(exclude=["test*"]),
    project_urls={"Source": REPOSITORY_URL, "Tracker": "{:s}/issues".format(REPOSITORY_URL)},
    python_requires=">=3.5",
    install_requires=SETUPTOOLS_REQUIRES,
    tests_require=TESTS_REQUIRES,
    extras_require={
        "build": ["twine", "wheel"],
        "release": ["releasecmd>=0.0.18,<0.1.0"],
        "test": TESTS_REQUIRES,
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing",
    ],
    cmdclass=get_release_command_class(),
)
