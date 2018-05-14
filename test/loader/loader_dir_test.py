##
# python standard library
#
import unittest
import os
import sys

##
# content bits modules
#
from pyspd.loader import LoaderDir


class LoaderDirTestCase(unittest.TestCase):

    def setUp(self):
        self.loader = LoaderDir()

    def get_example_paths(self):
        if not hasattr(self, 'example_paths'):
            tmp = os.path.join(os.path.dirname(os.path.dirname(
                os.path.abspath(__file__))), 'examples2')
            self.example_paths = [tmp]
        return self.example_paths

    def test_init_requires_no_arguments(self):
        err = False
        try:
            LoaderDir()
        except:
            err = True
        self.assertFalse(err)

        with self.assertRaises(TypeError):
            LoaderDir('a')

    def test_loader_raises_os_error_when_directory_does_not_exist(self):
        with self.assertRaises(OSError):
            self.loader.load(['/foo/bar/baz.py'])

    def test_locator_imports_module_from_given_dir(self):
        self.assertFalse('pl1' in sys.modules.keys())
        self.assertFalse('pl2' in sys.modules.keys())
        self.assertFalse('pl3' in sys.modules.keys())
        self.assertFalse('not_loaded_2' in sys.modules.keys())

        self.loader.load(self.get_example_paths())

        self.assertTrue('pl1' in sys.modules.keys())
        self.assertTrue('pl2' in sys.modules.keys())
        self.assertTrue('pl3' in sys.modules.keys())
        self.assertFalse('not_loaded_2' in sys.modules.keys())


if "__main__" == __name__:
    unittest.main()

