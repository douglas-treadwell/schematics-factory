#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from setuptools import setup, find_packages


def find_version(filename):
    """
    Attempts to find the version number in the file named filename.
    Raises RuntimeError if not found.
    """

    version = ''

    with open(filename, 'r') as file_:
        regex = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')

        for line in file_:
            match = regex.match(line)

            if match:
                version = match.group(1)
                break

    if not version:
        raise RuntimeError('Cannot find version information')

    return version


__version__ = find_version("schematics_factory/__init__.py")


def read(filename):
    with open(filename) as file_:
        content = file_.read()
    return content


setup(
    name='schematics-factory',
    version=__version__,
    description=('Convenient anonymous and nested models '
                 'using dict literal syntax for Schematics.'),
    long_description=read('README.md'),
    author='Douglas Treadwell',
    author_email='douglas.treadwell@gmail.com',
    url='https://github.com/douglas-treadwell/schematics-factory',
    packages=find_packages(exclude=('tests', 'examples', 'docs')),
    package_dir={'schematics_factory': 'schematics_factory'},
    include_package_data=True,
    install_requires=['schematics'],
    license='MIT',
    keywords=('schematics', 'validation', 'schema',
              'model', 'models', 'modelling', 'object', 'objects'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    test_suite='tests'
)
