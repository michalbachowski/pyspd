##
# python standard library
#
import unittest
import os
import sys

##
# content bits modules
#
from pyspd.loader import LoaderModule


class LoaderModuleTestCase(unittest.TestCase):

    def setUp(self):
        self.lm = LoaderModule()

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
            LoaderModule()
        except:
            err = True
        self.assertFalse(err)

    def test_init_requires_no_arguments(self):
        with self.assertRaises(TypeError):
            LoaderModule('a')

    def test_locator_raises_import_error_when_module_could_not_be_imported(self):
        with self.assertRaises(ImportError):
            self.lm.load(['foo.bar.baz'])

    def test_locator_imports_module_from_given_file(self):
        self.assertFalse('plug1' in sys.modules.keys())
        self.assertFalse('plug2.foo' in sys.modules.keys())
        self.assertFalse('plug3' in sys.modules.keys())

        self.lm.load(self.get_example_modules())

        self.assertTrue('plug1' in sys.modules.keys())
        self.assertTrue('plug2.foo' in sys.modules.keys())
        self.assertTrue('plug3' in sys.modules.keys())


if "__main__" == __name__:
    unittest.main()
