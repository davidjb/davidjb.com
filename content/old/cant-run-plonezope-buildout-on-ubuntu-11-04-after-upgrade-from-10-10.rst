Can't run Plone/Zope buildout on Ubuntu 11.04 after upgrade from 10.10
######################################################################
:date: 2011-05-11 09:33
:author: davidjb
:category: IT, Linux, Software
:tags: buildout, plone, python, zope
:slug: cant-run-plonezope-buildout-on-ubuntu-11-04-after-upgrade-from-10-10

After upgrading from Ubuntu 10.10 (Maverick Meerkat) to Ubuntu 11.04
(Natty Narwhal), you'll probably find that if you're running a Plone 4
buildout where you need to upgrade the Plone version, that compilation
of Zope will fail. The output will look something like this:

.. code:: pytb

    Getting distribution for 'Zope2==2.12.17'.
    In file included from src/AccessControl/cAccessControl.c:51:0:
    include/ExtensionClass/ExtensionClass.h:83:20: fatal error: Python.h: No such file or directory
    compilation terminated.
    error: Setup script exited with error: command 'gcc' failed with exit status 1
    An error occured when trying to install Zope2 2.12.17. Look above this message for any errors that were output by easy_install.

The reason for this is that the default Python version in Ubuntu 11.04
is now Python 2.7, rather than 2.6 as was previously the case. The
message here is telling us our Python development libraries/headers
aren't available, so do this:

.. code:: bash

    sudo apt-get install python2.6-dev

and re-run your buildout. Make sure too that if you're using Plone 4
that you're using Python 2.6, as newer versions like 2.7 aren't
supported (yet).
