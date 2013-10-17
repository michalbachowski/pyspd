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
from pyspd.locator.module import LocatorModule


class LocatorModuleTestCase(unittest.TestCase):

    def setUp(self):
        self.lf = LocatorModule(*self.get_example_modules())

    def get_example_path_dir(self):
        if not hasattr(self, 'example_path_dir'):
            self.example_path_dir = os.path.join(os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))), 'examples3')
        return self.example_path_dir

    def get_example_modules(self):
        tmp = self.get_example_path_dir()
        if tmp not in sys.path:
            sys.path.insert(0, tmp)
        return ['plug1', 'plug3', 'plug2.foo']

    def test_init_allows_no_arguments(self):
        err = False
        try:
            LocatorModule()
        except:
            err = True
        self.assertFalse(err)

    def test_init_allows_to_pass_many_arguments(self):
        err = False
        try:
            LocatorModule('a')
            LocatorModule('a', None)
            LocatorModule('a', 'b')
            LocatorModule('a', 'f', 'sdfsdf')
        except:
            err = True
        self.assertFalse(err)

    def test_locator_raises_import_error_when_module_could_not_be_imported(self):
        lf = LocatorModule('foo.bar.baz')
        self.assertRaises(ImportError, lf)

    def test_locator_imports_module_from_given_file(self):
        self.assertFalse('plug1' in sys.modules.keys())
        self.assertFalse('plug2.foo' in sys.modules.keys())
        self.assertFalse('plug3' in sys.modules.keys())

        self.lf()

        self.assertTrue('plug1' in sys.modules.keys())
        self.assertTrue('plug2.foo' in sys.modules.keys())
        self.assertTrue('plug3' in sys.modules.keys())


if "__main__" == __name__:
    unittest.main()
