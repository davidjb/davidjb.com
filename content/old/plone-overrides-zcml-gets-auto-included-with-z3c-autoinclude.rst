Plone: Overrides.zcml gets auto-included with z3c.autoinclude
#############################################################
:date: 2010-07-13 15:01
:author: davidjb
:category: Plone 
:tags: auto, icons, include, plone, plone 3, problem, theme, z3c, zcml, zope
:slug: plone-overrides-zcml-gets-auto-included-with-z3c-autoinclude

Unsurprisingly, specifying a z3c.autoinclude entry point in your Plone
product egg means your ZCML gets automatically included. That's great
because it means you don't have to specify your product under the ZCML
section of your instance in buildout. One thing that isn't so obvious
(it's not mentioned that I can see on `plone.org`_) is that if your
package is marked for ZCML autoinclude, then Plone will automatically
load an ``overrides.zcml`` file in your product.

Nothing hits you like a slippery wet fish in the face more than hitting
this issue and having it obfuscated through a lot of different layers.
The first symptom was that my content icons weren't appearing within my
Plone site. Only some of them though -- the ones in folder listings and
the navigation portlet. I thought nothing much of it initially, just
thinking the setting for displaying content icons had been changed in
the Plone control panel.

I started digging into this issue a bit more because it was annoying me.
That, and changing the control panel's options weren't working. Hacking
a few bits into the folder\_listing.pt view showed me that icons were
there, just not outputting any HTML. Weird. Outputting the actual type
of the icon brain itself showed me::

    myorg.theme.layout.icons.CatalogBrainContentIcon

and didn't think much of it. So what, a class is being generated at run
time for my theme? It wouldn't surprise me -- Python can do some pretty
cool things and that's probably just one of them.

Taking the ``CatalogBrainContentIcon`` string and ``grep``'ing for it
showed me otherwise. My theme package had this class, amongst others,
hanging around in it's ``layout`` module. Moving the module and
restarting Zope showed me that the ZCML was being loaded.

But how/why? It was definitely excluded from my main ``configure.zcml``
files..but not excluded entirely though. Little did I realise that I had
an ``overrides.zcml`` file floating around. Commented out from
``configure.zcml``, but still there all the same. Turns out adding the
z3c.autoinclude entry point to the theme product makes Plone
auto-include all ``overrides.zcml`` (unless told otherwise).
**\*fish-smack to face\*** This behaviour was modified slightly in Plone
4.0a5, so that you can make your ``overrides.zcml`` be excluded, but
that doesn't mean anything about Plone 3.3.5.

So, watch out with seemingly innocuous ZCML files floating around. They
can still be brought into play.

.. _plone.org: http://plone.org/products/plone/roadmap/247
