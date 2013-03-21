Dell SK-8135 keyboard not working during boot (POST, BIOS, GRUB) on OptiPlex 990
################################################################################
:date: 2011-10-20 15:19
:author: davidjb
:category: Hardware
:tags: bios, dell, keyboard, post
:slug: dell-sk-8135-keyboard-not-working-during-boot-post-bios-grub-on-optiplex-990

.. note:: **Update**: Since this was written, Dell has released version A10 of
    their `OptiPlex 990 BIOS`_!  I've tested this on my 990 and my
    keyboard now works!

Just a quick note to anyone out there confused out of their mind if
their Dell keyboard isn't working with their computer during boot: there
is some incompatibility between the OptiPlex 990 and the Dell SK-8135
keyboard.  I'm using the A06 BIOS, which is latest at the time of
writing.

The result of this is that you cannot use the keyboard during boot, so
not within POST, not to enter the boot menu or BIOS, and the keyboard
does not work in my GRUB until I unplug it and plug it in again.  I've
tried two of these specific keyboards, revision P and revision S, and
both show the same issue.  I've also tried the keyboard on two different
OptiPlex 990 machines, and the result is the same.  All sorts of other
keyboards work fine though, and the SK-8135 works fine once you load an
OS -- so through this detective work, there must be something wrong with
the computer (aka with the BIOS).

So, just in case you hit the same issue, this is what I've found.  If
you find this too, please contact Dell and hopefully we can get a
resolution.

Cheers!

.. _OptiPlex 990 BIOS: http://www.dell.com/support/drivers/us/en/04/DriverDetails/DriverFileFormats?DriverId=N31V7&FileId=2775891360
