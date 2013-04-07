Deliverance, Plone, and  tags
#############################
:date: 2009-11-27 15:17
:author: davidjb
:category: Plone
:tags: deliverance, element, plone, problem, theme, themeing, xml
:slug: deliverance-plone-and-tags

It's been a little bit of time since my last post, and who can blame me
with my site having been down for almost 2 full days over the last
week!  I'm not paying that much for the webspace, thankfully, but if I
was, I'd be seeing red over it.  Apparently some patch for MySQL broke
everything; imagine how it looked to see my site with a '500 internal
error' plastered all over it and not being able to access my cPanel. 
Ugh.

Anyway, everything's back again, assuming that you can see this.  Okay? 
Great!

Today's conundrum presented itself very, very strangely.  People
couldn't change their password in Plone (which effectively breaks
registration if a user has to select a password).  The Plone site we
have was being themed by Deliverance. A colleague and I were taking a
look at this earlier in the week and from everything that we could see,
the request traffic and variables were being sent onto Plone correctly
from Deliverance. That said, the issue persisted.

The issue ended up being a missing <base> tag in the page's HTML <head>
tag. Since this <base> tag controls relative links on any given page, I
guess that the resulting request/etc for password selection must have
been affected.  I've seen some pretty whacked out things happen without
that base tag, including bad relative links (the obvious problem),
missing menus on content (another issue relating to an old blog post)
etc.

Essentially, Deliverance doesn't bring the <base> tag across by default,
as it doesn't know any better. That said, putting these new elements:

.. code:: xml

    <replace content="/html/head/base" theme="/html/head/base" />
    <append content="/html/head/base" theme="children:/html/head" />

in the deliverance.xml configuration solved the problem.  Depending on
your theme, you might want just one of the lines as it says "replace my
<base> tag in theme with the one from the page" and falls back to
"append the base tag into the theme".  Thanks the tag being moved with
the first command, the 2nd doesn't happen if the base tag is already
gone from the content.

*phew* That was confusing; hopefully it helps someone out!
