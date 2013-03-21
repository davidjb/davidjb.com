plone.app.blob and Failed Migrations
####################################
:date: 2009-07-03 12:11
:author: davidjb
:category: Plone 
:tags: blob, fix, links, plone, problem, traceback
:slug: plone-app-blob-and-failed-migrations

Another fun-and-games style problem I've come across when using
plone.app.blob: sometimes migrations won't work when converting a
standard site's files over to blobs.

That's a pretty ambiguious description, but essentially, the error you
might see will have a semi-normal traceback to start, and then garbage
(contents of a file, presumably) - which, depending on the file size
might hurt your browser.  The last part of the (normal) traceback reads
thus:

.. code:: pytb

    File "/home/buildout/instance/eggs/plone.app.linkintegrity-1.0.11-py2.4.egg/ plone/app/linkintegrity/handlers.py", line 158, in referencedObjectRemoved raise LinkIntegrityNotificationException, obj LinkIntegrityNotificationException

Thankfully, this gives us an excellent pointer to a solution: disable
link integrity checking on your site prior to migrating.

The fix/workaround
~~~~~~~~~~~~~~~~~~

Head to the Plone Control Panel, and click onto Site.  Uncheck *Enable
link integrity checks*\ and then run your blob migration.  When you're
done, you can return your site to normal.Or not.  Your choice.  Doens't
seem like there's any harm with turning it back on once everything's
happy; just something to watch out when migrating content.


