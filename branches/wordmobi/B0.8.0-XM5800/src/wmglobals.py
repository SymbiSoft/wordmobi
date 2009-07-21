# -*- coding: utf-8 -*-

__all__ = [ "VERSION", "DEFDIR", "MIFFILE", "PERSIST", "TOUCH_ENABLED" ]

# always 3 numbers with two digits each maximum, e.g. 3.44.2, 4.2.33 ...
VERSION = "0.8.0" 
import e32
if e32.in_emulator():
    import sys
    import os
    DEFDIR = os.path.join(os.path.dirname(sys.argv[0]),"wordmobi_tmp")
    if not os.path.exists(DEFDIR):
        os.makedirs(DEFDIR)
else:
    DEFDIR = "e:\\wordmobi\\"
MIFFILE = "wordmobi2.mif"
PERSIST = "persist.bin"

try:
    from appuifw import touch_enabled
    TOUCH_ENABLED = touch_enabled()
except:
    # python < 1.9.3 does not support touch ui
    TOUCH_ENABLED = False
    