Plone: Relative 'Recent Changes' Portlets
#########################################
:date: 2008-11-20 11:33
:author: davidjb
:category: Plone
:tags: features, plone, portlets, product, python
:slug: plone-relative-recent-changes-portlets

The problem I've been faced with today on our Plone systems is that I
need to created a 'Recent Changes' portlet that's relative to where the
user is on the site.

Now, the standard portlet doesn't do anything for me, so that's pretty
useless. I had a look at the standard code for the portlet too and it's
not really feasible to try and mess with:

.. code:: xml

    <tal:recentlist define="view here/@@recent_view; results here/results;">

However, using a (nasty?) workaround, if we put the classic Recent
Changes portlet into play, we can change that above code in the ZMI to
something like:

.. code:: xml

    <tal:recentlist define="view here/@@recent_view;
                            theseResults python:container.portal_catalog(path='/'.join(context.getPhysicalPath()),sort_on='modified',sort_order='reverse');
                            results python:theseResults[:5];">

So, we handle the problem by asking the portal catalog this time, and
only wanting stuff that's under our current physical path. By using the
*path* parameter for the catalog, this works its magic for us. The
sub-selection of the array handles cutting back the results.

I noticed that the portlet also has links in its header and footer to
'/recently\_modified'. This would, typically, just give us the
everything on the portal, but by making a new page template with a
slightly different name, copying the code in from 'recently\_modified',
modifying its *results* as above, and pointing the portlet's links at
this new page template under our current page:

.. code:: python

    python:here.absolute_url()+'/relative_recently_modified'

we end up with a nice, relative, recent changes full listing.

It's a brutal hack, but you could apply the same idea to an actual
product and make a real Plone 3 portlet out of this.
