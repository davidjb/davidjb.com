Buildout and Version Problems
#############################
:date: 2009-01-06 16:35
:author: davidjb
:category: Python 
:tags: buildout, easy_install, python
:slug: buildout-and-version-problems

Two blog entries in one day - wow it's been a good work day.

Just a quick chronicle of my thoughts: version conflicts in buildout
aren't always pretty. My latest escapade into trying to load up Varnish
through zc.buildout resulted in a hair-tearing out message:

.. code:: pytb

    An internal error occured due to a bug in either zc.buildout or in a
    recipe being used:
    Traceback (most recent call last):
    File "/tmp/tmp8o-_PD/zc.buildout-1.1.1-py2.4.egg/zc/buildout/buildout.py", line 1477, in main
    File "/tmp/tmp8o-_PD/zc.buildout-1.1.1-py2.4.egg/zc/buildout/buildout.py", line 346, in install
    File "/tmp/tmp8o-_PD/zc.buildout-1.1.1-py2.4.egg/zc/buildout/buildout.py", line 857, in getitem
    File "/tmp/tmp8o-_PD/zc.buildout-1.1.1-py2.4.egg/zc/buildout/buildout.py", line 938, in _initialize
    File "/tmp/tmp8o-_PD/zc.buildout-1.1.1-py2.4.egg/zc/buildout/buildout.py", line 901, in _install_and_load
    File "/usr/lib/python2.4/site-packages/setuptools-0.6c9-py2.4.egg/pkg_resources.py", line 277, in load_entry_point
    return get_distribution(dist).load_entry_point(group, name)
    File "/usr/lib/python2.4/site-packages/setuptools-0.6c9-py2.4.egg/pkg_resources.py", line 2179, in load_entry_point
    raise ImportError("Entry point %r not found" % ((group,name),))
    ImportError: Entry point ('zc.buildout', 'default') not found

What??? What's that supposed to mean?

Turns out I managed to stumble upon the cause: our local PyPi repository
had actually already had an old version of the plone.recipe.varnish
source on it and my buildout needed the latest version. Even though I'd
directed buildout to seek out such version, my cache folder already
thought it was satisfied.

Solution
~~~~~~~~

Remove the old version from the cache and stick the new version into the
local PyPi.
