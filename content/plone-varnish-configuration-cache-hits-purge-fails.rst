Plone: Varnish Configuration (Cache Hits, Purge Fails)
######################################################
:date: 2009-01-21 08:40
:author: davidjb
:category: Plone 
:tags: cache, plone, problem, purge, varnish
:slug: plone-varnish-configuration-cache-hits-purge-fails

What a painful, painful day. It's taken about the entire day, but I've
finally figured out why our Varnish configuration around here for
Plone/Zope hasn't been accepting PURGE requests. Thus, without accepting
purge requests correctly, any content that gets changed in Plone doesn't
get updated in the cache until it times out (or we restart it). Ouch -
especially because it affects all sites under virtual hosting, and a lot
of these sites have publicly visible content that needs to be available
immediately.

So, the problem manifested itself as thus:

-  Cache hits happen
-  Performance was good on the Plone sites
-  PURGE requests sent to Varnish would produce 404's

So, after checking (many times) the object path for the PURGE was right,
Varnish would return a MISS and produce a 404 (DEBUG "VCL\_error(404,
Not in cache)" as the Varnish message).

Much searching/etc later, I found that using:

.. code:: bash

    curl -X PURGE http://localhost:8000/object/path

straight on the machine running Varnish would work and give a *200 Purged
response*. But, running the same command (replacing localhost with a FQDN) from
the Zope machine produced the 404. So, essentially, Varnish knows where to look
for the first command but not for the second.

Solution
~~~~~~~~

Where you set the backend for your Plone/Zope in the Varnish
configuration, add set req.http.host accordingly:

.. code:: cpp

    } elseif (req.url ~ "^/VirtualHostBase/https?/my.plone.site.com:(80\|443)/plone/VirtualHostRoot")
    {
    set req.backend = zope1;
    set req.http.host = "my.plone.site.com";
    }
    ...

In short, the URL is processed from Apache (in my situation) to result
in the *req.url*, and then Varnish needs to know what host anything
being cached relates to. Without it, hello 404 heaven.
