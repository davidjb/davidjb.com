Plone: Issues with products
###########################
:date: 2009-04-23 09:15
:author: davidjb
:category: Plone 
:tags: plone, problem, products, zip

Oh dear. Products in Plone that don't care to uninstall themselves at
all when removed. One such product that comes to mind is
ZipFileTransport.

I could go into depth all day about its failure to uninstall, but in
specific, it's this line of code in its setupHandlers.py file that kills
me:

.. code:: python

    sm.registerUtility(ZipFileTransportUtility('zipfiletransport'), IZipFileTransportUtility)

Now, where's the unregisterUtility called? Nowhere, unfortunately. So
when one tries to go and install/uninstall/reinstall/do certain things
on the site, you get a nasty failure message about trying to unpickle a
python object:

.. code:: pytb

    2009-04-23 10:19:19 ERROR Zope.SiteErrorLog http://localhost:8080/eresearch/portal_quickinstaller/uninstallProductsTraceback (innermost last):
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
    PicklingError: Can't pickle: import of module Products.ZipFileTransport.utilities.interfaces failed

Solution?
~~~~~~~~~

Okay, I found the unregisterUtility function in zope.component, and it
can be accessed by something like this (ipython session, of course):
(You'll need at least the ZFT parts below present to import them).

.. code:: python

    from zope.app.component.hooks import setSite
    from zope.component import getSiteManager
    from Products.ZipFileTransport.utilities.interfaces import IZipFileTransportUtility
    from Products.ZipFileTransport.utilities.utils import ZipFileTransportUtility
    setSite(portal)
    sm = getSiteManager()
    sm.unregisterUtility(component=None, provided=IZipFileTransportUtility)

    #Even though unregister happened, it probably said it worked but left crap around.
    #Let's clean it up

    #This intclass variable might not be right.  It's going to be the key present below,
    #so you can always find the right InterfaceClass manually and set it accordingly.
    intclass = IZipFileTransportUtility
    del sm.utilities._adapters[0][intclass]
    del sm.utilities._subscribers[0][intclass]

    #From here, search for 'Zip' to see if it's gone
    #Each should return -1.  If not, you've done something wrong!
    str(sm.utilities._adapters[0]).find('Zip')
    str(sm.utilities._subscribers[0]).find('Zip')
    str(sm.utilities.__bases__[0].__dict__).find('Zip')

And thus ends the tyranny of ZipFileTransport.

**Edit:** I should make it clear that to run the above commands you need
to have a handle to your Plone site object, and be pre-set as the
'portal' variable. If you set up ipython like so:
http://plone.org/documentation/kb/setup-ipython-for-zope then that takes
care of things automatically and gives you interactive handles to your
portal and Zope app root. If you're not using this, then figure out how
to set 'portal' manually to be your Plone site object (not a string or
name, but the actual object) and run the rest of the lines of code.

Also, I'm not sure whether you need to commit your changes or not. If
you find the changes don't stick, then try this in your ipython session:

.. code:: python

    import transaction
    transaction.commit()

