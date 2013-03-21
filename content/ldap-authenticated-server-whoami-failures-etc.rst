LDAP-Authenticated Server & Whoami Failures (etc)
#################################################
:date: 2009-09-28 11:53
:author: davidjb
:category: Linux
:tags: authentication, centos, chmod, ldap, login, permissions, users
:slug: ldap-authenticated-server-whoami-failures-etc

I'm back again, after a bit of a unscheduled 'break' in my normal work
life.  After a couple of days away for work on the Gold Coast, then the
sad passing of my Grandfather and his memorial, then being sick over the
last weekend from what I can only guess was a nasty 24-hour bug, I'm
back.  And whilst a little worse for wear still today, it's life pretty
much as normal.

Today's fun and games was on a server we use that uses LDAP
authentication for its users.  Nothing special, except that today I
started getting weird errors when logging in as my LDAP account, and the
server booting me off with random error messages::

    whoami: cannot find name for user ID 75966
    -tcsh: ldap-nss.c:1312: do\_init: Assertion \`cfg->ldc\_uris[\_\_session.ls\_current\_uri] != ((void \*)0)' failed.

Solution
~~~~~~~~

The simple solution was to check the permissions on ``/etc/ldap.conf``
(Centos) and sure enough, the permissions weren't allowing normal users
to read it (eg not 644).  Running this solves the problem:

.. code:: bash

    chmod 644 /etc/ldap.conf

Cheers to the author @
http://www.ducea.com/2008/03/07/ldap-troubleshooting-i-have-no-name/ for
the details.
