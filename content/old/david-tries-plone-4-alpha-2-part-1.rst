David tries Plone 4.0a2 (Part 1)
################################
:date: 2009-12-08 15:48
:author: davidjb
:category: Plone 
:tags: alpha, buildout, install, plone, plone 4, testing, zope
:slug: david-tries-plone-4-alpha-2-part-1

Plone 4 is approaching!  Excellent!  Lots of new features to play around
with and plenty more things to have to fix with the upgrade.  I've been
keeping tabs on the change log of updates and it's looking really good. 
Lots of little, but significant, changes are afoot.  Now, how about
actually installing the Alpha 2 version of Plone 4 to see it for real? 
Let's do it!

My steps are not going to work on your computer.  I don't think you'll
be able to follow my words/commands exactly, but here goes anyway about
my experience so far.  The buildout might/might not work on Windows/Mac;
I'm on Linux and that's that FYI.

-  I grabbed the buildout from
   https://svn.plone.org/svn/plone/buildouts/plone-coredev/branches/
   and beat it over the head with a stick.  I downloaded the Plone 4.0a2
   versions.cfg from http://dist.plone.org/release/4.0a2/versions.cfg
   over the top of the one provided and made the buildout.cfg provided
   only extend off versions.cfg.  You'll also need to strip back the
   'parts' section of the buildout (eg no 'test' sections since I don't
   really need to know things aren't 100% right yet ;-) )
-  Set up your virtualenv in your given folder, making sure you use
   **Python 2.6**.  It's not marked in huge text and bold for you as
   much as it is for me.  If you see this:

   .. code:: pytb

       While:
       Installing.
       Getting section instance1.
       Initializing section instance1.
       Loading zc.buildout recipe entry plone.recipe.zope2instance >=2.0:default.
       An internal error occured due to a bug in either zc.buildout or in a
       recipe being used:
       )[1 if IS_WIN else 0]
       ^
       SyntaxError: invalid syntax

   then you need to stop using Python 2.4 and start using 2.6, okay?

-  Make sure you've got the Python 2.6 development libraries installed
   on your machine.  Expect pain from Zope 2.12.1 (etc) if you don't. 
   If you see this:

   .. code:: pytb

       include/ExtensionClass/ExtensionClass.h:83:20: error: Python.h: No such file or directory
       ....[lots of nasty errors]...
       error: Setup script exited with error: command 'gcc' failed with exit status 1
       An error occured when trying to install Zope2 2.12.1.Look above this message for any errors thatwere output by easy_install.
       While:
       Installing.
       Getting section instance.
       Initializing section instance.
       Installing recipe plone.recipe.zope2instance.
       Getting distribution for 'Zope2==2.12.1'.
       Error: Couldn't install: Zope2 2.12.1

   then go and run this, then run Buildout again:

   .. code:: bash

       sudo apt-get install python-dev

-  Sort your PIL out.  See here: `this post`_ for how to handle it.  I'm
   sure there are other, possibly easier ways, but the two
   'easy\_install' lines in that post work.
-  Run your buildout and hope there's no other problems I haven't
   covered.  If you get stuck, go say hi to Google and I'll see you back
   here after class.  Other than that, wait a very long amount of time
   whilst the buildout completes, with or without fingers crossed.  Your
   choice.  My buildout's going well so far, though.

And we're done buildout-ing!  Success!

See my `next post`_ for my thoughts of this new version so far.

.. _this post: http://davidjb.com/blog/2009/06/virtualenv-plone-and-ubuntu-904-jaunty
.. _next post: http://davidjb.com/blog/2009/12/david-tries-plone-4-0a2-part-2
