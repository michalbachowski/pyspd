#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from logging import getLogger


from pyspd.locator.file import LocatorFile


logger = getLogger(__name__)

class LocatorRecursiveDir(LocatorFile):
    """Locates plugins in given directory recursively.
    By default any files inside this directory
    will be treated as potential plugin"""

    def __call__(self):
        """
        Loads a set of plugins at the given path.
        """
        logger.debug('loading plugins from paths: %s', ' '.join(self._files))

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
            self._handle_path(plugin_dir, filename)

    def _handle_path(self, plugin_dir, filename):
        tmp_dir = os.path.join(plugin_dir, filename)
        if os.path.isdir(tmp_dir):
            logger.debug('filename is dir, searching recursively; name=%s',\
                            filename)
            self._find_plugins_in_path(tmp_dir)
            return

        logger.debug('filename is file, loading; name=%s', filename)
        self._load_module_from_file(plugin_dir, filename)
