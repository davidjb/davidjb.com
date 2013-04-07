Wget a Plone site (and make it actually work)
#############################################
:date: 2010-02-25 15:01
:author: davidjb
:category: Plon 
:tags: cd, content, download, dvd, export, media, offline, plone, site, static, wget
:slug: wget-a-plone-site-and-make-it-actually-work

There's a lot of different resources and posts on the
web about how to export a Plone site to static html content, but no
methodology would actually solve all of my problems. Now, Plone is
inherently a complicated beast, given just how much it does, and that's
definitely putting it lightly. But here goes at my attempt to provide an
actual, workable solution.  Word for the wise though, this is for more
than just your front-end administrator to handle.  Also, instructions
are designed for Ubuntu 9.10.  Mileage may/will vary on other distros or
OSes.

Requirements
~~~~~~~~~~~~

-  Needs to get all pages, including default views of folders, correctly
-  Needs to rewrite all links to be relative, because I want to run the
   site locally on CD/DVD (or move it anywhere)
-  Should get all the CSS from the site, and images from the CSS
-  Doesn't have to be in 1 command (relaxed to make life easy ;-) )

How to
~~~~~~

Issues I've had with other methods (specifically, wget options) either
don't get the right pages, manage to ignore default folder views, or
other random problems.  Here's my take on the situation -- it's not a
one-click solution, but it worked for me:

#. Go into your site and change all portal\_css entries' Render Type to
   'Link'.  This solves issues with wget and @import for CSS.
#. Make invisible any actions in portal\_actions that you don't want
   saved.  For example, "Register" and "Contact" might want to be hidden
   as they won't be useful on a static site.
#. When ready, run the following script on your site (thanks to
   `kiilerex`_ for the wget command): 
   https://github.com/jcu-eresearch/static-plone-wget
#. Looking inside the bash script, you'll see uses wget to download the
   site, then gets a list of images referenced within the CSS files, and
   downloads them accordingly to the location where the CSS file(s)
   are.  Then, it corrects your CSS files to have relative URLs, rather
   than absolute as does Plone by default.
#. Your site should now be ready for distribution to any web location or
   distribution media!

Please let me know if there's any problems with the script. It's on GitHub
at https://github.com/jcu-eresearch/static-plone-wget so go crazy and
fork as you'd like.

.. _kiilerex: http://kiilerix.blogspot.com/2008/10/mirroring-plone-site.html
