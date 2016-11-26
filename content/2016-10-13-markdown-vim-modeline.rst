Adding a Vim modeline in a Markdown document
############################################

:category: Tech

A short tip: Markdown doesn't have any form of official or non-printable
markup in its language definition (that I could `ascertain`_) so adding a Vim
modeline into a document needs a little bit of massaging.  You could include
the modeline inside a HTML comment, but the better option that I found was to
do this at the end of the document:

.. code-block:: markdown

   [modeline]: # ( vim: set fenc=utf-8 spell spl=en: )

This uses the link label syntax to establish a link called ``modeline``, point
that at the URL of `#`, and then use the title of that fake link to set our
Vim modeline, following the modeline syntax and appropriate spacing and
colons.

That's it. Hopefully this saves you some thinking.

.. _`ascertain`: https://stackoverflow.com/questions/4823468/comments-in-markdown
