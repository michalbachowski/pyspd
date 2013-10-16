pyspd
=====

Python Simple Plugin Discovery

Python 2.7 and 3.x compatiblity
-------

As this library relies on mataclass it is difficoult to support both Python 2.7 and 3.x.
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
