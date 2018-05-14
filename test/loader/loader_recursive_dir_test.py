##
# python standard library
#
import unittest
import os
import sys

##
# content bits modules
#
from pyspd.loader import LoaderRecursiveDir


class LoaderRecursiveDirTestCase(unittest.TestCase):

    def setUp(self):
        self.lr = LoaderRecursiveDir()

    def get_example_paths(self):
        if not hasattr(self, 'example_paths'):
            tmp = os.path.join(os.path.dirname(os.path.dirname(
                os.path.abspath(__file__))), 'examples4')
            self.example_paths = [tmp]
        return self.example_paths

    def test_init_allows_no_arguments(self):
        err = False
        try:
            LoaderRecursiveDir()
        except:
            err = True
        self.assertFalse(err)

    def test_init_requires_no_arguments(self):
        with self.assertRaises(TypeError):
            LoaderRecursiveDir('a')

    def test_locator_raises_os_error_when_directory_does_not_exist(self):
        with self.assertRaises(OSError):
            self.lr.load(['/foo/bar/baz.py'])

    def test_locator_imports_module_from_given_directories(self):
        self.assertFalse('plg1' in sys.modules.keys())
        self.assertFalse('plg2' in sys.modules.keys())
        self.assertFalse('plg3' in sys.modules.keys())
        self.assertFalse('loaded3' in sys.modules.keys())
        self.assertFalse('loaded4' in sys.modules.keys())

        self.lr.load(self.get_example_paths())

        self.assertTrue('plg1' in sys.modules.keys())
        self.assertTrue('plg2' in sys.modules.keys())
        self.assertTrue('plg3' in sys.modules.keys())
        self.assertTrue('loaded3' in sys.modules.keys())
        self.assertTrue('loaded4' in sys.modules.keys())


if "__main__" == __name__:
    unittest.main()

