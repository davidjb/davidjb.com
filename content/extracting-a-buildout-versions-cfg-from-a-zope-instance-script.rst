Extracting a Buildout versions.cfg from a Zope instance script
##############################################################
:date: 2011-06-02 16:07
:author: davidjb
:category: Python
:tags: buildout, cat, cfg, eggs, grep, plone, sed, versions, zope
:slug: extracting-a-buildout-versions-cfg-from-a-zope-instance-script

Today, I needed to migrate some legacy Plone installs set up using
Buildout. If I were to simply move the buildout files and re-run
buildout, I'd end up with the latest versions of add-on products - and
since I'm using legacy versions of Plone 3, that'd almost certainly
break the system.  I do know about the Buildout extension
`buildout.dumppickedversions`_ (which does what its name suggests and
exports picked versions of eggs) but I can't re-run buildout to get this
extension for risk of updating existing products (what I'm trying to
avoid!).

The good news is that with just one line of bash in Linux (and a bunch
of helper commands :)), you can extract all your current egg versions
from a Zope instance script (eg bin/instance), like so, running the
command in your buildout directory:

.. code:: bash

    cat bin/instance1 | grep eggs | sed -r 's#.*eggs/(.*)-py2.[0-9].*#\1#g' | sed -r 's#-# = #g' | sed -r 's#_#-#g' | grep -E ' = [0-9\.]' | xargs -0 echo -e "[versions]\n" | sed -r 's#^\s+##g' > versions.cfg; cat versions.cfg

Copy the ``versions.cfg`` to the new buildout location and make buildout
extend off it.

Hopefully having `buildout.dumppickedversions`_ in place now should
resolve doing this again if/when I'm migrating any of my new Plone
installs. (Interesting to note my current dev install uses over 320
eggs).

.. _buildout.dumppickedversions: http://pypi.python.org/pypi/buildout.dumppickedversions
