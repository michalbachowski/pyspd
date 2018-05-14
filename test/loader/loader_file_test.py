##
# python standard library
#
import unittest
import os
import sys

##
# content bits modules
#
from pyspd.loader import LoaderFile


class LoaderFileTestCase(unittest.TestCase):

    def setUp(self):
        self.lf = LoaderFile()

    def get_example_path_dir(self):
        if not hasattr(self, 'example_path_dir'):
            self.example_path_dir = os.path.join(os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))), 'examples1')
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
            LoaderFile()
        except:
            err = True
        self.assertFalse(err)

    def test_init_requires_no_arguments(self):
        with self.assertRaises(TypeError):
            LoaderFile('a')

    def test_locator_raises_import_error_when_file_does_not_exist(self):
        with self.assertRaises(ImportError):
            self.lf.load(['/foo/bar/baz.py'])

    def test_locator_skips_non_python_files(self):
        self.lf.load([os.path.join(self.get_example_path_dir(), 'dummy.txt')])
        self.assertFalse('dummy' in sys.modules.keys())

    def test_locator_imports_module_from_given_file(self):
        self.assertFalse('plugin1' in sys.modules.keys())
        self.assertFalse('plugin2' in sys.modules.keys())
        self.assertFalse('plugin3' in sys.modules.keys())

        self.lf.load(self.get_example_paths())

        self.assertTrue('plugin1' in sys.modules.keys())
        self.assertTrue('plugin2' in sys.modules.keys())
        self.assertFalse('plugin3' in sys.modules.keys())

        self.lf.load([os.path.join(self.get_example_path_dir(), 'plugin3')])
        self.assertTrue('plugin3' in sys.modules.keys())


if "__main__" == __name__:
    unittest.main()
