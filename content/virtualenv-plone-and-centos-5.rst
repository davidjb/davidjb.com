Virtualenv, Plone, and Centos 5.x
#################################
:date: 2009-07-09 13:25
:author: davidjb
:category: Plone
:tags: centos, easy_install, plone, python, rpm, virtualenv
:slug: virtualenv-plone-and-centos-5

**EDIT:** Watch out for python-ldap 2.3.10, the latest version at time
of writing. Seems like there's an issue with it and Centos 5.4. Forcing
python-ldap to be version 2.3.8 works, though. (easy\_install
python-ldap==2.3.8)

Previously, you might have read about setting up a Virtualenv on Ubuntu
Jaunty. Now, that was reasonably painless since python-virtualenv and
python-setuptools is in the Ubuntu repo. Whether it's my Centos servers
and their misguided repos or me just not being able to find such a
related rpm packages, Centos just needs little more love to get it to
the same setup. (**Note:** actually, there was a setuptools RPM that I
installed, but no idea why it didn't give me easy\_install...)

Here's what we're looking at for this time around.

-  Install the dependencies and various development libraries needed for
   PIL etc:

   .. code:: bash

        yum install gcc gdbm-devel readline-devel ncurses-devel zlib-devel bzip2-devel sqlite-devel db4-devel openssl-devel tk-devel bluez-libs-devel libjpeg-devel zlib-devel freetype-devel

-  Install setuptools and virtualenv:

   .. code:: bash

        wget http://pypi.python.org/packages/2.4/s/setuptools/setuptools-0.6c9-py2.4.egg#md5=260a2be2e5388d66bdaee06abec6342a
        sh setuptools-0.6c9-py2.4.egg
        rm -f setuptools-0.6c9-py2.4.egg
        easy_install-2.4 -U setuptools
        easy_install-2.4 virtualenv

-  Create a virtual environment and activate it:

   .. code:: bash

        virtualenv -p /usr/bin/python2.4 .
        source ./bin/activate

-  Easy install the dependencies of Plone. Not sure if they're needed
   for Centos, but it did all work nicely after doing this:

    .. code:: 

        easy_install --find-links http://www.pythonware.com/products/pil/ Imaging
        easy_install --find-links http://download.zope.org/distribution PILwoTK
        easy_install python-ldap
        easy_install lxml

Clear as mud? I thought so. Essentially the only difference is actually
getting the right development libraries and then getting setuptools
itself working correctly. As I mentioned, for whatever reason my
python-setuptools rpm doesn't have easy install. Maybe it's because it's
an old version? Who knows. This is an easy enough workaround.
