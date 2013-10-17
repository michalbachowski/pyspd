#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyspd import MountPoint
import six


@six.add_metaclass(MountPoint)
class Plugin1MountPoint(MountPoint):
    pass


class Plugin1(Plugin1MountPoint):
    pass
