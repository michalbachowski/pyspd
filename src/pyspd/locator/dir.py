#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from pyspd.locator.file import LocatorFile


class LocatorDir(LocatorFile):
    """Locates plugins in given directory.
    By default any module (file or directory) inside this directory
    will be treated as potential plugin"""

    def __call__(self):
        """
        Loads a set of plugins at the given path.
        """
        for path in self._files:
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
