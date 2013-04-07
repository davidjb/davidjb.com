Increasing Plone's session timeout
##################################
:date: 2011-03-08 10:01
:author: davidjb
:category: Plon
:tags: buildout, plone, session, timeout, zope
:slug: increasing-plones-session-timeout

What you may notice if you're developing with Plone/Zope, is that if
you're storing small pieces of data within Plone's session variable (the
session\_data\_manager tool), data expires after a few minutes.  By
default, this timeout is 20 minutes, but is far too short if you're
expecting the information stored to last for say the whole time a user
is logged in.  In this situation, you'll need to increase the timeout.

Documentation on changing the session timeout is potentially a little
sketchy (Google "session-timeout-minutes zope"), but it's clear that you
need to change the ``session-timeout-minutes`` directive in your
``zope.conf``.

What's not immediately obvious is how to make a session persist
indefinitely (until server reboot), but this can be achieved by setting
the value to 0. Within a buildout environment for Plone, adding this
under your Plone's instance section will add the configuration to your
zope.conf.

.. code:: cfg

    [instance]
    ...
    zope-conf-additional =
        session-timeout-minutes 0

There are obviously implications for performance and other issues
associated with persisting session data like this, but for arguments
sake, let's say we've considered them.  You'll probably also want to
consider deleting session data stored like this on logout (see `Session
Variables`_ in the Plone collective documentation) but that's dependant
on your use case.

.. _Session Variables: http://collective-docs.plone.org/sessions/session_variables.html
