Plone and Dexterity: Working with computed fields
#################################################
:date: 2010-04-19 14:03
:author: davidjb
:category: Plon 
:tags: computation, content, dexterity, extension, function, plone, product, python
:slug: plone-and-dexterity-working-with-computed-fields

Today, we're looking at how to utilise computed fields within a
Dexterity-based content type. The specific use-case is that of having
two separate fields (first name and surname, for a Person type, for
example) generate the complete object title. The first part of this --
having the title of the content displayed correctly -- is pretty
straight forward once you know what documentation to read and understand
how things happen. The second part -- having the ID of the content
correctly generated to be first name/surname is slightly more
complicated.

Title computation and display
-----------------------------

Let's look at the first part.  What we need is a custom content class,
and this is documented in the `Dexterity Developer Manual`_.  As per the
documentation, you need to create a class and derive it off from either
Item or Container, depending on what your content originally is.  Then,
specify your new class as the 'klass' in your relevant type XML file in
your GenericSetup profile.

Now, with an empty class definition, like in the manual page, you can
start to add your computed fields. Your class might look something like
this (don't worry, I'll explain):

.. code:: python

    class Person(Item):
    """Customised Person content class"""
        @property
        def title(self):
            if hasattr(self, 'first_names') and hasattr(self, 'surname'):
                return self.first_names + ' ' + self.surname
            else:
                return ''

        def setTitle(self, value):
            return

So, we have our relevant function defined and decorated to be a
property. I've found that in at least this specific use-case (setting
the title from other fields), that this method is getting called before
the object's fields are instantiated. Hence the presence of the hasattr
checks.

Now, having a setTitle function seems a bit odd yes? Especially so since
it doesn't do anything meaningful at all. Odds are that you probably
won't need this type of function *unless* you're like me and needing to
set the **title** specifically. The reason you need it for the title
attribute is because you've got "def title(self)" as a function and your
default DublinCore functionality (called by Dexterity @
plone.dexterity.content, line 221, in \_\_init\_\_) attempts to
initialise the title, amongst other DC metadata. Interesting!

So, without a setTitle function, attempting to create a new instance of
your content fails with a "AttributeError: can't set attribute" error
because DC (Module Products.CMFDefault.DublinCore, line 369, in
setTitle) wants to set the title. Sorry, it can't do this (we don't want
it to, and it physically can't), so we override what would be the
default setTitle function to do nothing at all.

Correct ID at creation time from computed title
-----------------------------------------------

Now, this one's a little trickier. Unfortunately, there's no
documentation that I could find on the web about doing this, save a
`very short thread`_ on Nabble. In that thread, Martin Aspeli provides
some good pointers to this very use-case, but the example of
INameFromTitle provides the title as a field, rather than a function
(and isn't specifically registered as an adapter).

After a bit of poking and prodding, here's my solution:

.. code:: python

    from plone.app.content.interfaces import INameFromTitle
    class INameFromPersonNames(INameFromTitle):
        def title():
            """Return a processed title"""

    class NameFromPersonNames(object):
        implements(INameFromPersonNames)

        def __init__(self, context):
            self.context = context

        @property
        def title(self):
            return self.context.first_names + ' ' + self.context.surname

So, we extend off from the default functionality, making sure that our
title function is going to override the title field that's in
INameFromTitle by default. Then, we create our adapter and return the
processed title (function decorated as a property). No need for hasattr
checks here; the object is already initialised.

Then, register this in some ZCML, where the 'for' is the Dexterity
interface class and the latter two attributes are the classes we just
specified:

.. code:: xml

    <adapter for="sample.project.person.ISamplePerson"
        provides="sample.project.person.INameFromPersonNames"
        factory="sample.project.person.NameFromPersonNames"
        />

Then, the magic of inheritance takes over and the relevant code that
would normally generate the ID off from the title field comes from the
processed title. Tada!

Conclusion
~~~~~~~~~~

Put all these things together with Dexterity and that's it. I'm still in
the process of doing this, but you should be able to apply the same
processes to other fields. Just watch out for DublinCore initialisation.
If you see that sort of error message about a setXXX function and
attribute, then you'll know what to do.

**Note to self:** the reason I didn't use a behaviour here is because
things like INameFromTitle give us a field (see source file). We don't
want this, but rather just programmatic generation of the title.

.. _Dexterity Developer Manual: http://plone.org/products/dexterity/documentation/manual/developer-manual/advanced/classes
.. _very short thread: http://n2.nabble.com/Dexterity-computed-fields-td3498400.html
