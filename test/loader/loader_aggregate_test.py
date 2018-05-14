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
from pyspd.loader import LoaderInterface, LoaderAggregate


class LoaderAggregateTestCase(unittest.TestCase):

    def setUp(self):
        self.l1 = mock.Mock(LoaderInterface)
        self.l2 = mock.Mock(LoaderInterface)
        self.lf = LoaderAggregate([self.l1, self.l2])

    def test_init_disallows_no_arguments(self):
        with self.assertRaises(TypeError):
            LoaderAggregate()

    def test_init_allows_to_pass_one_argument(self):
        err = False
        try:
            LoaderAggregate('a')
        except:
            err = True
        self.assertFalse(err)

        with self.assertRaises(TypeError):
            LoaderAggregate('a', None)

    def test_loader_calls_all_aggregated_locators(self):
        names = ['foo', 'bar', 123]
        self.lf.load(names)
        self.l1.load.assert_called_once_with(names)
        self.l2.load.assert_called_once_with(names)


if "__main__" == __name__:
    unittest.main()

