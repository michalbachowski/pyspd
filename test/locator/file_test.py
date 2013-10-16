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
from pyspd.locator.file import LocatorFile


class LocatorFileTestCase(unittest.TestCase):

    def setUp(self):
        self.lf = LocatorFile(*self.get_example_paths())

    def get_example_path_dir(self):
        if not hasattr(self, 'example_path_dir'):
            self.example_path_dir = os.path.join(os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))), 'examples')
        return self.example_path_dir

    def get_example_paths(self):
        if not hasattr(self, 'example_paths'):
            tmp = self.get_example_path_dir()
            self.example_paths = [os.path.join(tmp, 'plugin1.py'),
                os.path.join(tmp, 'plugin2.py')]
        return self.example_paths

    def test_init_allows_no_arguments(self):
        err = False
        try:
            LocatorFile()
        except:
            err = True
        self.assertFalse(err)

    def test_init_allows_to_pass_many_arguments(self):
        err = False
        try:
            LocatorFile('a')
            LocatorFile('a', None)
            LocatorFile('a', 'b')
            LocatorFile('a', 'f', 'sdfsdf')
        except:
            err = True
        self.assertFalse(err)

    def test_locator_raises_import_error_when_file_does_not_exist(self):
        lf = LocatorFile('/foo/bar/baz.py')
        self.assertRaises(ImportError, lf)

    def test_locator_skips_non_python_files(self):
        lf = LocatorFile(os.path.join(self.get_example_path_dir(), 'dummy.txt'))
        lf()
        self.assertFalse('dummy' in sys.modules.keys())

    def test_locator_imports_module_from_given_file(self):
        self.assertFalse('plugin1' in sys.modules.keys())
        self.assertFalse('plugin2' in sys.modules.keys())
        self.assertFalse('plugin3' in sys.modules.keys())

        self.lf()

        self.assertTrue('plugin1' in sys.modules.keys())
        self.assertTrue('plugin2' in sys.modules.keys())
        self.assertFalse('plugin3' in sys.modules.keys())


        lf = LocatorFile(os.path.join(self.get_example_path_dir(), 'plugin3'))
        lf()
        self.assertTrue('plugin3' in sys.modules.keys())


if "__main__" == __name__:
    unittest.main()
