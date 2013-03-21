Logged out users can't bring up the Plone popup calendar
########################################################
:date: 2009-12-18 12:10
:author: davidjb
:category: Plone
:tags: authenticated, calendar, css, javascript, members, plone, popup, problem, testing, users
:slug: logged-out-users-cant-bring-up-the-plone-popup-calendar

It's another one of those 'strange' problems that has cropped up, but by
default in Plone, users who aren't authenticated aren't actually able to
bring up a pop-up calendar on a date field.

It's amazing that I haven't run into this issue before with something
like PloneFormGen, where you'd think that a simple Date input field
would be pretty common.  Although, I guess it's the case that even
though I've used these given forms, I've probably never taken much
notice of the popup calendar icon and just selected a random date from
the drop-down lists.  I suppose entering a random number on they
keyboard and hitting tab across the fields 3 times is simpler than going
for the mouse.  Who knows.

Anyway, the issue presents itself with an error in the Javascript on the
page, with something like 'plone.jscalendar not defined', if my memory
serves me correctly.  I believe that Firebug/Firefox didn't show up an
error for me (because I was logged in!) so make sure you test this on
your site when you're logged out, if you've got such fields.  Testing in
IE revealed the problem since my IE versions in my VM can't actually
enter details into form fields, thus preventing me *from* actually
logging in.

Solution
~~~~~~~~

The solution was the only Google result at the time, and that was at:
`http://plone.org/products/ploneformgen/issues/232`_

Essentially, head into the portal\_css and portal\_javascripts areas in
the ZMI and look search on the page for "calendar".  You should find
that the 'condition' on these resources isn't right (eg only logged in
users or "not: portal/portal\_membership/isAnonymousUser" is set or
isn't correct at all).  Correct it accordingly to be blank (easiest
way!) and save.  You may need to enable/reload/disable the debugging
modes for the CSS and JS to see the change immediately.

.. _`http://plone.org/products/ploneformgen/issues/232`: http://plone.org/products/ploneformgen/issues/232
