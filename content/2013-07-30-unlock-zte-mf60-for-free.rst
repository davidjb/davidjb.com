Unlocking your Telstra Elite (ZTE MF60) Mobile Wi-fi Device for Free
####################################################################

:category: Freebies

Ha, that's a dodgy-sounding title if I ever heard one.  If you're
reading this, then I'll assure you that these instructions are real,
open, and free, and that I've used them to unlock my device.  Read on...

**Update**: I should mention that hexecute's site at
https://sites.google.com/site/mf60guide/ now mentions his patch can unlock as
well.  I haven't tried that, but from memory, the Windows drivers that are
available on that site didn't work with my MF60 - presumably a different model
or something similar.  If what's there doesn't work for you, try my
instructions below.  Otherwise, go for it because one-click seems a lot
simpler!

Instructions
~~~~~~~~~~~~

So, I've just unlocked my Telstra Elite MF60 for free.  It's effectively just a
matter of flashing the generic ZTE firmware once, and disconnecting the device
during its restore process (at about 80% complete) when the SIM lock hasn't
been applied yet.  After doing this, flashing the firmware again finishes
successfully but without a lock in place. The only issue I had was getting the
drivers for initial installation when connecting to my computer, but that's
about it. Thankfully for you, I've extracted these drivers and they're
available for download below. 

You'll need
^^^^^^^^^^^

#. A physical Windows-based PC.  I used Windows 7.
#. These downloads:

  * `ZTE Generic firmware <http://download.ztedevices.com/UploadFiles/product/643/2586/soft/P020120813336503279684.zip>`_ (`Mirror <https://drive.google.com/a/davidjb.com/file/d/0B5CAsXBD5-mARHBUek9Wb2pfT1U/view>`__)

  * `Firmware version check patch <https://sites.google.com/site/mf60guide/MF60-patch.zip?attredirects=0>`_ -
    (Thanks to Hexecute @ https://sites.google.com/site/mf60guide/)

    (`Mirror <https://docs.google.com/file/d/0B5CAsXBD5-mAbzZKOFRwM3RfdkE/view>`__)

  * Drivers for Telstra Elite device circa June 2013):
    `ZTEMODEM.ISO <https://docs.google.com/file/d/0B5CAsXBD5-mAV2k1NGpKU1JJVkk/view>`_

Process
^^^^^^^

#. Download Telstra Elite ZTEMODEM.iso, the generic ZTE firmware, and the patch

#. Install the drivers from the ISO. You can either mount the ISO or extract
   it using a program like 7Zip.  Note that these drivers are different
   to other ``ZTEMODEM.iso`` drivers around.  

   For me, they've been tested on a Telstra Elite MF60 purchased in June 2013,
   so YMMV.

#. Plug in the MF60 modem via your USB port, or if it was already plugged in,
   or redetect devices in your Device Manager.  You'll notice that several COM
   ports are now installed. Without the correct drivers installed, you won't see
   these COM devices load.  In my situation, I only ever saw the *ZTE MMC Mass
   Storage Device* installed.

#. Run the generic firmware updater, and run the memory-based patch to allow
   the firmware to actually start working.  Without the patch, as you may see,
   the updater will refuse to work because it thinks the firmware is
   incompatible.  Start the firmware updating.

#. Let the firmware update but upon reaching 80%, you'll notice that your
   modem will reset & display a ZTE logo on screen.  When you see this,
   disconnect the USB plug.

   If you had a foreign SIM card in the modem at this point, you'll see why 
   - the SIM lock is not engaged!  

#. Close the firmware updater and ignore the warning message.

#. Re-run firmware updater one more time (no patch needed now). 
   Let it run through and finish.

That's it - your device is unlocked and on awesome generic firmware!

If you haven't already, install a foreign SIM card into the modem.
Enjoy your unlocked MF60!  

The default wifi network name is ``ufi_999999`` and password of ``12345678``.
Accesss your modem at http://192.168.0.1/ and login using the password
``admin``.  

You should probably change these :)

