#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from itertools import takewhile
from logging import getLogger

from six.moves import map, filterfalse, filter

from pyspd.locator.file import LocatorFile


logger = getLogger(__name__)

def _get_extension_checker(filename):
    return lambda ext: filename.endswith(ext)

class LocatorRecursiveDir(LocatorFile):
    """Locates plugins in given directory recursively.
    By default any files inside this directory
    will be treated as potential plugin"""

    def __init__(self, *files):
        """
        Object initialization

        Arguments:
            :param     *files: list of files or directories to be examined when looking for plugins
            :type      *files: list
        """
        self._skip_names = []
        self._skip_ext = []
        self.skip('__pycache__', '*.pyc')
        LocatorFile.__init__(self, *files)

    def __call__(self):
        """
        Loads a set of plugins at the given path.
        """
        logger.debug('loading plugins from paths: %s', ' '.join(self._files))
        logger.debug('file names explicitly skipped: %s', \
                     ' '.join(self._skip_names))
        logger.debug('file extensions skipped: %s', ' '.join(self._skip_ext))

        for path in self._files:
            self._find_plugins_in_path(path)

    def skip(self, *files):
        test = lambda f: f.startswith('*')
        self._skip_names.extend(filterfalse(test, files))
        self._skip_ext.extend(map(lambda f: f[1:], filter(test, files)))
        return self

    def _should_skip_file(self, filename):
        if filename in self._skip_names:
            logger.debug('filename explicitly skipped; name=%s', filename)
            return True

        found_extensions = list(takewhile(_get_extension_checker(filename), \
                                        self._skip_ext))
        if len(found_extensions) == len(self._skip_ext):
            logger.debug('filename extension disallowed; name=%s', filename)
            return True

        return False

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
        logger.debug('examinining file; name=%s', filename)
        if self._should_skip_file(filename):
            return

        tmp_dir = os.path.join(plugin_dir, filename)
        if os.path.isdir(tmp_dir):
            logger.debug('filename is dir, searching recursively; name=%s',\
                            filename)
            self._find_plugins_in_path(tmp_dir)
            return

        logger.debug('filename is file, loading; name=%s', filename)
        self._load_module_from_file(plugin_dir, filename)
