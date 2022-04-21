Updating the BIOS on a Supermicro Motherboard
##############################################

:date: 2021-01-17
:category: Tech
:tags: Hardware, RAM, Computers

Supermicro provides BIOS upgrades for its motherboards and some particular
models' upgrades require the use of a DOS-based environment to be applied. If
you're reading this, you'll already have noted that the README supplied with
the upgrade ``.zip`` file isn't overly helpful on getting set up with a
suitable environment to *safely* run the BIOS upgrade. Likewise, if you've
tried to actually run the included ``FLASH.BAT`` file, you'll probably have
found it doesn't quite work.  Hence, these instructions to guide you.

#. Before we get started, bear in mind that flashing your BIOS will delete all
   of your settings, boot ordering *and* your administrative password. Take a
   note of everything before you start.

#. Download FreeDOS_ (I used the v1.2 Lite USB file) and flash this bootable
   image to a USB stick (I use either Etcher_ or Rufus_)

#. Download the `bios upgrade`_ from Supermicro and extract this zip archive
   onto the USB stick you just created.  If your FreeDOS partition only takes
   up the first few MBs of the USB, then just create a second partition after
   the FreeDOS one - to be supported in DOS, it will need to be small (I just
   picked 128MB), be FAT formatted and have a small sector size (16KB is
   fine).

#. Insert your FreeDOS USB drive into your computer's motherboard and boot
   from it.

#. At this point, you'll be prompted to *install* FreeDOS, so exit out of that
   - you'll return to a ``C:\>`` prompt.

#. Change to the drive/directory where your BIOS upgrade is located. In my
   case, this is ``D:\``, as I had to create a second partition.

#. Run ``FLASH.BAT BIOSname#.###``, where ``BIOSname#.###`` is the name of the
   BIOS image, named for your motherboard's model and the release date (which
   in itself is confusingly ambiguous, using a single digit for the year and
   single digit for month).

#. ``FLASH.BAT`` sets your motherboard up to enter "flash mode" and then
   unhelpfully tries to automatically reboot the machine and in order to
   re-run itself on next boot by creating and/or modifying an ``autoexec.bat``
   file.  Unfortunately, it makes no attempts to figure out *where*
   ``FLASH.BAT`` is actually running from, so when your computer does reboot,
   the autoexec will fail.

   Oh, and here the big thing to remember - since you're manually booting into
   this USB stick, when your computer reboots you **must** ensure you boot
   back into the FreeDOS USB.

#. So, now you're back in FreeDOS after the reboot and ``autoexec.bat`` has
   failed. Change back to the drive/directory where your BIOS upgrade is located.

#. Run the exact same ``FLASH.BAT BIOSname#.###`` command again and your BIOS
   upgrade will begin this time as your hardware flags are set correctly to
   allow flashing to occur.

#. Let the process complete and when done, press Control + Alt + Delete to
   reboot.

#. This first bootup will take a little longer than expected (about a minute
   or so) - I imagine this is performing detailed hardware or other tests now
   that the BIOS memory was cleared.

That's it - all done.  If you're interested in what happens under the hood, or
you hit some sort of other problem, ``FLASH.BAT`` is a quick read and running
the individual flash commands is possible too if you had to.

.. _FreeDOS: https://www.freedos.org/download/
.. _Etcher: https://www.balena.io/etcher/
.. _Rufus: https://rufus.ie/
.. _bios upgrade: https://www.supermicro.com/support/resources/bios_ipmi.php
