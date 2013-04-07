Plone, Dexterity, and Incorrect Widgets
#######################################
:date: 2010-06-21 15:09
:author: davidjb
:category: Plone 
:tags: content type, datetime, dexterity, fields, form, plone, problem, product, zope
:slug: plone-dexterity-and-incorrect-widgets

A nice 'gotcha' is the distinction between Zope's schema.Date and
schema.Datetime. The difference is obvious and straightforward when the
two terms are laid out side-by-side: one is for dates only and the other
adds a time component. Where things fell down for me in my usage of
these fields with a Dexterity-based content type in Plone is the human
component. When these fields are mashed in together within a lot of
other text/Python/names, it's easy to miss those 4 little letters of
'time'. This lead me trying to use a DatetimeFieldWidget when I really
could only use a DateFieldWidget. **Wrong widget for the wrong type =
unpredictable.**

When it's all laid out like that, things are clear and simple. When the
small typo has been made, however, things are far less forgiving and
informative. Thankfully, the typo wasn't my fault, but was caused by a
ZopeSkel template for Dexterity (`zopeskel.dexterity`_) so I'm not
kicking myself over it. Essentially, the error message (for those of you
possibly experiencing something similar) is like this:

.. code:: pytb
    
    2010-06-18 16:32:03 ERROR Zope.SiteErrorLog 1276842723.120.730292360531 http://localhost:8080/test/kss_z3cform_inline_validation/validate_input
        Traceback (innermost last):
        Module ZPublisher.Publish, line 119, in publish
        Module ZPublisher.mapply, line 88, in mapply
        Module ZPublisher.Publish, line 42, in call_object
        Module <wrapper>, line 5, in wrapper
        Module kss.core.actionwrapper, line 238, in apply
        Module plone.app.z3cform.kss.validation, line 48, in validate_input
        Module z3c.form.group, line 92, in extractData
        Module z3c.form.form, line 143, in extractData
        Module z3c.form.field, line 302, in extract
        Module z3c.form.converter, line 164, in toFieldValue
        Module zope.i18n.format, line 79, in parse
        Module sre, line 129, in match
        TypeError: expected string or buffer

And the end result of this is that you can't validate fields in your
Dexterity content Add form (eg the above traceback is echoed whenever
you click in/out of a field), nor can you actually save your content.
Unfortunately, even if you were to go hunting through the traceback,
you'd probably end up like me and find that the code is trying to
validate a completely different field than the problematic one. No help
whatsoever.

After going through each of the different fields I had on my content
type, I figured out the cause. If you're hitting a similar issue, check
your widgets. If you're using `zopeskel.dexterity`_, don't worry though.
I checked in a fix for this issue this morning, correcting the widget to
be used. You'll need to use the latest version from the Plone Collective
SVN to make the templates work correctly.

On the other hand, you could look at `collective.z3cform.datepicker`_,
which implements a much more user-friendly Date and DateTime widgets
(using jQuery UI etc).

.. _zopeskel.dexterity: http://pypi.python.org/pypi/zopeskel.dexterity
.. _collective.z3cform.datepicker: http://pypi.python.org/pypi/collective.z3cform.datepicker
