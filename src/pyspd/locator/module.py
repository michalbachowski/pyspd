#!/usr/bin/env python
# -*- coding: utf-8 -*-
import importlib
from pyspd.locator import LocatorInterface


class LocatorModule(LocatorInterface):
    """Locates plugins given as pure python module name (foo.bar.baz).
    Locator expects that PYTHONPATH is set correctly
    """
    def __init__(self, *modules):
        """
        Object initialization

        Arguments:
            :param     *modules: list of modules to be loaded
            :type      *modules: list
        """
        self.modules = set(modules)

    def __call__(self):
        """
        Loads plugins from given modules
        """
        for module in self.modules:
            importlib.import_module(module)
