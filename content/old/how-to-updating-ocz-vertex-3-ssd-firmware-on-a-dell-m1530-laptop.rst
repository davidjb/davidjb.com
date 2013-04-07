How to: Updating OCZ Vertex 3 SSD Firmware (on a Dell M1530 laptop)
###################################################################
:date: 2011-05-21 23:45
:author: davidjb
:category: Hardware
:tags: boot, drive, firmware, guide, linux, live, ssd, update, usb
:slug: how-to-updating-ocz-vertex-3-ssd-firmware-on-a-dell-m1530-laptop


.. note:: **Update 3:** This guide is effectively now entirely outdated
    with regards to the available tools.  I've gone back to simply using
    a Windows boot disk to handle the firmware upgrades, although they've
    gotten less frequent as of late. 

I've just shelled out a good chunk of money in buying an OCZ Vertex 3
240GB solid state drive (SSD) and it's amazingly quick. So amazingly
quick that I thought I may just have fallen into a coma when I had to
temporarily switch back to my old mechanical hard drive and boot from it
again. And this is only using the Vertex 3 on a SATA II interface - not
even the SATA III it's designed for. I actually just bought a new laptop
with the intention (at least one of ;)) of being able to utilise the
drive's full potential on SATA III, but I digress.

After having only had this drive for a week, I've noticed that there are
firmware upgrades available from the OCZ website, and the Vertex 3's
firmware stands at 2.06 at time of writing. Now, you can upgrade this
firmware (and upgrading did **not** erase my drive!) but it's not the
easiest if you're like me and only have a laptop with the SSD as your
only drive. Thankfully, a bit of trial and error on my part got this
licked. Here's a guide to how I did it.

Now, as the OCZ site mentions, you can't upgrade a disk that you've
booted off. I've also learned that you need to have your SSD connected
in via a dedicated SATA controller (NOT a USB-to-SATA converter or any
such thing) and in my case of my M1530 laptop, is the internal drive
bay. This means we need to be booting off a USB stick or optical disc -
something Windows essentially won't do easily. Thankfully, this is
something that Linux shines at. And the good news here is that OCZ have
a Linux-based updater tool available. Hurray!

Here's what you can do. Warning: your mileage **will** likely vary for
you if using a different laptop, different model version, different
firmware to A12, different SSD firmware, etc, so be very careful
following my words verbatim.

#. Download and install a Linux distribution to a USB stick or burn an
   optical disc.  In my case, I chose Ubuntu 11.04, because that's what
   I'm comfortable with.
#. Head to the OCZ forums and download the linked `Linux OCZ Firmware
   Update Tool`_. At time of writing, the version is 1.15.  Put the zip
   or tar file close to hand (eg on the USB stick is a good idea).
#. Shut down your computer.
#. Potentially optional step:  change the SATA mode on your drive to
   'ATA' (away from 'AHCI') within the BIOS.  As far as I had read, this
   is necessary.  That said,  I haven't tried it without doing this as
   of yet.  When changed, shut down your computer.
#. Disconnect all power from the computer - in the case of my laptop,
   this was the AC and the battery.  Wait for a minute before
   reconnecting.  Apparently this is enough time for the AHCI security
   'freeze' to be cleared from the SSD.
#. Connect power again and boot from your USB stick.
#. When your Linux distro is loaded, inspect your SSD's parameters with
   this command, replacing /dev/sda with your drive's device::

       sudo hdparm -I /dev/sda

#. If all is well, then you should see 'not frozen' and 'not locked' in
   the output, near the very bottom.  If you only see 'frozen' (for
   instance) as one of the lines, then your device needs to be unfrozen
   before continuing

   #. In my case, I had to turn off the swap partition on the drive
      (done easily with gparted) and
   #. I had to suspend and resume my computer whilst on running off the
      USB stick.  This last point clinched it for me and the security
      freeze was lifted.

#. Once you're ready, make sure your computer is connected to the
   Internet as the firmware updater downloads the latest version from
   OCZ on the fly.
#. Locate your zip/tar of the firmware tool and extract it somewhere
   convenient.  For argument's sake, I've put mine in my home directory.
#. Run the appropriate command from the following to update the firmware
   (linux32 is for if you are presently booted into a 32 bit OS and
   linux64 is for 64 bit; replacing /dev/sda with your drive's device)::

       sudo ~/fwupd\_v115/linux32/fwupd -log /dev/sda
       sudo ~/fwupd\_v115/linux64/fwupd -log /dev/sda

#. You should be greeted with a message of success, if it all worked. If
   it didn't, then check to make sure your drive isn't reported as
   locked or frozen - this is what it was for me 99% of the time.

So that's about it. This guide and how-to is mostly posted for my own
information for later, but hopefully it might help someone else. Like
always, make sure you've backed up your data before beginning anything
like this.

.. _this thread: http://www.ocztechnologyforum.com/forum/showthread.php?89670-Bootable-Tools-for-OCZ-Vertex2-3-Agility2-3-Solid3-Revo-and-Ibis-SSD-s
.. _here: http://www.ocztechnologyforum.com/staff/ryderocz/sf/fwupd_v2.10.tar
.. _Linux OCZ Firmware Update Tool: http://www.ocztechnologyforum.com/forum/showthread.php?82289-OCZ-SandForce-Linux-based-firmware-update-tool
