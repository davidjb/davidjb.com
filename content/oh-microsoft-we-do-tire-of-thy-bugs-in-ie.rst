Oh Microsoft, we do tire of thy bugs in IE
##########################################
:date: 2010-07-22 17:20
:author: davidjb
:category: Web
:tags: bug, css, html, IE, ie8, internet explorer, rendering, tag, tags
:slug: oh-microsoft-we-do-tire-of-thy-bugs-in-ie

Yes, it's another post about Microsoft and its poor implementation of
Internet Explorer. This time it's version 8 and its rendering of lists,
and in specific, links within list items. Most humorously, Microsoft's
own documentation (separate issue; about `rounded corners`_) gave me a
laugh when it said:

    "Microsoft is committed to providing a browser that
    accurately supports Web standards."

Maybe it's just me, but I've given up waiting for the day that IE actually
supports anything correctly.

So, the issue I found was that with a ``<ul>`` with a number of ``<li>``
tags inside wouldn't stop displaying the list bullets, despite a very
explicit CSS definition on the ``<li>`` tags.  Why this was the case,
I'm not sure, and am happy to chalk it up to IE being IE, like it always
is.

In order to fix the issue, however, I just started poking and prodding
IE in its Developer Toolbar with extra styles until it did what I wanted
it to.  Turns out that at least in my case, that in order to remove all
trace of bullets, I needed to have the ``list-style:none outside none;``
CSS declaration attached to the ``<ul>``, each ``<li>``, and the top
level ``<a>`` tags that were inside the ``<li>`` tags.  Talk about
repeating myself.  You'd think that the CSS would be applied to the
``<ul>`` and ``<li>``, which are list elements, and not be needed for
the ``<a>`` tag, which shouldn't matter despite it being in an ``<li>``.

I guess the good news is that you can bash the crap out of IE until it
works and Microsoft has provided the Developer Toolbar.  The bad news is
that "fixes" aren't always so obvious because you can never trust where
the bug could be.

As a final aside about IE 8, here's another snippet from that `same
documentation`_ about IE8:

    In Internet Explorer 8, we shipped several features from HTML5 and
    CSS3. Our primary goal was implementing CSS 2.1 (a specification
    that has reached final candidate stage) *completely and correctly*
    before moving on to specifications that are still in development and
    may change.

Completely and correctly implemented?  Again, I'm still waiting.

.. _rounded corners: http://msdn.microsoft.com/en-us/library/bb250413%28VS.85%29.aspx
.. _same documentation: http://msdn.microsoft.com/en-us/library/bb250413%28VS.85%29.aspx
