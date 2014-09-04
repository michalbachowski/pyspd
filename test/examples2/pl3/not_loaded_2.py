#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyspd import MountPoint
import six


@six.add_metaclass(MountPoint)
class Plugin4MountPoint(MountPoint):
    pass


class Plugin4(Plugin4MountPoint):
    pass
