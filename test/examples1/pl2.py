#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyspd import MountPoint
import six


@six.add_metaclass(MountPoint)
class Plugin2MountPoint(MountPoint):
    pass


class Plugin2(Plugin2MountPoint):
    pass
