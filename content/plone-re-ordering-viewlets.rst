Plone: Re-ordering Viewlets
###########################
:date: 2009-08-19 16:34
:author: davidjb
:category: Plone
:tags: genericsetup, plone, product, programming, theme
:slug: plone-re-ordering-viewlets

Just responded to a post on the Plone Nabble forums (`here`_) about how
to re-order viewlets.  In particular, this one is little different (but
not terribly so) because the original poster wanted to put the
breadcrumbs above the global sections (global tabs in Plone).  Normally,
this is straight forward because you just use a Generic Setup profile
(viewlets.xml) and use an order manager to move your viewlet.  This,
however, is a teeny bit more complicated because you've got one viewlet
that's outside of another viewlet manager.

Without further ado, my post from the forums:

    Check out
    `http://plone.org/documentation/tutorial/customizing-main-template-viewlets/reordering-and-hiding-viewlets`_
    for a pretty useful idea of manipulating viewlets.

    As it mentions there, you need a viewlets.xml in your theme
    product's generic setup profile.  In this case, there's a bit more
    complexity because the path\_bar isn't registered in the same order
    manager.  So, in your case, you'll want something like this in your
    **viewlets.xml** (hides the old path bar, and inserts it now before
    the global sections [tabs]):

    .. code:: xml

        <hidden manager="plone.portaltop" skinname="My Theme">
            <viewlet name="plone.path_bar" />
        </hidden>
        <order manager="plone.portalheader" skinname="My Theme">
            <viewlet name="plone.path_bar" insert-before="plone.global_sections" />
        </order>

    and you'll need to have something like this in a **configure.zcml**
    file (eg browser/configure.zcml) in order to get it into the
    PortalHeader manager:

    .. code:: xml

        <browser :viewlet
            name="plone.path_bar"
            manager="plone.app.layout.viewlets.interfaces.IPortalHeader"
            permission="zope2.View"
            />

    So, make these updates to your theme product, reinstall, and it
    should be good.

    Also, depending on ordering and what else you have in your theme,
    you might just want to re-order plone.path\_bar to the top of the
    plone.portaltop viewlet.  That'll put it before the PortalHeader
    manager (as you can see in @@manage-viewlets).

.. _here: http://n2.nabble.com/reordering-portal-globalnav--tp3470440p3470440.html
.. _`http://plone.org/documentation/tutorial/customizing-main-template-viewlets/reordering-and-hiding-viewlets`: http://plone.org/documentation/tutorial/customizing-main-template-viewlets/reordering-and-hiding-viewlets
