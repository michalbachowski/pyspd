#!/usr/bin/env python
# -*- coding: utf-8 -*-


class LocatorInterface(object):
    """Interface for any locator class
    """

    def __call__(self):
        """
        Locates and loads plugin modules using built in strategy
        """
        raise NotImplementedError()
