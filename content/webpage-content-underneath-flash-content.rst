Webpage content underneath Flash content
########################################
:date: 2009-06-12 13:33
:author: davidjb
:category: Web
:tags: content, flash, html, problem, web, xhtml
:slug: webpage-content-underneath-flash-content

So, you've got a website that you've made and you've used a Flash movie
on it.  Okay, no worries.  Now, what if you tried to add a
(non-form-element) drop-down menu or some AJAX-ed content into the site,
and found the Flash movie actually acted as an overlay?

This problem doesn't seem consistent.  Different OSs, browsers, and
Flash versions don't indicate consistency - that's what I've seen
anyway.  Nevertheless, the problem persists for some users and it's
down-right annoying.

The fix?  Make your Flash code look similar to this:

.. code:: html

    <object data="my-movie.swf" type="application/x-shockwave-flash" height="100" width="200">
        <param name="movie" value="my-movie.swf" />
        <param name="quality" value="high" />
        <param name="embed" value="transparent" />
        <param name="wmode" value="transparent" />
        <param name="menu" value="false" />
        <img src="alternate.jpg" alt="ARCS - Revolutionising Collaboration" height="100" width="200" />
    </object>

That there should be entirely XHTML compliant (and completely
cross-browser compatible) code for creating a Flash object on your page
that'll place nice with other content.
