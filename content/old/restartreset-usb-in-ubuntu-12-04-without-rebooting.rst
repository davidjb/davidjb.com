Restart/reset USB in Ubuntu 12.04 without rebooting
###################################################
:date: 2012-06-25 10:34
:author: davidjb
:category: IT
:tags: linux, power, reset, restart, ubuntu, usb
:slug: restartreset-usb-in-ubuntu-12-04-without-rebooting

Either my Dell Optiplex 990 computer or my Linux install has an issue:
occasionally, when I re-plug a USB device into the system, it'll cause a
fault in the USB module in the kernel and USB goes dark. I'm unsure as
to whether this is a hardware or software issue, but I'd simply like to
restart my USB subsystem and continue working. When searching the web
for 'restart USB in Linux' and 'reload USB kernel module', you get a
plethora of results and none of which will work (seemingly due to how
the Ubuntu standard kernel is compiled), at least for me within Ubuntu
12.04, Precise Pangolin. Until now, I've had no success and had to hard
reset. No longer.

You'll need root/sudo access to the machine to be able to run commands.
In my case, without USB available, then I've either got to sprint for a
PS/2 keyboard and mouse or login via SSH. You can do what I've done and
prepared things into a suitable script I can run with just a Gnome
launcher.  Thanks to this `fantastic post`_ for the help. Either place
the following into a script or run the commands directly:

.. code:: bash

    echo -n "0000:00:1a.0" | tee /sys/bus/pci/drivers/ehci_hcd/unbind
    echo -n "0000:00:1d.0" | tee /sys/bus/pci/drivers/ehci_hcd/unbind
    echo -n "0000:00:1a.0" | tee /sys/bus/pci/drivers/ehci_hcd/bind
    echo -n "0000:00:1d.0" | tee /sys/bus/pci/drivers/ehci_hcd/bind

The hardware identifiers being passed around here can be revealed using
a command like ``lspci | grep USB``. In my case, the identifiers in the
original post were exactly what I have in my system.

I'm yet to see if my USB will correctly come back online after freezing
up as it hasn't happened yet, but I'll try this when it does and report
back. That said, the commands above definitely reload all USB devices
attached to the system; that much I've tried.

.. _fantastic post: http://ubuntuforums.org/showpost.php?p=9162799&postcount=1
