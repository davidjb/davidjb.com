Plone: URL Encoding In A Script
###############################
:date: 2009-01-30 08:46
:author: davidjb
:category: Plone 
:tags: adapter, form, plone, ploneformgen, python, quote, url
:slug: plone-url-encoding-in-a-script

So, for today's problem, how can we get a URL (specifically the GET
request arguments) suitably encoded? Easy, if we're talking about a
Python script that lives on the file system and can be used within
Zope/Plone that way. But what about some sort of Python script that has
to exist on the Plone site (specifically, creating a PloneFormGen (PFG)
Custom Adapter)?

First thing I jumped to is urllib and urlecode: but no luck because
you're unauthorised to import the library in your script. Boo!

After much poking, and Googling for something that I thought should be
simple, I found this:

.. code:: python

    from Products.PythonScripts.standard import url_quote_plus

Does exactly what it says and what it should, and no security issues.
There's also ``url_quote`` which produces ``%20`` instead of ``+``.
