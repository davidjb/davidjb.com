Missing content menus in Plone
##############################
:date: 2009-09-30 12:35
:author: davidjb
:category: Plone 
:tags: apache, hosting, menus, plone, rewrite, rules, urls, VHM, virtual hosting
:slug: missing-content-menus-in-plone

Another dose of insanity please!  Coming right up, sir.

Today's second discussion comes from an issue I was having recently with
a new Plone site that I was hosting behind Apache and Deliverance.  No
Varnish here yet, because I'd rather the site worked first before I try
and cache the life out of it.

Now, the specific problem I was having was that the content menus in
Plone (eg Add New, Display, State, Actions and for me, Sub-types)
weren't displaying.  I thought it a Deliverance issue - maybe I was
dropping those content items accidentally or not including the
JavaScript needed to display them.  Uh, nope on both accounts.

Solution
~~~~~~~~

After a detailed search of everything I could have been doing wrong, I
can across my Apache rewrite rules.  Amazingly enough, I'd left off the
**/\_vh\_mysite** at the end, so the URLs weren't being written
correctly.  Whilst the site was loading (mostly) fine, because I'd
inserted the URL to point to the site correctly, I'd forgotten that the
VHM needs the \_vh\_mysite part.

Adding it in fixed the problem in a second, along with a throat-clearing
shift-refresh.
