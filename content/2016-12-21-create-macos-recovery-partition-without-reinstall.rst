Creating a macOS Recovery Partition without reinstalling OSX or re-running your installer
#########################################################################################

:category: Tech
:tags: mac, macOS, recovery

   **Note that this process worked for me on macOS Sierra (10.12).  I give no
   warranties that this will work for you so backup first.**

Restoring from a Time Machine backup - at least for me - won't furnish you
with a Recovery partition.  This is bad news because the only *official* way
of getting a recovery partition is to reinstall macOS.  This seems a little
counter-intuitive because isn't the point of backing up your computer so you
**don't** have to reinstall your OS?  Anyway, let's get to creating your
recovery partition without a reinstall or without 3rd party tools.  It's
easier than you think!

Background
==========

As you probably already know, macOS won't help create a recovery partition for
you and your OS will complain in these various ways:

* iCloud Find my Mac can't be enabled
* FileVault (disk encryption) can't be enabled

There's a *lot* of info on the web about how to potentially resolve this,
along with a number of 3rd party tools -- and none of them worked for me.  The
first one that was suggested was Carbon Copy Cloner and this won't work
because all it does it clone a Recovery HD, which means you actually need a
partition to start with.  I was also under the impression that would help you
*create* one as well, but this isn't possible on your boot disk.  Finally,
even when trying CCC from another Mac (and pointing it at my Macbook in Target
Disk Mode), it wouldn't work either -- though I can't recall the specific
reason.  So CCC is out.

Next, there's the suggestion of `Recovery Partition Creator 4.x
<http://musings.silvertooth.us/downloads-2/>`_ from Christopher Silvertooth.
This AppleScript-based tool looks like it used to worked back in the day (10.9
era) but it fails on Sierra; getting part way through and hanging.  So, this
is out too.  The script is saved as read-only so the raw source isn't
available but looking at what it does call (``dmtest
ensureRecoveryPartition``) lead me to a fully workable solution.

Solution
========

Firstly, you'll either need two Mac computers or the ability to boot your
computer off an external drive because the recovery partition creator
``dmtest`` can't write to your boot drive. The latter is easy if you've got a
spare cable for Target Disk Mode (hold down ``T`` as your computer starts up).
If so, connect it to the second Mac, and start the machine you want a Recovery
partition on in Target Disk Mode.

Otherwise, if you can boot a second disk (USB etc) connected to your target
computer, then just do so.  I had a spare Mac on hand so that was much faster
and easier than installing macOS onto a USB.

After your second Mac/macOS install can see the disk you want to install a
recovery partition onto (use either Disk Utility or ``diskutil list`` to check
its presence), do this:

.. raw:: html

   <script src="https://gist.github.com/davidjb/48204e370810407d6faeba48f1f414f1.js"></script>

Run this in a terminal after you have downloaded Sierra, or your OS, from the
App Store.  Adjust the ``TARGET`` and ``MACOS_INSTALLER`` paths accordingly.

Essentially, we download the latest (easily) accessible Recovery drive .dmg
with ``dmtest`` in it, the utility that's going to help us create the Recovery
partition, and then mount/use the .dmg inside the macOS installer to get the
work done.  Don't mind that the ``dmtest`` is from Lion; it works just fine
with Sierra.  This won't take long to run and the debugging messages in your
terminal tell you what percentage complete the process is.

Feel free to adapt this to your own paths or for different versions of macOS.

