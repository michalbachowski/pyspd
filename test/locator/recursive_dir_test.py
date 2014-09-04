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
from pyspd.locator.recursive_dir import LocatorRecursiveDir


class LocatorRecursiveDirTestCase(unittest.TestCase):

    def setUp(self):
        self.lf = LocatorRecursiveDir(*self.get_example_paths())

    def get_example_paths(self):
        if not hasattr(self, 'example_paths'):
            tmp = os.path.join(os.path.dirname(os.path.dirname(
                os.path.abspath(__file__))), 'examples4')
            self.example_paths = [tmp]
        return self.example_paths

    def test_init_allows_no_arguments(self):
        err = False
        try:
            LocatorRecursiveDir()
        except:
            err = True
        self.assertFalse(err)

    def test_init_allows_to_pass_many_arguments(self):
        err = False
        try:
            LocatorRecursiveDir('a')
            LocatorRecursiveDir('a', None)
            LocatorRecursiveDir('a', 'b')
            LocatorRecursiveDir('a', 'f', 'sdfsdf')
        except:
            err = True
        self.assertFalse(err)

    def test_locator_raises_os_error_when_directory_does_not_exist(self):
        lf = LocatorRecursiveDir('/foo/bar/baz.py')
        self.assertRaises(OSError, lf)

    def test_locator_imports_module_from_given_file(self):
        self.assertFalse('plg1' in sys.modules.keys())
        self.assertFalse('plg2' in sys.modules.keys())
        self.assertFalse('plg3' in sys.modules.keys())
        self.assertFalse('loaded3' in sys.modules.keys())
        self.assertFalse('loaded4' in sys.modules.keys())

        self.lf()

        self.assertTrue('plg1' in sys.modules.keys())
        self.assertTrue('plg2' in sys.modules.keys())
        self.assertTrue('plg3' in sys.modules.keys())
        self.assertTrue('loaded3' in sys.modules.keys())
        self.assertTrue('loaded4' in sys.modules.keys())


if "__main__" == __name__:
    unittest.main()
