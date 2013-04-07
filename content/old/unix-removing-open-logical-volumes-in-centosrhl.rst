Unix: Removing Open Logical Volumes in Centos/RHL
#################################################
:date: 2009-05-13 09:19
:author: davidjb
:category: Linux
:tags: centos, close, logical, red hat, remove, unix, volume
:slug: unix-removing-open-logical-volumes-in-centosrhl

Because I still haven't remembered to set myself up with a
limited-access account for blogging on my new site, I'm back here again.
(EDIT: Migrated from old site)

This time is a lot of fun and games with removing an "open" logical
volume from within a CentOS environment. The dom0 machine has a set of
logical volumes in a volume group for each of the VMs and one of them
went and failed dismally, and after its xen destruction (xm destory foo)
its LV was left with it being "open".

It's not exactly easy to see how/why this would be the case and every
command (lsof, fuser, mount, etc) told me that the LV wasn't in use. But
still, lvremove, lvchange, and dmsetup commands failed.

But, I've solved my problem! Hopefully yours too.. read on through the
commands:

.. code:: bash

    # lvchange -an /dev/vmsvg1/foo
    LV vmsvg1/foo in use: not deactivating
    # dmsetup info -c vmsvg1-foo
    Name             Maj Min Stat Open Targ Event  UUID
    vmsvg1-foo    253  65 L--w    1    1      2  XXX
    # dmsetup remove -force vmsvg1-foo
    device-mapper: remove ioctl failed: Device or resource busy
    # lvchange -an /dev/vmsvg1/foo
    /dev/vmsvg1/foo: read failed after 0 of 4096 at 0: Input/output error
    /dev/mapper/vmsvg1-foop1: read failed after 0 of 2048 at 0: Input/output error
    # dmsetup remove -force vmsvg1-foop1
    # dmsetup remove -force vmsvg1-foo
    # lvs vmsvg1
    foo    vmsvg1 -wi---   4.00G   (it's closed!!)
    # lvchange -an /dev/vmsvg1/foo
    # lvremove /dev/vmsvg1/foo
    Logical volume "foo" successfully removed

So, after all that, it looks like there's some stupid 'p1' references in
/dev/mapper/ . Nfi why, but removing it (albeit by force with dmsetup)
solved the problem.
