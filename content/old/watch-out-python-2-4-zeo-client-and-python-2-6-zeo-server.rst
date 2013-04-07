Watch out: Python 2.4 ZEO client and Python 2.6 ZEO Server
##########################################################
:date: 2011-07-11 16:23
:author: davidjb
:category: Plone 
:tags: database, fs, plone, server, zeo, zope
:slug: watch-out-python-2-4-zeo-client-and-python-2-6-zeo-server

Today was interesting when an issue with saving content on a Plone 3.3.5
site got reported to me. The system was producing undecipherable error
messages about ZEO disconnections and database conflicts whenever
someone would try and create some content within Plone (folders,
particularly). Errors looked like:

.. code:: pytb

    Module ZEO.zrpc.connection, line 796, in wait. DisconnectedError" and "raise ReadConflictError().
    ReadConflictError: database read conflict error"

and also:

.. code:: pytb

    ERROR ZEO.zrpc (2515) can't decode message: '(K\x11K\x01U\tserialnos(]((U\x08\x00\x00\x00\x00\x00X\x...'

-- essentially the issue described `here`_. My ZEO server was running
ZODB3 3.9.5 with Python 2.6, and my client running ZODB3 3.8.3 with
Python 2.4; almost everything worked.

The long and the short of this issue appears to be, as the `ZODB
documentation mentions`_, is that Python 2.4 servers work with 2.5+
clients, but not the other way around.  It's slightly misleading when
you read further and see that::

    ZODB ZEO clients from ZODB 3.2 on can talk to ZODB 3.9 servers. ZODB
    ZEO Clients can talk to ZODB 3.8 and 3.9 ZEO servers.

So, despite this seeming interoperability, dang - I can't use my
pre-existing ZEO server setup (based on the Plone 4 buildout for
versions, etc) which is currently in place and running.

Thankfully, building being what it is, the solution for me was to simply
re-use that buildout for any Plone instances that are Python 2.4
clients.  This was as simple as re-cloning my git repository where I
keep the buildouts, firing up a brand new virtualenv for Python 2.4, and
moving the data across.

One more thing...
~~~~~~~~~~~~~~~~~

There is one final thing worth mentioning, which I got awfully caught
out by.  I was finding that my ZEO processes, under this new
environment, just would not start - essentially, they would keep
respawning again and again until they stopped (triggered by some
'quick-respawn' safety mechanism, seemingly).  I thought this was some
issue concerning the fact I'd had my databases and files loaded against
newer ZEO versions, but this actually not.  This was a by-product of not
having my ZEO authentication database present - because there was no
file, presumably the processes kept crashing.  Sadly, no error message,
so hence this note.  Take care with this one.

.. _here: https://mail.zope.org/pipermail/zodb-dev/2010-December/013893.html
.. _ZODB documentation mentions: http://pypi.python.org/pypi/ZODB3/3.9.5#compatibility
