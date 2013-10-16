pyspd
=====

Python Simple Plugin Discovery. It's merely about plugin discovery and registration by providing mount point for them.
Basic concepts were described by Marty Alchin back in 2008 in his blogpost [A Simple Plugin Framework](http://martyalchin.com/2008/jan/10/simple-plugin-framework/).

Python 2.7 and 3.x compatiblity
-------

As this library relies on mataclass it is difficult to support both Python 2.7 and 3.x.
To overcom this limitation I recommend using [six](https://bitbucket.org/gutworth/six) Python component:

```python
import six
from pyspd.plugins import MountPoint


six.add_metaclass(MountPoint)
class TemplateHooks(object):
    pass
```


LICENSE
-------

MIT
