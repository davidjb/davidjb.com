Plone: PloneFormGen Customisations
##################################
:date: 2009-01-12 16:39
:author: davidjb
:category: Plone 
:tags: authenticator, changes, forms, plone
:slug: plone-ploneformgen-customisations

Another fun problem for me to address today: upgrading to the latest
version of Plone (3.1.7 at time of writing) caused my custom
PloneFormGen (otherwise known as PFG) view to break in a nasty way:

.. code:: pytb

    Module None, line 13, in fgvalidate_base
    - <fscontrollervalidator at /site/fgvalidate_base used for /site/registration-form>
    - Line 13
    Module Products.PloneFormGen.content.form, line 519, in fgvalidate
    Module plone.protect.authenticator, line 60, in check
    Forbidden: Form authenticator is invalid.

Obviously there's some new validation code for forms in Plone 3.1+.
Thanks to a very simple (and useful!) blog entry:
`http://www.die-welt.net/index.php/blog/239/Upgading\_forms\_in\_Plone\_3`_
, the solution is to add:

.. code:: html

    <input tal:replace="structure context/@@authenticator/authenticator" />

somewhere in the form.

.. _`http://www.die-welt.net/index.php/blog/239/Upgading\_forms\_in\_Plone\_3`: http://www.die-welt.net/index.php/blog/239/Upgading_forms_in_Plone_3
