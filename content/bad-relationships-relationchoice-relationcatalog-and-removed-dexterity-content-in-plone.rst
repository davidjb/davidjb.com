Bad relationships: RelationChoice, RelationCatalog and removed Dexterity content in Plone
#########################################################################################
:date: 2010-10-26 17:38
:author: davidjb
:category: IT, Work
:tags: borked, dexterity, plone, problem, zope
:slug: bad-relationships-relationchoice-relationcatalog-and-removed-dexterity-content-in-plone

**Disclaimer:** this post isn't giving relationship advice (or..it is in
some twisted way).  Unsurprisingly, removing content in Plone via the
ZMI when Plone says something can't be deleted is likely to cause
problems.

In my case, the fact I removed a Dexterity-based container ("Project")
caused users to no longer add or edit content of my Project type.  The
reason for this boiled down to my use of RelationChoice fields, in order
link Projects to Person objects and vice versa.  The backend storage for
the RelationChoice field is an instance of
``z3c.relationfield.index.RelationCatalog``, and this keeps records of where
the relations are going to and going from.

Now, I created a test Project and some content underneath it.  Due to
some strange KSS errors I was getting on said content, I decided to try
deleting the parent Project.  Plone complained, telling me that the
content couldn't be deleted, and giving the same KSS traceback errors. 
Needing to get rid of the Project, I decided to traipse into the ZMI and
manually delete the Project that way.  I thought I was successful.  I
was, but I caused more problems because the Project I made was still
pointing at a Person object.

Several days later, users began complaining of not being able to add new
Projects or edit existing Project content either.  The traceback looked
like this:

.. code:: pytb

    2010-10-26 13:30:02 ERROR Zope.SiteErrorLog 1288063802.910.831336088181 http://localhost:8080/plone/programs/sample-project/@@edit
    Traceback (innermost last):
      Module ZPublisher.Publish, line 119, in publish
      Module ZPublisher.mapply, line 88, in mapply
      Module ZPublisher.Publish, line 42, in call_object
      Module plone.z3cform.layout, line 64, in __call__
      Module plone.z3cform.layout, line 54, in update
      Module plone.dexterity.browser.edit, line 32, in update
      Module plone.z3cform.fieldsets.extensible, line 59, in update
      Module plone.z3cform.patch, line 30, in GroupForm_update
      Module z3c.form.group, line 138, in update
      Module z3c.form.action, line 99, in execute
      Module z3c.form.button, line 311, in __call__
      Module z3c.form.button, line 170, in __call__
      Module plone.dexterity.browser.edit, line 21, in handleApply
      Module z3c.form.group, line 117, in applyChanges
      Module zope.event, line 23, in notify
      Module zope.component.event, line 26, in dispatch
      Module zope.component._api, line 130, in subscribers
      Module zope.component.registry, line 290, in subscribers
      Module zope.interface.adapter, line 535, in subscribers
      Module zope.component.event, line 33, in objectEventNotify
      Module zope.component._api, line 130, in subscribers
      Module zope.component.registry, line 290, in subscribers
      Module zope.interface.adapter, line 535, in subscribers
      Module z3c.relationfield.event, line 82, in updateRelations
      Module zc.relation.catalog, line 546, in unindex
      Module zc.relation.catalog, line 556, in unindex_doc
      Module zc.relation.catalog, line 622, in _remove
    KeyError: 128268893

These errors were strange, because the KeyError was different every
time. After several hours of delving through code, it was clear that the
ZC relation catalog was expecting a given key but not finding it (as the
traceback suggests). After poking around in the RelationCatalog's
storage, there were a variety of references sticking around that
involved the old Project that I'd deleted. I hacked in a:

.. code:: python

    print [x.from\_object for x in sorted(catalog.findRelations({}))]

at line 84 of ``z3c/relationfield/event.py``, and it showed references
to objects that no longer existed.

Trying to use the ``removeRelations`` method of
``z3c/relationfield/event.py`` isn't useful, because that swallows up
the same KeyError, so in order to remove the borked relations, it would
have to be done manually. That said, the underlying storage for the
RelationCatalog goes over my head.

So, due to time constraints, I resolved my issues by using the catalog's
"clear" method to remove all records. Easily done by inserting:

.. code:: python

    catalog.clear()

at line 84 of ``z3c/relationfield/event.py`` (and removing
after I edited a Project and invoked said code). Clearing the catalog
didn't break any of relations for my content, and everything's now
re-indexed after each Project was edited and saved again.

**Word to the wise:** if you're working with this sort of tech, figure
out why you can't delete something and solve that, rather than hacking
away. It will come back to bite you. Let me know if you've fixed a
similar issue without needing to clear the catalog.
