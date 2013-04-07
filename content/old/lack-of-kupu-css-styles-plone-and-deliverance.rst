(Lack of) Kupu CSS Styles, Plone and Deliverance
################################################
:date: 2010-01-14 14:13
:author: davidjb
:category: Plone 
:tags: css, deliverance, editor, kupu, plone, static, style, theme
:slug: lack-of-kupu-css-styles-plone-and-deliverance

**Note:** see `this post`_ for up-to-date details.

Essentially, the issue is that Deliverance doesn't theme (and rightly
so) the Kupu editor within Plone and hence any styles applied to normal
pages by Deliverance don't show up.  My workaround, as detailed on that
post, is to customise the "emptypageresources" page template and include
a suitable link to the CSS file, like so:

.. code:: html

    <link href="site.css" type="text/css" rel="StyleSheet" tal:attributes="href string:${context/@@plone_portal_state/navigation_root_url}/static/theme/site.css;" />

(changing the tal:attributes section accordingly).  This should
introduce perfectly correct styles for your editor from your Deliverance
(or other) static theme.

This feels to be a very common use case, but I can't seem to find any
other suggestions on a workaround/solution. I'd have to think that this
is likely to be a widespread issue, though. It's definitely not
something that should happen if we're actually able to have the WYSIWYG
editor be WYSIWYG (unlike some other CMS products).

.. _this post: http://www.coactivate.org/projects/deliverance/lists/deliverance-discussion/archive/2010/01/1263439188459/forum_view
