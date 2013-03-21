Plone: Plone4Artists Video - Can't Edit Videos
##############################################
:date: 2009-02-25 09:01
:author: davidjb
:category: Plone 
:tags: p4a, plone, plone4artists, problem, subtyped, video
:slug: plone-plone4artists-video-cant-edit-videos

Wow..I just keep hitting these problems. The latest issue is chronicled
here: http://dev.plone4artists.org/pm/p/plone4artists/ticket/160

which essentially boils down to this problem when you try and edit a
video subtyped File from p4a.plonevideo (or p4a.video or whatever it's
called now):

.. code:: pytb

    Traceback (innermost last):
    * Module ZPublisher.Publish, line 119, in publish
    * Module ZPublisher.mapply, line 88, in mapply
    * Module ZPublisher.Publish, line 42, in call_object
    * Module zope.formlib.form, line 769, in __call__
    * Module p4a.video.browser.video, line 362, in update
    * Module Products.Five.formlib.formbase, line 55, in update
    * Module zope.formlib.form, line 732, in update
    * Module p4a.video.browser.video, line 367, in setUpWidgets
    * Module zope.formlib.form, line 393, in setUpEditWidgets
    * Module zope.formlib.form, line 323, in _createWidget
    * Module zope.component._api, line 103, in getMultiAdapter
    ComponentLookupError: ((<p4a .fileimage.file._field.FileField object at 0x15ce2610>, <httprequest , URL=[snip].mp4/atct_edit>), <interfaceclass zope.app.form.interfaces.IInputWidget>, u'')

And so, after much painful searching and confusion, it's just simply an
issue of including ``p4a.fileimage`` in the ZCML section of your
instance in your buildout.

Wow..back to work (finally).

