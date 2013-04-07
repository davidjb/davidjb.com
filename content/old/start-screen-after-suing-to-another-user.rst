Start screen after su'ing to another user
#########################################
:date: 2009-12-04 15:49
:author: davidjb
:category: Linux 
:slug: start-screen-after-suing-to-another-user

Today's problem is one that requires no introduction (well, maybe it
does :-\| ) but it's a problem nonetheless.  The issue is that after
using the '**su**\ ' command to become another user, there's trouble
running **screen** sessions.

This page
(`http://dbadump.blogspot.com/2009/04/start-screen-after-sudo-su-to-another.html`_)
details it simply and perfectly (which, yes, I know in turn came from
another page).  Essentially the error is thus::

    Cannot open your terminal '/dev/pts/1' - please check.

Which really doesn't man nor beast with its descriptiveness.  From that
page, which came from another page mentioned on that page (?), here's
the fix:

.. code:: bash

    su [userName]
    script /dev/null
    screen -x [screenName]

And that's it!  Simple solution, and many thanks to that blog for
sorting it out for me.

.. _`http://dbadump.blogspot.com/2009/04/start-screen-after-sudo-su-to-another.html`: http://dbadump.blogspot.com/2009/04/start-screen-after-sudo-su-to-another.html
