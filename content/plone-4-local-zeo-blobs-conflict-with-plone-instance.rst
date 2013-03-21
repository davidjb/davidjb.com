Plone 4: Local Zeo blobs conflict with Plone instance
#####################################################
:date: 2010-07-06 16:04
:author: davidjb
:category: Plone 
:tags: blob, conflict, database, db, files, plone, plone 4, problem, upgrade, zeo
:slug: plone-4-local-zeo-blobs-conflict-with-plone-instance

As the title suggests, there's a conflict between a Zeo database
instance being run together with a Plone 4/Zope instance, and them
trying to share the same blob storage folder.  But, this only happens if
you misunderstand or incorrectly set the option of  *shared-blob = off*,
and *blob-storage* to be the same location as for Zeo in your buildout. 
If that previous set of (seemingly jumbled) thoughts doesn't make any
sense to you, then move along, nothing to see here.

By default, at the time of writing, blob support within Zeo runs with
the *bushy*\ layout, and creates this format by default when starting up
for the first time. Plone 4, however, when trying to stream blobs from
your Zeo database, uses a customised *zeocache* blob layout. See where
I'm going with this? You try and inadvertently use these aspects
together and you've got a conflict.

If you're having this problem, then you'll get weird errors concerning
the *layout* of your blobs. Starting the Zope instance before the Zeo
server results in Zope setting the **.layout** file for the blob storage
to *zeocache*. Once your Zope instance errors out and you realise that
your Zeo instance isn't running, you'll inevitably try and start Zeo up.
When you do, you get an error about the layout type not existing:

.. code:: pytb

    /home/david/buildout/parts/zeo/bin/runzeo
    Traceback (most recent call last):
      ...
      File "/home/david/buildout/eggs/ZODB3-3.9.5-py2.6-linux-i686.egg/ZODB/blob.py", line 714, in __init__
        self._blob_init(base_directory, layout)
      File "/home/david/buildout/eggs/ZODB3-3.9.5-py2.6-linux-i686.egg/ZODB/blob.py", line 600, in _blob_init
        self.fshelper = FilesystemHelper(blob_dir, layout)
      File "/home/david/buildout/eggs/ZODB3-3.9.5-py2.6-linux-i686.egg/ZODB/blob.py", line 339, in __init__
        self.layout = LAYOUTS[layout_name]
    KeyError: 'zeocache'

Now, if you try to fix this by dumping your now-existing blob storage
folder (a method mentioned to work elsewhere on the web) and starting
your Zeo server first, you'll still get problems. The blob storage gets
created correctly with the 'bushy' layout by Zeo, but trying to start
the Zope instance fails, because Zeo's created its storage accordingly
in the same spot. This is part of the error:

.. code:: pytb

    Traceback (most recent call last):
      ...
      File "/home/david/buildout/eggs/ZODB3-3.9.5-py2.6-linux-i686.egg/ZODB/blob.py", line 362, in create
        (self.layout_name, self.base_dir, layout))
    ValueError: Directory layout `zeocache` selected for blob directory /home/david/buildout/var/blobstorage/, but marker found for layout `bushy`

The two ways of solving this are to:

#. Change the *shared-blob* option to be **on**. Both Zeo and Zope will
   exist in harmony again, both using the *bushy* layout.
#. Changing the *blob-storage* location for either the Zeo server or the
   Zope instance. This will result in two separate folders and likely
   duplicate files and HDD wastage, but hey, it'll work, right? This is
   probably a useful option for testing.

The *zeocache* layout is new with Plone 4 (aka, I haven't seen it before
so it probably is), so watch out for this when upgrading.

Stay tuned for more in this series of Plone 4 upgrade notes.
