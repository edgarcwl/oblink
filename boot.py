# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
print('boot')
import gc
import vfs
from flashbdev import bdev
try:
    if bdev:
        vfs.mount(bdev, "/")
except OSError:
    import inisetup
    inisetup.setup()

gc.collect()

import ota
import main