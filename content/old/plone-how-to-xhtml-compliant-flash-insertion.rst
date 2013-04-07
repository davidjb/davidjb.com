Plone How-To: XHTML Compliant Flash Insertion
#############################################
:date: 2009-01-13 16:40
:author: davidjb
:category: Plone 
:tags: filtering, flash, parameters, plone, xhtml
:slug: plone-how-to-xhtml-compliant-flash-insertion

Wow, it seems easy doesn't it. Just add an object tag, params, and embed
and we're done, right? Well, sure, if we didn't want to adhere to W3C
standards.

To do the right thing, we need something like this:

.. code:: html

    <object type="application/x-shockwave-flash" data="movie.swf" width="100" height="100">
        <param name="movie" value="movie.swf" />
        <img src="alt.jpg" width="100" height="100" alt="" />
    </object>

Not much to it there, and this is available everywhere on the web. It
validates okay, and that's what we need.

However, if you follow normal procedure for sticking this in Plone
(disable filtering of the relevant **object** and **param** tags in HTML
Filtering (Plone Control Panel), then make a Page with this code),
you'll see it won't work in IE.

Much hair-tearing and searching led me to find that the rendered Page is
missing the **param** tag in the source XHTML. Huh?!?, you say - I just
disabled the filtering. Why's it not there?!.

Sure, you did. What noone told you is that you need to go into the ZMI
-> portal\_transforms -> safe\_html and tell Plone that the **param**
tag is an *empty tag* (like <img />). In the list of **valid\_tags**,
set **param** to be *0*. Save this page.

Now try it again in IE. Looking at the source in both should show the
**param** tag now, and your Flash should show up just fine once you
convince IE to refresh.
