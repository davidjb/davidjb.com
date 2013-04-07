Installing Python 2.4 on Ubuntu 10.04 Lucid Lynx
################################################
:date: 2010-05-04 12:00
:author: davidjb
:category: Linux
:tags: help guide, installation, linux, lucid, packages, python, ubuntu
:slug: installing-python-2-4-on-ubuntu-10-04-lucid-lynx

Whoops.  No one sent me the memo that Python
2.4 support was being removed entirely from the latest version of
Ubuntu, 10.04 Lucid Lynx.  To be fair, I was presented with the message
that 'these outdated packages will be removed' and in that list was
python2.4.  I made the unfortunate assumption that this just mean the
package was outdated (which it certainly is) and I'd have the ability to
install it again in Lucid.  There were a number of different packages on
the list and in order to save time, I let the updater remove them all. 
End result?  No more Python 2.4 on Lucid.Now, installing it back again
isn't too much of a hassle. You just need the old packages again from
the Jaunty repositories.

.. code:: bash

    wget http://mirror.aarnet.edu.au/pub/ubuntu/archive/pool/main/p/python2.4/python2.4-minimal_2.4.6-1ubuntu3.2.9.10.1_i386.deb -O python2.4-minimal.deb
    wget http://mirror.aarnet.edu.au/pub/ubuntu/archive/pool/main/p/python2.4/python2.4_2.4.6-1ubuntu3.2.9.10.1_i386.deb -O python2.4.deb
    wget http://mirror.aarnet.edu.au/pub/ubuntu/archive/pool/main/p/python2.4/python2.4-dev_2.4.6-1ubuntu3.2.9.10.1_i386.deb -O python2.4-dev.deb
    sudo dpkg -i python2.4-minimal.deb python2.4.deb python2.4-dev.deb
    rm python2.4-minimal.deb python2.4.deb python2.4-dev.deb

You can use your own mirror for the Ubuntu repository as required. I've
selected the AARNet mirror since it's about one of the quickest
(typically) for me here in Australia on an AARNet-connected educational
institution. Also, I'm using the i386 packages -- presumably this should
be fine with the amd64 counterparts as well.

**Note on Python 2.4 packages:** watch out for old Python 2.4
system-level packages you had installed (like python-virtualenv and
similar) previously on Jaunty or earlier.  These will now likely be
their Python 2.6 counterparts and installed differently than the old
ones.  So, if you try and ``easy_install`` something like virtualenv
again, expect that you'll have two apps with the same identical name (vs
virtualenv-2.4 previously) in your system path.

**Note on Virtualenv:** Exercise caution -- especially with the example
of virtualenv. Its latest incarnation has some deeper emotional issues
when mixing and matching the python-virtualenv package from the official
Lucid repos and Python2.4. I get the feeling `this bug`_ is related.

Python 2.4 Profiler Reinstallation
----------------------------------

If you find that some of your code (hello, Plone unit testing and
functional testing, I'm talking about you) won't run because you can't
"import profile" (``ImportError: No module named profile``), then you'll
need to get a hold of the python2.4-profiler package and install that.
Now, life is made more fun by the fact that python-profiler (Ubuntu's
new Python 2.6 version) explicitly conflicts with this package. Soooo...
do this to install it:

.. code:: bash

    sudo apt-get remove python-profiler
    wget http://mirror.aarnet.edu.au/pub/ubuntu/archive/pool/multiverse/p/python-profiler/python2.4-profiler_2.4.3-1ubuntu3_all.deb -O python2.4-profiler.deb
    sudo dpkg-deb -x python2.4-profiler.deb /
    rm python2.4-profiler.deb
    sudo apt-get install python-profiler

and hey presto, you've got your profile module installed for ye olde
Python 2.4.

.. _this bug: https://bugs.launchpad.net/ubuntu/+source/python-virtualenv/+bug/339904
