Plone: Ploneboard Conversation Editing
######################################
:date: 2008-11-27 11:40
:author: davidjb
:category: Plone
:tags: conversation, editing, plone, ploneboard, python, redirection, script
:slug: plone-ploneboard-conversation-editing

I'm back with even more Plone goodness. Turns out Ploneboard has a
problem/issue (well, HAD an issue until I went and edited the code on
the SVN repository for the Collective of Plone. Read: will not have in
the next major release) with redirecting the user after they go and edit
a post. So essentially the user ends up getting to a page that says
'Insufficient privileges', which is was extremely odd considering I do
everything as an admin.

The fix goes a little something like this:

In ploneboard\_scripts/comment\_redirect\_to\_conversation change it to
be:

.. code:: python

    # XXX if we ever do batching, we need extra logic here.
    redirect_target = context.getConversation()
    anchor = context.getId()

    response = context.REQUEST.get('RESPONSE', None)
    if response is not None:
    response.redirect('%s#%s' % (redirect_target.absolute_url(), anchor))
    print "Redirecting to %s" % redirect_target.absolute_url()
    return printed


Originally, the user was attempted to be sent to some other view that
they couldn't access. Now, they just get sent to the conversation. No
tricks, just the conversation.

More Plone on the way!
