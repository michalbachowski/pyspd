#!/usr/bin/env python
# -*- coding: utf-8 -*-
import importlib
import os
import sys
from pyspd.locator import LocatorInterface


class LocatorFile(LocatorInterface):
    """Locates plugins in given file or directory.
    Loads module from given file or directory"""
    def __init__(self, *files):
        """
        Object initialization

        Arguments:
            :param     *files: list of files or directories to be examined when looking for plugins
            :type      *files: list
        """
        self._files = list(files)
        self._module_name_cache = []

    def __call__(self):
        """
        Loads a set of plugins at the given path.
        """
        for path in self._files:
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
        name = self._prepare_module_name(path, filename)
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
        if '__pycache__' == item:
            return
        if item.startswith('__init__.py'):
            return os.path.basename(plugin_dir)
        if item.endswith(".py"):
            return item[:-3]
        if item.endswith(".pyc"):
            return item[:-4]
        if os.path.isdir(os.path.join(plugin_dir, item)):
            return item

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
        importlib.import_module(name)
