#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# python standard library
#
import unittest
import os
import sys

##
# content bits modules
#
from pyspd.locator.dir import LocatorDir


class LocatorDirTestCase(unittest.TestCase):

    def setUp(self):
        self.lf = LocatorDir(*self.get_example_paths())

    def get_example_paths(self):
        if not hasattr(self, 'example_paths'):
            tmp = os.path.join(os.path.dirname(os.path.dirname(
                os.path.abspath(__file__))), 'examples2')
            self.example_paths = [tmp]
        return self.example_paths

    def test_init_allows_no_arguments(self):
        err = False
        try:
            LocatorDir()
        except:
            err = True
        self.assertFalse(err)

    def test_init_allows_to_pass_many_arguments(self):
        err = False
        try:
            LocatorDir('a')
            LocatorDir('a', None)
            LocatorDir('a', 'b')
            LocatorDir('a', 'f', 'sdfsdf')
        except:
            err = True
        self.assertFalse(err)

    def test_locator_raises_os_error_when_directory_does_not_exist(self):
        lf = LocatorDir('/foo/bar/baz.py')
        self.assertRaises(OSError, lf)

    def test_locator_imports_module_from_given_file(self):
        self.assertFalse('pl1' in sys.modules.keys())
        self.assertFalse('pl2' in sys.modules.keys())
        self.assertFalse('pl3' in sys.modules.keys())

        self.lf()

        self.assertTrue('pl1' in sys.modules.keys())
        self.assertTrue('pl2' in sys.modules.keys())
        self.assertTrue('pl3' in sys.modules.keys())


if "__main__" == __name__:
    unittest.main()
