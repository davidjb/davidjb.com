User IDs show as comment authors in Plone 4.x after migration from plone.app.discussion
#######################################################################################
:date: 2011-11-01 13:18
:author: davidjb
:category: Plone 
:tags: collective, comments, discussion, docs, documentation, fix, plone
:slug: user-ids-show-as-comment-authors-in-plone-4-x-after-migration-from-plone-app-discussion

If you've migrated your site from earlier versions of Plone to the
latest ones in the 4.x series, or else have started using
plone.app.discussion earlier than that, you might have come across a
situation where comments on your site show user IDs as authors rather
than a user's full name. If you see this anywhere, chances are your
comment's migration didn't go according to plan, and that the Creator
information didn't get recorded correctly on the comment.

I've just written this on the Collective developer docs:
`http://readthedocs.org/docs/collective-docs/en/latest/misc/upgrade.html#fixing-creator-details-on-existing-comments`_

The script there should help by stepping through all comments on your
site and fixing up the creator details as required. As mentioned in the
comments beneath the script, the mileage you get may vary depending on
the state of your comments. I found half my site's comments were fine
and half weren't. Some of mine had no author name, email, or user ID in
the relevant fields, and the script there checks for these (and the
actual existence of a user after looking up what's in the Creator
property), so that should be enough to sanity-check so it won't stomp
over correct comments.

That said, if for some reason, you happened to have a user with ID
*david* and full name of *Administrator*, also had a user with the ID of
*Administrator*, and had a comment which had an incorrect *Creator* but
did have the three fields of *author\_username*, *author\_name*, and
*author\_email*, then it won't affect those comments and you might just
have to manually fix them up.

.. _`http://readthedocs.org/docs/collective-docs/en/latest/misc/upgrade.html#fixing-creator-details-on-existing-comments`: http://readthedocs.org/docs/collective-docs/en/latest/misc/upgrade.html#fixing-creator-details-on-existing-comments
