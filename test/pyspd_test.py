#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# python standard library
#
import unittest

##
# test helpers
#
#from testutils import IsA
import six

##
# content bits modules
#
from pyspd import MountPoint


@six.add_metaclass(MountPoint)
class TestMountPoint(object):
    pass


class TestPlugin(TestMountPoint):
    pass


class MountPointTestCase(unittest.TestCase):

    def setUp(self):
        self.th = TestPlugin()

    def test_plugins_attribute_is_present(self):
        self.assertTrue(hasattr(TestMountPoint, 'plugins'))

    def test_plugins_attribute_is_a_list(self):
        self.assertIsInstance(TestMountPoint.plugins, list)

    def test_plugins_are_registered(self):
        self.assertTrue(TestPlugin in TestMountPoint.plugins)

    def test_plugins_attribute_is_present_also_in_plugin_instances(self):
        self.assertTrue(hasattr(TestPlugin, 'plugins'))


if "__main__" == __name__:
    unittest.main()
