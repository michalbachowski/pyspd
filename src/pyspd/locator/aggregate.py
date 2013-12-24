#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyspd.locator import LocatorInterface


class LocatorAggregate(LocatorInterface):
    """Plugin locator that aggregates other plugin locators"""

    def __init__(self, *args):
        """Object initialization

        Arguments:
            :param    *args: locators to be aggregated
            :type     *args: callable
        """
        self.locators = list(args)

    def append(self, locator):
        """Append new locator

        Arguments:
            :param    locator: locator to be appended
            :type     locator: callable
        :returns: LocatorAggregate
        """
        if locator not in self.locators:
            self.locators.append(locator)
        return self

    def __call__(self):
        """
        Locates plugins using given locators
        """
        for locate in self.locators:
            locate()
