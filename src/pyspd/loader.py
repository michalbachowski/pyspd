import importlib
from logging import getLogger
import os
import sys


logger = getLogger(__name__)


class LoaderInterface(object):
    """Interface for any loader class"""

    def load(self, names):
        """
        Locates and loads plugin modules using built in strategy

        Arguments:
            :param    names: names (paths, module names) to be loaded
            :type     names: Iterable[str]
        """
        raise NotImplementedError()


class LoaderAggregate(LoaderInterface):
    """Plugin loader that aggregates other plugin loaders"""

    def __init__(self, loaders):
        """Object initialization

        Arguments:
            :param    loaders: loaders to be aggregated
            :type     loaders: Iterable[LoaderInterface]
        """
        self._loaders = list(loaders)

    def load(self, names):
        """
        Loads plugins using given loaders

        Arguments:
            :param    names: names (paths, module names) to be loaded
            :type     names: Iterable[str]
        """
        for loader in self._loaders:
            loader.load(names)


class LoaderFile(LoaderInterface):
    """Loads plugins in given file or directory.
    Loads module from given file or directory"""

    def __init__(self):
        """
        Object initialization
        """
        self._module_name_cache = []

    def load(self, names):
        """
        Loads a set of plugins at the given path.

        Arguments:
            :param    names: file paths to load plugin from
            :type     names: Iterable[str]
        """
        for path in names:
            filename = os.path.basename(path)
            dirname = os.path.dirname(path)
            self._load_module_from_file(dirname, filename)

    def _load_module_from_file(self, path, filename):
        """Loads module from given file and path

        Arguments:
            :param    path: path where file is placed
            :type     path: string
            :param    filename: name of file to load
            :type     filename: string
        """
        logger.debug("loading module from file; path=[%s]; filename=[%s]",
                     path, filename)
        (path, name) = self._prepare_module_name(path, filename)
        if not self._valid_module_information(path, name):
            return

        self._import_module(path, name)

    def _prepare_module_name(self, plugin_dir, item):
        """
        Prepares name of module to load

        Arguments:
            :param    plugin_dir: directory where module is placed
            :type     plugin_dir: string
            :param    item: name of module file (might be file of directory)
            :type     item: string
        :returns: string -- name of module to load
        """
        if item == '__pycache__':
            return (None, None)
        if item.startswith('__init__.py'):
            return (os.path.dirname(plugin_dir), os.path.basename(plugin_dir))
        if item.endswith(".py"):
            return (plugin_dir, item[:-3])
        if item.endswith(".pyc"):
            return (None, None)
        if os.path.isdir(os.path.join(plugin_dir, item)):
            return (plugin_dir, item)
        return (None, None)

    def _valid_module_information(self, path, name):
        """Checks if given module name is valid

        Arguments:
            :param    name: module name
            :type     name: string
        :returns: bool -- information whether module name is valid
        """
        if name is None:
            return False
        tmpname = os.path.join(path, name)
        if tmpname in self._module_name_cache:
            return False
        self._module_name_cache.append(tmpname)
        return True

    def _import_module(self, path, name):
        """
        Imports module given as path to directory and module name

        Arguments:
            :param    path: path to import module from
            :type     path: string
            :param    name: name of module
            :type     name: string
        :returns: object -- loaded module
        """
        if path not in sys.path:
            sys.path.insert(0, path)
        logger.debug('loading module; module=%s; sys.path=%s', name,
                     ' '.join(sys.path))
        importlib.import_module(name)


class LoaderDir(LoaderFile):
    """Loads plugins in given directory.
    By default any module (file or directory) inside this directory
    will be treated as potential plugin"""

    def load(self, names):
        """
        Loads a set of plugins at the given path.

        Arguments:
            :param    names: path to directories to load plugins from
            :type     names: Iterable[str]
        """
        for path in names:
            logger.debug("Loading directory; dir=[%s]", path)
            self._find_plugins_in_path(path)

    def _find_plugins_in_path(self, path):
        """Looks for plugins in given path

        Arguments:
            :param    path: path to search for plugins in
            :type     path: string
        """
        plugin_dir = os.path.realpath(path)

        for filename in os.listdir(plugin_dir):
            self._load_module_from_file(plugin_dir, filename)


class LoaderRecursiveDir(LoaderFile):
    """Loads plugins in given directory recursively.
    By default any files inside this directory
    will be treated as potential plugin"""

    def load(self, names):
        """
        Loads a set of plugins at the given path.

        Arguments:
            :param    names: path to directories to load plugins from
            :type     names: Iterable[str]
        """
        logger.debug('loading plugins from paths: %s', ' '.join(names))

        for path in names:
            self._find_plugins_in_path(path)

    def _find_plugins_in_path(self, path):
        """Looks for plugins in given path

        Arguments:
            :param    path: path to search for plugins in
            :type     path: string
        """
        plugin_dir = os.path.realpath(path)

        for filename in os.listdir(plugin_dir):
            self._handle_path(plugin_dir, filename)

    def _handle_path(self, plugin_dir, filename):
        tmp_dir = os.path.join(plugin_dir, filename)
        if os.path.isdir(tmp_dir):
            logger.debug('filename is dir, searching recursively; name=%s',
                         filename)
            self._find_plugins_in_path(tmp_dir)
            return

        logger.debug('filename is file, loading; name=%s', filename)
        self._load_module_from_file(plugin_dir, filename)


class LoaderModule(LoaderInterface):
    """Loads plugins given as pure python module name (foo.bar.baz).
    Loader expects that PYTHONPATH is set correctly
    """

    def load(self, names):
        """
        Loads plugins from given modules

        Arguments:
            :param    names: names of modules to be loaded
            :type     names: Iterable[str]
        """
        for module in names:
            importlib.import_module(module)

