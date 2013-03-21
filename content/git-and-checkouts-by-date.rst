Git and checkouts by date
#########################
:date: 2009-09-07 13:09
:author: davidjb
:category: Git
:tags: date, git, history, versions
:slug: git-and-checkouts-by-date

Cheers to this `very handy post`_ for posting details from Nabble on how
to check out a git branch based upon the date it was commited.  If I
haven't modified Wordpress to turn off the character replacement, then
watch out because the double-quotes and double-dash will need to be
checked before running the command:


.. code:: bash

    git checkout `git rev-list -n 1 --before="2009-07-27 13:37" master`

A very easy way to flick back to a given revision.

.. _very handy post: http://www.bramschoenmakers.nl/en/node/645
