#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    cobra
    ~~~~~

    Implements cobra main

    :author:    Feei <feei@feei.cn>
    :homepage:  https://github.com/wufeifei/cobra
    :license:   MIT, see LICENSE for more details.
    :copyright: Copyright (c) 2017 Feei. All rights reserved
"""
import codecs
import dict
import setuptools.command.test


# -*- Long Description -*-

def long_description():
    try:
        return codecs.open('README.md', 'r', 'utf-8').read()
    except IOError:
        return 'Long description error: Missing README.md file'


setuptools.setup(
    name=dict.__name__,
    version=dict.__version__,
    description=dict.__description__,
    long_description=long_description(),
    keywords=dict.__keywords__,
    author=dict.__author__,
    author_email=dict.__contact__,
    url=dict.__url__,
    license=dict.__license__,
    platforms=['any'],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: English',
        'Topic :: Utilities',
        'Topic :: Terminals',
        "Topic :: System :: Distributed Computing",

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    packages=setuptools.find_packages(exclude=['tests']),
    include_package_data=True,
    package_data={
        '': ['*.py']
    },
    entry_points={
        'console_scripts': [
            'dict = dict:main',
        ],
    },
)