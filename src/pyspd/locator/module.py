#!/usr/bin/env python
# -*- coding: utf-8 -*-
import importlib
from warnings import warn
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
        warn("pyspd.locator.module.LocatorModule is deprecated." +
             "Use pyspd.loader.LoaderModule instead")
        self._modules = list(modules)

    def __call__(self):
        """
        Loads plugins from given modules
        """
        warn("pyspd.locator.module.LocatorModule is deprecated." +
             "Use pyspd.loader.LoaderModule instead")
        for module in self._modules:
            importlib.import_module(module)
