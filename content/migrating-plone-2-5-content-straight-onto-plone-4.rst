Migrating Plone 2.5 content straight onto Plone 4
#################################################
:date: 2011-01-14 15:07
:author: davidjb
:category: Plone 
:tags: content, migration, plone, settings, site
:slug: migrating-plone-2-5-content-straight-onto-plone-4

It's my very last Plone 2.5 site and I'm very happy to see the back of
it.  Using the joy that is **quintagroup.transmogrifier**, I was able
to, without much manual effort, migrate my content from a Plone 2.5 site
(constructed with instancemanager, of all things!) straight into a shiny
new Plone 4 site on Buildout.

My only key need was to port the content and structure, and I was happy
to make big allowances for the sake of certain content and time.  So, my
thoughts here mightn't (probably won't!) suit everyone.My requirements
and allowances were these:

-  Content and structure only needed to be migrated.  Plone settings,
   theme, user accounts, and everything else would either come from my
   newly-created Plone 4 theme or be manually re-added.
-  There were/are only a handful of users on the site.
-  My Plone 2.5 site used a lot of custom content types (IronicWiki,
   Wicked, Quills, PloneSoftwareCentre, Poi and more).

   -  I want to avoid ever going through migrating custom 'document'
      types again.  Thankfully, the 'wiki'-based content types translate
      easily to pure Plone documents.
   -  I was happy to jettison content in PSC, Poi, and Quills
      (Weblogs).  This is a big issue but it wasn't worth my time since
      the content was already 5+ years out of date and never used.

-  Default folder view selections don't appear to migrate.  I was able
   to manually fix things up.

That out of the way, here's my process.

For Plone 2.5
~~~~~~~~~~~~~

#. Follow Step 1 of `QuintaGroup's instructions`_ for migrating a
   Plone 2.1 site to Plone 3.  I had a Plone 2.5 site and this worked
   well.  Essentially, you want to use ZopeSkel (paster) to create
   yourself a Plone 2.5 buildout and then checkout the relevant packages
   (as per the instructions).  I created mine on my local Ubuntu machine
   for my sanity as the old server the site was running on was ages out
   of date.
#. Figure out what you need to actually get the Plone 2.5 instance to
   start up.  Now, my site had a huge amount of 3rd party packages that
   caused me grief, and I had to add these into the buildout before the
   instance would even start successfully.  In my case, it was a matter
   of copying out the old product web links from my instancemanager
   script and putting them in the **productdistros** section of my Plone
   2.5 buildout.

   -  Note that if your Plone instance was entirely manually managed,
      then I'm guess you either on a hunt, or you could try copying the
      files into your relevant directory.
   -  I also had a number of SVN-based products too so I employed my
      fried, mr.developer, to check them out from the right SVN location
      to the buildout src directory.

#. Once you've got your instance started (in the foreground), then you
   should be able to access
   http://localhost:8080/<your\_site\_name>/@@pipeline-config which is
   the configuration for Transmogrifier.

   #. You can modify your configuration to suit you.  There's a little
      learning involved here, but there are a good number of
      Transmogrifier resources around.
   #. My configuration looks like this: `transmogrifier-export.txt`_,
      where I explicitly ignore a whole bunch of content types (read:
      problematic for export/import), and export my content out to a
      temporary directory
   #. Make changes to the export configuration and save the result.

#. Under the ZMI, head into portal\_setup and click the 'Properties'
   tab.  Change the active site configuration to be 'Transmogrifier' and
   save this.
#. Click the 'Export' tab at the top, and then export the 'Content' step
   you see listed.  Watch your console output for progress and anything
   that might be a problem.
#. If successful, then you'll get presented with a generic setup .tar.gz
   to download.  Save this somewhere useful; you'll need it shortly.  If
   you were like me and exported to a directory, then you'll get an
   'empty' .tar.gz download and your content will be in the directory
   you specified.


Manually modify content before import
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The reason I outputted to a directory so was I could hack a few things
around in my content. Transmogrifier is powerful, but a bit complicated.
I couldn't find out how to rename a field to another in the pipeline (eg
IronicWiki content use the "body" field rather than "text" as do normal
Document content), and likewise I couldn't successfully translate
content type names.

So, find and replace it is. WickedDocs and IronicWiki are essentially
modern Plone Documents in disguise (as wiki markup is the same), so we
can just translate them over. In addition, I go ahead and rename
anything that's called "index\_html" as this would otherwise be
displayed as the actual page on a given folder automagically (and not
through being selected in the Display drop down menu):

.. code:: bash

    cd /path/to/our/temp/directory
    grep -lr -e 'WickedDoc' * | xargs sed -i 's/WickedDoc/Document/g'
    grep -lr -e 'IronicWiki' * | xargs sed -i 's/name=\"body\"/name=\"text\"/g'
    grep -lr -e 'IronicWiki' * | xargs sed -i 's/IronicWiki/Document/g'
    find . -name index_html | xargs rename -v 's/index_html/main_page/g'
    grep -lr -e 'index_html' * | xargs sed -i 's/index_html/main_page/g'
    grep -lr -e 'copy_of_main_page' * | xargs sed -i 's/copy_of_main_page/copy_of_index_html/g'


Once done with this, I copied the 'structure' directory (inside the temp
directory) into the .tar.gz you have from earlier, ready for upload to
the new site.

For Plone 4
~~~~~~~~~~~

#. Set up your Plone 4 like normal.  You should (are?) using Buildout,
   so follow the instructions `here`_, again from QuintaGroup, to
   install the same quintagroup.transmogrifier product into your Plone 4
   instance (eg just add it into your eggs and zcml for your instance).
#. Create a Plone site if you haven't already.
#. Like before, you can use the configuration page at
   http://localhost:8080/<your\_site\_name>/@@pipeline-config , except
   this time, configure the import options.  My config looks like this:
   `transmogrifier-import.txt`_ - pretty much the same as the default.
#. When you're ready, head into the ZMI and into 'portal\_setup', this
   time clicking on the 'Import' tab.
#. Browse down to the very bottom of the page, and use the file field
   (hint: Browse button) to locate your .tar.gz file you've prepared.
#. Click 'Import uploaded tarball' and watch your console output for
   progress.

Cleaning up
~~~~~~~~~~~

This process wasn't without manual work, unfortunately.  But, it
certainly took care of 95% of the pain of copying content across! 
Here's an overview of the manual work I had to do:

-  Set default pages of folders.  This could have probably been carried
   out by a script but I didn't write one because I only had a 20
   folders to fix.  In Plone 2.5, I believe the default view was when
   you set a page to be called 'index\_html' (happy for corrections),
   but AFAIK, there weren't options to set a certain page as the view.
-  Set site settings.  This involved going through all control panels to
   pick and manually port settings, but because of so many changes from
   Plone 2.5 to 4, there's probably not an obvious migration path
   anyway.
-  Convert legacy portlets.  These settings do get copied across, but
   you'll need to go to the 'Manage portlets' link on your main homepage
   and click the 'Convert' button.  At time of writing (Plone 4.0.2)
   this migration is actually broken (ticket logged already!) but you
   can just as easily migrate manually -- look in the ZMI properties at
   the site root for your portlet listings.
-  Fix some workflow states.  My old site used a non-default workflow,
   so workflow states needed correcting.  Thankfully, I was able to push
   most content around just using the Types control panel.

And the rest of the actions I did were simply boilerplate for setting up
a Plone 4 site (theme installation, etc).

This isn't the most straightforward path, but it did work and get my
content across.  Hopefully moving to Plone 5 and above won't be too much
of a problem.

.. _QuintaGroup's instructions: http://projects.quintagroup.com/products/wiki/quintagroup.transmogrifier/plone2-3
.. _transmogrifier-export.txt: http://davidjb.com/wp-content/uploads/2011/01/transmogrifier-export.txt
.. _here: http://projects.quintagroup.com/products/wiki/quintagroup.transmogrifier/plone3-4#Installationonbuildout
.. _transmogrifier-import.txt: http://davidjb.com/wp-content/uploads/2011/01/transmogrifier-import.txt
