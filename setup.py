#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'requests>=2.5.2',
]

test_requirements = [
    'mock>=1.2'
]

setup(
    name='infoblox_netmri',
    version='0.1.0',
    description="A simple client for the Infoblox NetMRI RESTful API.",
    long_description=readme + '\n\n' + history,
    author="John Belamaric",
    author_email='jbelamaric@infoblox.com',
    url='https://github.com/infobloxopen/infoblox_netmri',
    packages=[
        'infoblox_netmri',
    ],
    package_dir={'infoblox_netmri':
                 'infoblox_netmri'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache",
    zip_safe=False,
    keywords='infoblox_netmri',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='infoblox_netmri.tests',
    tests_require=test_requirements
)
