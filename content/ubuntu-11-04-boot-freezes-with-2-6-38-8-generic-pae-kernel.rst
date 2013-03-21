Ubuntu 11.04 boot freezes with 2.6.38-8-generic-pae kernel
##########################################################
:date: 2011-05-05 15:46
:author: davidjb
:category: Linux
:tags: 11.04, boot, frozen, kernel, natty, ubuntu
:slug: ubuntu-11-04-boot-freezes-with-2-6-38-8-generic-pae-kernel

So you've just installed 32-bit Ubuntu 11.04 (Natty Narwhal), and in my
case, upgraded from Ubuntu 10.04 (Maverick Meerkat).  The upgrade
process seemingly went fine and then you were asked to restart your
computer.  You diligently do so, only to come back to find that your
computer has frozen at GRUB2 upon trying to boot the
2.6.38-8-generic-pae kernel from the GRUB list.  Now what?  How do you
fix this?

The issue appears to stem from some form of installation issue where
this new kernel isn't set up right.  Note: I don't actually know what's
wrong and can't investigate.

The good news is that you can use the 'Previous Versions' entry in the
GRUB listing to boot to one of your older kernels and get your system
started.  Once you're booted, then load up Synaptic Package Manager and
(re-)install::

    linux-image-2.6.38-8-generic-pae linux-generic-pae linux-headers-generic-pae linux-image-generic-pae linux-headers-2.6.38-8-generic-pae

You should now be able to restart your computer and use the PAE-based
kernel. Thanks to a post on the Ubuntu forums for pointing me in the
right direction.
