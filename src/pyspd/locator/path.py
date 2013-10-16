#!/usr/bin/env python
# -*- coding: utf-8 -*-
import importlib
import os
import sys
from pyplugins.locator import LocatorInterface


class LocatorPath(LocatorInterface):
    """Locates plugins in given directory.
    By default any module (file or directory) inside this directory
    will be treated as potential plugin"""

    def __init__(self, *paths):
        """
        Object initialization

        Arguments:
            :param     *paths: list of paths to be searched when looking for plugins
            :type      *paths: list
        """
        self.paths = set(paths)
        self.module_name_cache = []

    def __call__(self):
        """
        Loads a set of plugins at the given path.
        """
        for path in self.paths:
            self.find_plugins_in_path(path)

    def find_plugins_in_path(self, path):
        """Looks for plugins in given path
        """
        plugin_dir = os.path.realpath(path)

        for filename in os.listdir(plugin_dir):
            self.load_module_from_file(path, filename)

    def load_module_from_file(self, path, filename):
        """Loads module from given file and path

        Arguments:
            :param    path: path where file is placed
            :type     path: string
            :param    filename: name of file to load
            :type     filename: string
        """
        name = self.prepare_module_name(path, filename)
        if not self.valid_module_name(name):
            return

        self.import_module(path, name)

    def prepare_module_name(self, plugin_dir, item):
        """
        Prepares name of module to load

        Arguments:
            :param    plugin_dir: directory where module is placed
            :type     plugin_dir: string
            :param    item: name of module file (might be file of directory)
            :type     item: string
        :returns: string -- name of module to load
        """
        if item.endswith(".py"):
            return item[:-3]
        if item.endswith(".pyc"):
            return item[:-4]
        if os.path.isdir(os.path.join(plugin_dir, item)):
            return item

    def valid_module_name(self, name):
        """Checks if given module name is valid

        Arguments:
            :param    name: module name
            :type     name: string
        :returns: bool -- information whether module name is valid
        """
        if name is None:
            return False
        if name in self.module_name_cache:
            return False
        return True

    def import_module(self, path, name):
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
