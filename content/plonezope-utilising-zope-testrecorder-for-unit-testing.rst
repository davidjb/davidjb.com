Plone/Zope:  Utilising zope.testrecorder for unit testing
#########################################################
:date: 2010-03-25 09:40
:author: davidjb
:category: Plone 
:tags: buildout, install, plone, product, recorder, test, unit tests, zope
:slug: plonezope-utilising-zope-testrecorder-for-unit-testing

Writing unit tests (especial doctests) for your Plone product is
reasonably time consuming. For us developers, having tested code is
absolutely essential. This is especially true when clients are beating
down your door looking for a fully functional product and you need to
know what you've written works and isn't going to fall over (just yet,
anyway). Web apps are able to be tested using a multitude of frameworks,
and whilst not the most fully featured (eg lacking Javascript support),
Zope's doctest machinery is right there within your Plone product. In
order to write these, enter zope.testrecorder to more-or-less automate
replicating your actions into tests.

zope.testrecorder is simple to install: just add it to your eggs list
under your buildout's relevant instance section, and also the
corresponding zcml list too. Re-run your buildout and you will now have
the latest version of the package installed.

There's some good documentation out there about this, such as `Martin
Aspeli's article`_ on plone.org, but it's slightly dated given latest
updates with the package. Essentially, everything is relevant with the
exception of how to actually access the test recorder now. Enter
`PyYou's post`_ about this same topic. Thanks to that article I now know
you should go to
**http://zopehost:port/++resource++recorder/index.html** to access the
test recorder, and not try and add an object in the root of Zope (or
elsewhere).

Aside from that, the recorder works like a charm. You input the address
of what site (it can be anything or anywhere) you want to test and click
the 'Go' button. Everything you do (mostly) gets monitored and recorded.
A few words to the wise though:

-  No testing or recording Javascript-based or centric actions.  So
   don't expect that product you wrote with the Google Maps API to work
   so well with recording tests.  Or, don't expect the test recorder to
   understand correctly that you clicking on the 'Add New...' menu in
   Plone isn't actually a real link.
-  No ability to just browse with Javascript turned off.  Essentially,
   as the zope.testrecorder itself needs Javascript to run, you can't
   turn it off, thinking you'll record things correctly, or at all. 
   Maybe there's a way around this issue, but it's likely more
   complicated than I care to concern myself with.
-  Specialised form widgets are problematic.  The Plone visual editor is
   one (Javascript, again), but does work if you switch the editor to be
   HTML before saving a form.  Another example that will require some
   fancy work around is z3c.relationfield -- there's no non-Javascript
   fall back here (that I can see).
-  You'll need to manually intervene with the rendered tests and fix
   some things up.  For example, testing the default title of a Plone
   site doesn't work because there's a hyphen in the title.  It's a
   special character and thus saved "incorrectly" within the doctests.

Aside from all that, most of the heavy lifting is done for you, so
cheers to the creators of zope.testrecorder for making my life just that
bit easier.

.. _Martin Aspeli's article: http://plone.org/documentation/kb/testing/zope-testrecorder
.. _PyYou's post: http://pyyou.wordpress.com/2008/04/11/how-to-install-zopetestrecorder-with-buildout/
