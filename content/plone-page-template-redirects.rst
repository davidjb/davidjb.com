Plone: Page Template Redirects
##############################
:date: 2008-11-25 11:38
:author: davidjb
:category: Plone
:tags: edit, hack, javascript, plone, redirect, template
:slug: plone-page-template-redirects

Was wondering how to get a Plone page template to go to a page before the template actually loads. Now, actually getting Plone to not go to this template would be FAR better, but since we can’t actually modify the functionality of the Favourites content items in the content listings (not easily), I instead modify it’s default view.

Using this:

.. code:: html

    <head>
        <metal:js fill-slot="javascript_head_slot">
            <script type="text/javascript"
            tal:content="python:'location.href=\''+portal.absolute_url()+'/'+here.remoteUrl+'\';;'">
            </script>
        </metal:js>
    </head>

We see that the page reloads to the relevant location as soon as the
head JavaScript is done loading.

Easy, quick, useful, hack-y. More to come for Plone.
