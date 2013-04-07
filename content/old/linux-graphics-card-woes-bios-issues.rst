Linux: Graphics Card Woes & BIOS Issues
#######################################
:date: 2009-01-27 08:44
:author: davidjb
:category: IT, Linux, Work
:tags: bios, driver, graphics, linux, problem, ubuntu
:slug: linux-graphics-card-woes-bios-issues

…and I had thought that installing a graphics card in a computer was as
easy as opening the case, inserting the card, and booting the machine
(then Xorg config etc). Well, to tell the truth, I just moved my HDD,
peripherals (gfx card included) to a new box - now a Dell OptiPlex 755.
But, it's not that easy if you can't boot your Ubuntu 8.10 OS!

The computer kept spitting this message out, even though it just worked
a few days ago::

    15.848000 NVRM: This PCI I/O region assigned to your NVIDIA device is invalid:
    15.848000 NVRM: BAR1 is 0M @ 0x00000000 (PCI:0001:00.0)
    15.848000 NVRM: The system BIOS may have misconfigured your graphics card.
    15.848000 NVRM: The NVIDIA probe routine failed for 1 device(s)
    15.848000 NVRM: None of the NVIDIA graphics adapters were initialized!
    15.848000 NVRM: This PCI I/O region assigned to your NVIDIA device is invalid:

After much pain, I managed to get into the computer and have the network
loaded up (yay). Some hours of searching, I'd stumbled onto Dell's
Official solution to driver updates (biosdisk); no luck because the boot
disk wouldn't load the EXE. Tried the official method from Ubuntu's
wiki; no luck since my BIOS couldn't be found in the package repo.

Final ditch effort to do it manually led me to this:
http://bigbrovar.wordpress.com/2008/12/07/upgrade-downgrade-your-dell-bios-on-ubuntu/

And, it works! Turns out on my system I didn't even need to edit the
/boot/grub/menu.lst file (BIOS just updates itself upon reboot).

And then, like magic, everything's fine. My whole system is back working
again after just that one (major) fix.

Back to work for me…

