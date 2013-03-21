GenericSetup and "mismatched" tags in ZCML
##########################################
:date: 2010-03-12 11:01
:author: davidjb
:category: Plone
:tags: configuration, error, mismatched, plone, tags, xml, zcml, zope
:slug: genericsetup-and-mismatched-tags-in-zcml

Ever the issue-magnet, I've spent the better part of my morning trying
to debug a mistmatched tag error from within some ZCML (aka XML for the
non-initiated).  Essentially, the issue boiled down to the system
telling me that it was certain that I had a mistmatched tag within my
configuration, and presented me with the problematic XML tag (complete
with line numbers).  However, life's not always that simple.

The traceback looked like this:

.. code:: pytb

    Traceback (most recent call last):
    zope.configuration.config.ConfigurationExecutionError: xml.parsers.expat.ExpatError: mismatched tag: line 6, column 70
    in:
    File "/home/david/buildout/src/aaa.project/aaa/project/profiles.zcml", line 9.2-15.6

And specified the exact genericsetup:registerProfile configuration that
was problematic. After much poking and prodding and thinking that there
must be some random character hidden in my configuration file (and
checking other files that call this one), no dice. Even copying and
pasting some new code that I knew worked just simply didn't when I put
it here.

So, I just happened to actually think about what I'm calling with this
ZCML: a Plone product generic setup profile. And, yes, now it seems so
clear that the issue was in fact in that GS profile. My vim editor had
kindly re-auto-closed a tag that it shouldn't have (because it was
already closed) in my metadata.xml. Fixing that solved the issue and let
my Zope instance start up again.
