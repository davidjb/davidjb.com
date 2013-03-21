Buildout: Trying to create a Plone/Zope instance
################################################
:date: 2009-02-11 08:51
:author: davidjb
:category: Python 
:tags: bootstrap, buildout, error, plone, script, zope
:slug: buildout-trying-to-create-a-plonezope-instance

Eeek...what's this mean?

.. code:: pytb

    install() got an unexpected keyword argument 'allow_hosts'

after trying to build zope2zeoserver from my buildout configuration.

After some searching, I found that it was due to my bootstrap.py script
(the one the gets buildout in the first place and creates the relevant
scripts) was actually pulling down an outdated version of zc.buildout.
So, the problem results because this old version of buildout doesn't
have a clue how to handle the given argument.

**Solution:** update the buildout. For me, that meant correcting the
bootstrap script, but for you, it could be a matter of using
easy\_install to take care of that for you.
