Plone: Python Eggs And Development
##################################
:date: 2009-01-02 15:04
:author: davidjb
:category: Plone 
:tags: egg, linux, python, setuptools
:slug: plone-python-eggs-and-development

Welcome to the new year! It's the start of another journey around the
sun and the beginning of work for me. Whilst I'm the only one actually
working around here today, I thought I'd take the chance and update with
some useful info:

Troublesome Python eggs
-----------------------

Now, much to my amazement, when you're creating/compiling/whatever
Python eggs for Plone you need to actually specify the files you want
included in the build. I suppose it's fair enough, but thought it might
have actually done it for me. No such luck!

The ``SOURCES.txt`` file in the egg-info folder needs to be updated
accordingly. A command like ``find ‘pwd` -name "*.*"`` will do the trick
and list out the files in the directory (assuming you start from the
root of the egg). If there’s extra stuff in the folder, you'll probably
need to weed out the extraneous files (.pyc, git, svn, etc) before
building the egg with::

    david@computer: python2.4 setup.py build
    david@computer: python2.4 setup.py sdist bdist\_egg

which gets our lovely setuptools to build (scramble?) the egg and place
the source and egg into the ``dist`` folder. Providing the SOURCES.txt
file was correct, then you'll have the right files included. If you
don't, you'll be in for trouble when you try and include the egg under
ZCML etc because the files just don't come along for the ride.

Serve with sides of bacon and toast, place into your favourite PyPi
(cheese shop) and include with your buildout config.

Further reading
---------------

If you're really bored, check out
http://peak.telecommunity.com/DevCenter/setuptools for some good
material on what Setuptools can do for you.
