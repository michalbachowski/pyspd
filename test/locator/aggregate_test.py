#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# python standard library
#
import unittest

##
# testutils
#
from testutils import mock

##
# content bits modules
#
from pyspd.locator.aggregate import LocatorAggregate


class LocatorAggregateTestCase(unittest.TestCase):

    def setUp(self):
        self.l1 = mock.MagicMock()
        self.l2 = mock.MagicMock()
        self.l3 = mock.MagicMock()
        self.lf = LocatorAggregate(self.l1, self.l2)

    def test_init_allows_no_arguments(self):
        err = False
        try:
            LocatorAggregate()
        except:
            err = True
        self.assertFalse(err)

    def test_init_allows_to_pass_many_arguments(self):
        err = False
        try:
            LocatorAggregate('a')
            LocatorAggregate('a', None)
            LocatorAggregate('a', 'b')
            LocatorAggregate('a', 'f', 'sdfsdf')
        except:
            err = True
        self.assertFalse(err)

    def test_append_requires_one_argument(self):
        self.assertRaises(TypeError, self.lf.append)
        err = False
        try:
            self.lf.append(self.l1)
        except:
            err = True
            raise
        self.assertFalse(err)

    def test_locator_all_aggregated_locators(self):
        self.lf.append(self.l3)
        self.lf()
        self.l1.assert_called_once_with()
        self.l2.assert_called_once_with()
        self.l3.assert_called_once_with()


if "__main__" == __name__:
    unittest.main()
