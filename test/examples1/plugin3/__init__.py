#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyspd import MountPoint
import six


@six.add_metaclass(MountPoint)
class Plugin3MountPoint(MountPoint):
    pass


class Plugin3(Plugin3MountPoint):
    pass
