Virtualenv, Plone, and Ubuntu 9.04 Jaunty
#########################################
:date: 2009-06-12 12:35
:author: davidjb
:category: Plone 
:tags: 9.04, 9.10, jaunty, karmic, linux, plone, python, ubuntu, virtualenv, zope
:slug: virtualenv-plone-and-ubuntu-904-jaunty

What a complicated situation it is trying to use all of the
above-mentioned pieces of software together. In all seriousness,
Virtualenv is now appearing to be the best thing since sliced bread for
me to help out with making Plone/Zope usable under Jaunty.

By default, as everyone should know by now, a whole bunch of old Python
2.4 packages got removed from Jaunty, throwing us Plone developers into
peril.  Well, those of us who hadn't discovered the joys of virtualenv
yet, that is.

Here's how to convert an existing buildout folder over to Virtualenv
without too much hassle:

.. code:: bash

    sudo apt-get install python-virtualenv
    virtualenv -p /usr/bin/python2.4 .
    source ./bin/activate
    easy_install ipython
    easy_install --find-links http://www.pythonware.com/products/pil/ Imaging
    easy_install --find-links http://download.zope.org/distribution PILwoTK
    easy_install python-ldap
    ./bin/buildout

And that should handle the issues of, in order of command: installing
virtualenv, setting up our current folder, activating virtualenv,
installing useful/necessary python packages, and reworking everything
via buildout.

The instance of Plone/Zope can be started up with/without
\`\ **activate**\ \` being \`\ **source**\ \`'d, as virtualenv has now
got its own local python interpreter here.

Cheers to Athena Geek @
http://athenageek.wordpress.com/2009/05/22/virtualenv-in-plone/ for the
details to get me started.

**EDIT:** You might need to install some of the following packages to
make all the imaging (and rest of Plone) be happy:

.. code:: bash

    sudo apt-get install python2.4-dev libtk-img-dev libfreeimage-dev libjpeg62-dev libfreetype6-dev libtk-img-dev tcl8.5-dev tk8.5-dev lynx poppler-utils xpdf wv xlhtml ppthtml

**EDIT2:** If you get weird messages about "Undefined symbol:
PyUnicodeUCS2\_\*" then you should probably wipe your virtualenv clean
and go again. Essentially, dump your lib, include, and content of your
eggs folder, and re-do your virtualenv. If pain persists, see your
Google.

**EDIT3:** This also works on Karmic (9.10)! :)
