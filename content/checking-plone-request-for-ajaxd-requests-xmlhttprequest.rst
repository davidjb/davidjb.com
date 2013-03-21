Checking Plone REQUEST for Ajax'd requests (XMLHttpRequest)
###########################################################
:date: 2011-01-07 10:54
:author: davidjb
:category: Plone 
:tags: ajax, fields, form, http, pfg, plone, request
:slug: checking-plone-request-for-ajaxd-requests-xmlhttprequest

Recently, I've needed a PloneFormGen (PFG) form of mine to have certain
fields excluded when the form is displayed in one of Plone 4's fancy
popups.  At the same time, I need this field to still persist within the
'standard' view of the form.  It's the request object to the rescue, and
all I've had to do is insert this TALES expression against the *Enabling
Expression* for my PFG field:

.. code:: python

    python:request.environ.get('HTTP_X_REQUESTED_WITH') != 'XMLHttpRequest'

and the end result is that unless the request is one of XMLHttpRequest,
then we'll show the field.

Shouldn't be any reason this same TALES couldn't be applied in a page
template against XHTML, or elsewhere.
