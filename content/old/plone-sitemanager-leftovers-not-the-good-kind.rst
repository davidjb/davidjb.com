Plone: SiteManager leftovers; not the good kind
###############################################
:date: 2010-06-28 14:35
:author: davidjb
:category: Plone 
:tags: egg, error, install, plone, problem, site, update, zope
:slug: plone-sitemanager-leftovers-not-the-good-kind


.. note:: **Update:** You should check out `wildcard.fixpersistentutilities`_
    - it's a fantastic solution to problems like this. Many thanks to
    Nathan Van Gheem, the author of the add on. Check out the link and
    see how to install it (temporarily) on your Plone instance that
    needs its site manager cleaned up.

Leftovers are typically useful when they're in your fridge at home. They
mean you don't have to mess around making lunch for the next day for
work, and can just grab them, and walk right out the door. Now,
leftovers in the zope.component SiteManager aren't so nice, especially
when some Plone products fail to remove what they've registered. The
consequences of this are that you've got references left which will
break things when you uninstall/remove the physical eggs/files. These
leftovers would be ones would be mutated food that comes to kill you
after you've thrown it in the bin, assuming we follow the same analogy.
But how to fix them?

Here's the error message you might be faced with when trying to install
or uninstall products -- something that stops you might in your tracks:

.. code:: pytb

    2010-06-22T10:38:48 ERROR Zope.SiteErrorLog https://mysite.com/portal_quickinstaller/uninstallProducts
    Traceback (innermost last):
    Module ZPublisher.Publish, line 125, in publish
    Module Zope2.App.startup, line 238, in commit
    Module transaction._manager, line 96, in commit
    Module transaction._transaction, line 395, in commit
    Module transaction._transaction, line 495, in _commitResources
    Module ZODB.Connection, line 510, in commit
    Module ZODB.Connection, line 555, in _commit
    Module ZODB.Connection, line 582, in _store_objects
    Module ZODB.serialize, line 407, in serialize
    Module ZODB.serialize, line 416, in _dump
    PicklingError: Can't pickle <class 'p4a.plonevideoembed.interfaces.IVideoLinkSupport'>: import of module p4a.plonevideoembed.interfaces failed

Unsurprisingly, it's similar to something I encountered before. Way back
when, I hit the same issue with `ZipFileTransport`_, and my fix for it
is just as relevant today as it was then. Start up a zopepy session (or
ipython) that still has the relevant classes in the system path, and run
this:

.. code:: python
    
    from p4a.plonevideoembed.interfaces import IVideoLinkSupport as intclass
    from p4a.video.interfaces import IVideoSupport as intclass2

    from zope.app.component.hooks import setSite
    from zope.component import getSiteManager
    setSite(portal)
    sm = getSiteManager()
    sm.unregisterUtility(component=None, provided=intclass)
    sm.unregisterUtility(component=None, provided=intclass2)

    #Even though unregister happened, it probably said it worked but left crap around.
    #Let's clean it up.

    #This intclass variables might not be right or perfectly complete. It's going to be the key present below,
    #so you can always find the right InterfaceClass manually and set it accordingly.
    del sm.utilities._adapters[0][intclass]
    del sm.utilities._subscribers[0][intclass]
    del sm.utilities._subscribers[0][intclass2]
    del sm.utilities._adapters[0][intclass2]

    #From here, search for a term to see if it's gone
    #Each should return -1. If not, you've done something wrong!
    str(sm.utilities._adapters[0]).find('p4a')
    str(sm.utilities._subscribers[0]).find('p4a')
    str(sm.utilities.__bases__[0].__dict__).find('p4a')

    import transaction
    transaction.commit()

Shut down your existing Plone/Zope instance and restart it. You should
now be able to install or remove products accordingly again -- and also
get rid of those old packages' physical files you don't need.

.. _wildcard.fixpersistentutilities: http://pypi.python.org/pypi/wildcard.fixpersistentutilities
.. _ZipFileTransport: |filename|plone-down-with-dodgy-products.rst
