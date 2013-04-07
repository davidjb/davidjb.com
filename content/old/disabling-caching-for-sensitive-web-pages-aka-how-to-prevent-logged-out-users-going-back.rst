Disabling caching for sensitive web pages (aka how to prevent logged out users going 'back')
############################################################################################
:date: 2011-03-24 12:50
:author: davidjb
:category: Web
:tags: caching, http, no-store, rfc, web
:slug: disabling-caching-for-sensitive-web-pages-aka-how-to-prevent-logged-out-users-going-back

We all see web pages like Internet banking, HR systems, email, and more
that allow you to log in, do something and load pages, log out, and then
prevent you from using your browser's history to see that sensitive
information.  I'm amazed that in my searches I couldn't quickly find a
definitive source of information on how to achieve this.  Pages across
the web in a search for 'stop caching' range from blog posts, to forum
posts, to other pages, and people asking the question (try it: `here`_,
or `maybe here`_).

Maybe I got unlucky, but finding a definitive answer to the questions of
"how to prevent the use of the back button" or "how to stop browsers
caching" etc wasn't a piece of cake. Hence this post.

The answer isn't concrete in itself either due to differing browser
support, but the most useful information comes from RFC2616, the RFC for
HTTP/1.1. In `section 14.9.2`_, we learn about ``no-store``. This cache
directive should see a correctly-implemented browser not storing a
request/response on disk (non-volatile storage) and deleting the info as
quick as possible from RAM (volatile storage).

I've found that combining this, with an Expires header, and other
Cache-Control directives, has worked across Firefox 4, Chrome 10,
Internet Explorer 6, 7, 8, and 9 to keep relevant pages entirely out of
the cache. Here's a snippet from some Python code:

.. code:: python

    response.setHeader('Expires', formatDateTime(getExpiration(0)))
    response.setHeader('Cache-Control', 'no-store, no-cache, max-age=0, must-revalidate, private')

You could likely use this in the <meta> tags in your page too.

This, by all means, isn't a guaranteed solution as the RFC may not be
followed by all browsers.  I've also noted that the RFC isn't exactly
clear with regards to a browser's history this sort of thing.  `Section
13.13`_ mentions that "a history mechanism is meant to show exactly what
the user saw at the time when the resource was retrieved", and using the
RFC-specified ``no-store`` on a logged in page (or anything dynamic)
would seemingly break this implication.

At any rate, seems like this implementation works successfully on the
browsers I've tested. Apparently IE doesn't like the ``no-store`` or
``no-cache`` settings in certain circumstances but it's been fine for me
thus far.

.. _here: http://www.google.com/search?q=stop+caching
.. _maybe here: http://www.google.com/search?q=stop+caching+firefox
.. _section 14.9.2: http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9.2
.. _Section 13.13: http://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html#sec13.13
