Adding a return URL during logout with CAS
##########################################
:date: 2012-01-11 11:38
:author: davidjb
:category: web programming
:tags: auth, cas, http, url, web
:slug: adding-a-return-url-during-logout-with-cas

CAS (Central Authentication Service) is a single-sign-on service (say
that several times quickly) and through accessing a CAS ``/logout`` URL,
as an application, you're able to log the given user out.  What wasn't
clear (by Googling) was whether there's a possibility to redirect the
user back to the original application (or a given URL).  I now know,
thanks to the `CAS Protocol Documentation`_ (section 2.3), that any
posts that mention adding ``?service=http://my.url/`` to the ``/logout``
URL are incorrect, as this isn't a valid parameter (at least not at time
of writing).

However, you can add a ``?url=http://my.url/`` to the logout URL and get
this (likely, depends on your CAS settings) displayed as a link on the
logout page. So, a full URL like this is good to go::

    https://cas.foo.edu/cas/logout?url=http://davidjb.com/

.. _CAS Protocol Documentation: http://www.jasig.org/cas/protocol
