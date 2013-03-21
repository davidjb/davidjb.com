Deliver me from ... Deliverance?
################################
:date: 2009-09-02 14:26
:author: davidjb
:category: Themes
:tags: bleeding edge, deliverance, plone, rules, technology, theme, themeing, xml
:slug: deliver-me-from-deliverance

Always one for being on and beyond the bleeding edge of new technology,
I've (with the help of colleagues) been setting up a new technology for
applying themes to web sites.  In particular, I'm applying Deliverance
to Plone and whilst I'm not the first one to venture out into the
wilderness this way, I've got to be thinking that I could be one of the
few people documenting their experience.  Ah, but where to begin?

The proxy
~~~~~~~~~

Ah yes, the proxy.  Deliverance is very kind to us in that it operates
it's own proxy.  This, whilst okay, is a royal pain when Apache or
similar is sitting in front, sending rewritten URLs to Deliverance [I'm
hosting as a sub-folder on a domain].  Maybe I'm just not cluey enough
to figure it out, but when you spend almost a week and then have to hack
things about with python code, it's probably not just me.  In some
cases, I think Deliverance is just trying to be 'too' smart, and you'll
see what I mean shortly.

At any rate, I've made Apache do a **ProxyPass** to Deliverance and then
make Deliverance do the "rewriting", and then the Zope VHM makes magic
happen like normal.  Great!  Except no, that's not it, because
Deliverance has no idea about the fact my site is hosted from both HTTP
and HTTPS (or hosted from 2 domains)?  What I've had to do is thus in
Apache (and the same for HTTP etc):

.. code:: apache

    RequestHeader set X-Forwarded-Scheme https
    RequestHeader set X-Forwarded-Port 443
    ProxyPass /mysite http://my.deliverance.host:8000/mysite

and then this in Deliverance, since we now have what scheme/port/host
we're serving from.  All URLs coming back from Plone/VHM will be okay!
8-):

.. code:: apache

    <proxy path="/mysite" domain="my.sites.domain">
    <dest href="http://localhost:8080/VirtualHostBase/{X-Forwarded-Scheme}/{X-Forwarded-Server}%3A{X-Forwarded-Port}/mysite/VirtualHostRoot/_vh_mysite" />
    <transform strip-script-name="1" keep-host="0" />
    <response rewrite-links="0" />
    </proxy>

The theme
~~~~~~~~~

Oh, the theme.  Again, Deliverance tries to be too smart for its own
good if you specify a Deliverance-hosted theme here.  If you have
something relevative (eg ``/_theme/theme.html``), it'll work, but on your
HTTPS site all theme elements will be unencrypted since HTTP is it. 
Whoops!

Resolution?  Not nice, but you'll need to serve your resources outside
of Deliverance (probably faster anyway!), and have them accessible for
both protocols.  The good news is that when you specify an **absolute**
URL, with protocol, then Deliverance pays attention, thus:

.. code:: xml

    <theme href="{X-Forwarded-Scheme}://static.web.server/static/mysite/theme.html" domain="my.sites.domain" />


POST requests
~~~~~~~~~~~~~

Ughh.  Deliverance feels the need to be smart, *again*, by applying
themes to incoming POST requests.  Now, I can't think of any time you'd
*actually* want this (unless...well, no..never), so make sure you've got
something like this in your XML file to stop Deliverence:

.. code:: xml

    <match environ="REQUEST_METHOD: POST" abort="1" />

Copying/Moving Attributes
~~~~~~~~~~~~~~~~~~~~~~~~~

Okay, now this one's just weird.  You need to specify which individual
or several attributes from your content and then tell Deliverance to
apply them all to the attributes of the target element.  Seems simple
enough now, but why is there no doco?  This works:

.. code:: xml 

    <replace content="attributes(href):#portal-logo" theme="attributes://*[@id='globalnav']/div/a" />

and this won't (type mismatch error):

.. code:: xml

    <replace content="attributes(href):#portal-logo" theme="attributes(href)://*[@id='globalnav']/div/a" />


Conclusion
~~~~~~~~~~

Don't get me wrong, I like Deliverance.  Xpath support is great, CSS
3-style selectors are awesome, and what it does is magical.  However, it
needs a bit of work before I parachute away from Plone's themes for
good.

Fair's fair though, it's only version 0.3.  I'm looking very forward to
the future though.
