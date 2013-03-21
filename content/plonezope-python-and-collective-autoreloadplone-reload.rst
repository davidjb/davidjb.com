Plone/Zope, Python and collective.autoreload / plone.reload
###########################################################
:date: 2009-11-20 14:34
:author: davidjb
:category: Python
:tags: code, collective, egg, error, package, plone, python, reload, restart
:slug: plonezope-python-and-collective-autoreloadplone-reload

Here's an interesting error message I got stumped with for a good set of
hours.  The issue started with me using collective.autoreload with Plone
and it does the trick, mostly.  With any such 'operation' and live
reloading of code for Python, you've got to expect that not everything
will go according to plan.  Most things do, but one issue I found
presented with this error message:

.. code:: pytb

    < ... huge traceback ...>
    TypeError: super(type, obj): obj must be an instance or subtype of type

The issue arises for me (and you'll probably see it elsewhere) when I go
ahead and modify a Python class that I've extended off from another, and
I'm calling a function from the parent class.  The browser view class
I'm extending from needs to use the same methods but extend the
functionality, so hence me calling super(...).myfunction().   In
hindsight, the error is actually pretty logical -- the "obj" is being
shown to not be a type or subtype of the specified type.  What they
didn't spell out in bright neon letters is that whilst the type I was
working with looks the same in code (it IS the same), having it reloaded
makes it different.

The solution is to restart Zope and go again.  This same thing manifests
in a number of different ways (Error 500 Internal Server Errors for
certain views, etc) but if you're seeing something weird, don't always
assume you've broken something. My favourite thought for the week
applies directly to this:  just because you hear hoofbeats, don't
immediately think zebras.  Being in IT though, it's hard to go straight
for the simplest solution.   Might save you some head-bashing as I've
done it for you. :)

As a side note, it's a similar idea as a network problem I saw the other
day.  The problem could have been solved in 5 seconds by looking at the
lights on the network port, but the "IT solution" was to restart the
computer between OSes and check if the OS was the problem.  Victims of
our own knowledge; we sadly know too much.
