Plone/Zope: Truncating a Data.fs back to a certain date/time
############################################################
:date: 2010-07-20 13:39
:author: davidjb
:category: Plone 
:tags: data.fs, database, date, fix, linux, plone, python, time, truncate, zeo, zodb, zodb3, zope
:slug: plonezope-truncating-a-data-fs-back-to-a-certain-datetime

Okay. So, anyone out here who's listening -- particularly those
overly-enthusiastic users -- don't try to recursively ``wget`` your
Plone site (or other CMS, for that matter) whilst you're logged in with
an account that can make edits. It **will** lead to a very bad situation
where your site administrator and technical team need to step in and fix
your mistakes. For the uninitiated, a loose recursive wget (when logged
in with some degree of Edit rights) will hit every link that's on your
pages, and I mean in the (X)HTML *source*. For a Plone site, this means
hitting every "Edit" link, every "Revert to this version" link, and
every other link that might be dangerous when clicked randomly. Oh, and
if the account you've got has admin rights, well, it's not getting any
better and requires the Data.fs to be undone back to before it happened.
Here's how to do that easily.

So enough of the backstory. How to fix a suitably bollocks'd Data.fs?
Well, the easy answer is to recover from a backup. Of course you've got
plenty of those, right? No? Oh dear. Never to stress, you can use your
existing Data.fs file and strip away any number of transactions, to
bring your file back to any date, time, or transaction you'd like.

#. Realise you'll be losing everything from now back until then, so take
   a copy of data off your Plone site, back up your Data.fs (twice, if
   need be), and make it crystal clear to your users changes are going
   bye-by.
#. Figure out when you want to go back to.  If you want a particular
   transaction, consider checking your Zope Undo log to locate the
   specific date/time of a given transaction.  Otherwise, figure out the
   date and time.  Then, convert that date and time to UTC as that what
   date/times are in the Data.fs.  In Queensland, Australia, we're +10
   hours.
#. Shut down ZEO if it's still running.
#. Edit ``parts/zope2/lib/python/ZODB/FileStorage/fsdump.py``, and add
   this to allow you to run this file:

   .. code:: python

        if __name__ == "__main__":
            main()

#. Get your PYTHONPATH sorted for running this file.  Consider
   ``./bin/instance1`` shell, if you've got a Plone instance, or using
   zopepy.  Manually update it if necessary.
#. Run the the ``fsdump.py`` script thusly, substituting the date for
   yours (or a date/time):

   .. code:: bash

        ./bin/python parts/zope2/lib/python/ZODB/FileStorage/fsdump.py var/filestorage/Data.fs | grep 2010-07-12

   This will tell you exactly the offset you need to truncate the
   Data.fs file.

#. Take that offset amount and truncate your Data.fs file, inserting the
   number after "seek=":

   .. code:: bash

        dd if=/dev/zero of=var/filestorage/Data.fs seek=199340531 bs=1 count=0

#. Restart your ZEO service and re-connect to it from your Plone/Zope
   instance.  Your database should be back to the date and time you
   specified.  If it's close, but not quite right, check your times and
   that they're UTC.
#. Get some backups and politely ask your users to think twice about any
   such consequences next time.

And we're done!
