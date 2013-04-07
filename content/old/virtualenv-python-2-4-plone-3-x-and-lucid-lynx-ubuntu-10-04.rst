Virtualenv, Python 2.4, Plone 3.x and Lucid Lynx (Ubuntu 10.04)
###############################################################
:date: 2010-05-12 14:47
:author: davidjb
:category: Plone 
:tags: 10.04, how-to, install, installation, lucid, plone, python, virtualenv
:slug: virtualenv-python-2-4-plone-3-x-and-lucid-lynx-ubuntu-10-04

These titles of my posts just keep getting longer and longer.  For those
of you paying close attention (I know who you are), this is the next in
my series of getting the above-mentioned tools working together. 
Previously, it was Centos 5.x, Jaunty (9.04), Karmic (9.10) and now
Lucid (10.04).  Only subtly different, each of this distributions has
pretty much called for its own post on the matter of getting a working
Plone 3.x / Python 2.4 virtualenv installation going.  So, here goes
this time around.

Install Python 2.4 first
------------------------

If you've not done so already, you need to install Python 2.4.  Lucid
now no longer comes with the packages for Python 2.4 (at all; so not
even python2.4, python2.4-dev) in its repositories, so you need to wind
back the clock and get the Karmic packages.  Don't worry, everything
seems to work okay.  `Read my post about this`_ and come back here.

Prerequisites
-------------

Ready to roll? You might want to make sure that you've got python2.4
available (eg run ``python2.4``) and that you can ``import  profile``.
If not, go back to the other post and read carefully (or complain loudly
:)). You should also check the following:

-  Got easy\_install-2.4?  Try and type it in your terminal.  No good? 
   Then do this:

   .. code:: bash

       wget http://pypi.python.org/packages/2.4/s/setuptools/setuptools-0.6c11-py2.4.egg
       sudo sh setuptools-0.6c11-py2.4.egg
       rm -f setuptools-0.6c11-py2.4.egg
       sudo easy_install-2.4 -U setuptools
       sudo easy_install-2.4 virtualenv

-  If you've got the python-virtualenv Ubuntu package installed.  If you
   do, have a serious think about uninstalling it and getting the one
   for Python2.4 via easy\_install-2.4. Your warranty ends here if you
   continue with the Ubunutu-installed virtualenv.
-  If you need to install system-level packages. Even if you've run this
   before on an old Karmic (or older install), do it again as you've
   likely lost packages in the upgrade.

   .. code:: bash 

       sudo apt-get install libtk-img-dev libfreeimage-dev libjpeg62-dev libfreetype6-dev libtk-img-dev tcl8.5-dev tk8.5-dev lynx poppler-utils xpdf wv xlhtml ppthtml

Make your virtualenv happen
---------------------------

Now that's sorted, convert an existing buildout folder over to
Virtualenv:

.. code:: bash

    virtualenv -p /usr/bin/python2.4 .
    source ./bin/activate
    python bootstrap.py -v1.4.3
    easy_install ipython
    easy_install --find-links http://www.pythonware.com/products/pil/ Imaging
    easy_install --find-links http://download.zope.org/distribution PILwoTK
    easy_install python-ldap
    ./bin/buildout

And that handles setting up and activating virtualenv, **making sure we
bootstrap with version 1.4.3 of buildout**, installing useful/necessary
python packages, and reworking everything via buildout. As highlighted
with the **bold** text, you must make sure you add the ``-v1.4.3``
option to running bootstrap.py.

Conclusion
----------

So, that wraps things up. You should now have a fully functional
virtualenv, just like you did back in the good old days (or, if you're
new to this game, a fresh new install). Now, if you're a Plonista, you
can fire up your instance and it should start just fine.

.. _Read my post about this: http://davidjb.com/blog/2010/05/installing-python-2-4-on-ubuntu-10-04-lucid-lynx
