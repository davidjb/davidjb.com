Ubuntu 9.10 install hiccough
############################
:date: 2009-10-30 13:21
:author: davidjb
:category: IT, Linux
:tags: jaunty, karmic, koala, linux, problem, python, ubuntu, upgrade
:slug: ubuntu-9-10-install-hiccough

Yay, the new version of Ubuntu is out.  With it comes plenty of cool new
features (how awesome does the start up and login screen look now?) and
also plenty of opportunities for things to break when I've become so
accustomed to having them working.  At least it's not Windows though --
I think I may just gnaw my own limbs off before I have to get forced to
upgrade to Windows 7 for gaming reasons.

But I digress, there was one reasonably small problem with the upgrade
that I saw on both of my Ubuntu machines (laptop and desktop):
 python-wxversion has a problem and won't upgrade.  Looking back in the
terminal it appeared that either it was an "IOError: bad file
descriptor" or otherwise a certain file (well, it did change when I
tried to reinstall) like wxversion.py can't be found in
/usr/lib/python2.6.  All very confusing.

It was especially worrying when the installer came up and said "Sorry,
your upgrade failed.  Your system could be in an unstable state."  That
sent alarm bells ringing and possibly with good reason (eg broken apps)
-- at least I had good reason to fix the problem rather than just ignore
it.

The solution was simple for both machines:

.. code:: bash

    sudo apt-get remove python-wxgtk2.8
    sudo apt-get install python-wxgtk2.8

Not painful at all.  Except it was a case of finding which package to
reinstall.  Don't try and reinstall python-wxversion like I did because
you won't get far.  It'll still die.  python-wxversion is, however, a
dependency of the above package so all's well once you get that sorted.

From Googling, it looks like this problem was common and thankfully
fixed in the repos.  Although, it was still present on Karmic upgrade so
who knows.

Maybe it's bad Karma?  I bet 1000 people have made that joke already...
