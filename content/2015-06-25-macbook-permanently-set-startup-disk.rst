Configuring rEFInd boot manager as your startup disk on a Mac
#############################################################

:category: Tech

So I've installed Ubuntu on the metal of my MacBook Pro Retina (13 inch, if
you must know) and in order to dual-boot the machine, I use the `rEFInd Boot
Manager <http://www.rodsbooks.com/refind/>`_.

It works really well and was simple to configure, but I found that after
upgrading to Yosemite (10.10), Mac OS X became the default boot OS, whereas
rEFInd was booting by default originally.

Originally, this was fine, I dealt with just holding the ``Option`` key down
during boot to bring up the `Startup Manager
<https://support.apple.com/en-au/HT204417>`_ and selecting ``EFI Boot`` in
order to get into Linux.  I wasn't restarting the computer that much anyway.
But like most things, eventually, it irked me enough that I set out to fix it.

Normally, in OS X, to change the boot drive, you'd use System Preferences and
change your Startup Disk but in this case, you won't see your EFI partition
available to be selected.  Likewise, even if you go ahead and follow rEFInd's
method for mounting the EFI partition, you'll find that it's not selectable as
a Startup Disk.  Or, even if you can, selecting it and restarting makes no
difference.

So, what's a guy to do?  Turns out you can hold the ``Control`` key down
**prior** to clicking onto a volume/device in the Startup Manager to set that
volume as the boot default!  So, I held down ``Control``, clicked ``EFI Boot``
and that's that.

This worked for me on my 2011-era Mac, now running OS X 10.10, but since this
option isn't officially documented anywhere that I can see, it could go away
at any time.  Try it and add a comment below with your results.

Thanks to `Macworld
<http://www.macworld.com/article/1135944/startupboot.html>`_ for the solution!

As a side note, it's interesting to see the UI for Mac OS has barely changed
in decades for selecting a Startup Disk.
