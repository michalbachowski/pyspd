#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


# monkey patch os.link to force using symlinks
import os
del os.link

setup(name='PySimplePluginsDiscovery',
    url='https://github.com/michalbachowski/pyspd',
    version='0.1.0',
    description='Python simple plugins framework described by Martin Alchin (http://martyalchin.com/2008/jan/10/simple-plugin-framework/)',
    license='MIT',
    author='Michał Bachowski',
    author_email='michal@bachowski.pl',
    packages=['pyspd', 'pyspd.locator'],
    package_dir={'': 'src', 'locator': 'src/locator'})
