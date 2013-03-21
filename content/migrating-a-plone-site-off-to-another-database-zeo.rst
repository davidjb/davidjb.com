Migrating a Plone site off to another database (Zeo)
####################################################
:date: 2009-09-30 12:25
:author: davidjb
:category: Plone 
:tags: database, export, import, migration, plone, site, zeo, zodb
:slug: migrating-a-plone-site-off-to-another-database-zeo

Another of the interesting things in my professional life has been
migrating a Plone site from one database (where it lived as a dev site,
along with many others) onto a nice, clean database of its own.  Now,
yes, I'm aware that the export/import feature of Zope **isn't** supposed to
be used for migrating content or sites.  I am also aware, however,
through personal experience, that things have always been fine because
I'm using the same eggs and essentially the same installations
everywhere, thanks to buildout.

So, the process goes as follows, with the above-mentioned points
considered already:

#. Head to the root of your ZMI and export your given Plone site  as
   ZEXP
#. Shut down your instance (or do what you will with your old site and
   installation)
#. Copy the ZEXP file into the 'import' folder of your new Zope instance
#. Start your new instance, with your new empty database
#. Log in to the root of the ZMI
#. Add a new Plone site and call it anything you want (eg 'foo').  I'll
   explain why shortly.
#. Delete your 'foo' Plone site.
#. Import your existing Plone site and be happy because it's now arrived
   safe and sound.

Note
~~~~

The reason I highlight adding a new Plone site a point 6 is because if
originally, you were like me and imported your site first to a bare Zope
install, you'll get errors **everywhere** in your site.  They'll look
like "AttributeError: getGroups" or possibly something more obscure (if
possible!) and everything will fall over and die.

Now, by creating a new Plone site first 'massages' the root of Zope, and
then your site should be fine.  Among other things, adding a site
changes the acl\_users of the ZMI (seeing an abnormal acl\_users is what
led me to the solution).  At a guess, given its type, this acl\_users
change probably has something to do with the error above.
