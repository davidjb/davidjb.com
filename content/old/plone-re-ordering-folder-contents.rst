Plone: Re-ordering Folder Contents
##################################
:date: 2009-01-19 16:42
:author: davidjb
:category: Plone 
:tags: batch, folder contents, forms, help, javascript, plone
:slug: plone-re-ordering-folder-contents

Ahhh, a new work week.

The first perplexing puzzle for the week was a seemingly silly idea (it
still is) in Plone where it allows you to view the contents of a given
folder in batches of 20. Now, combine this concept (which is good) with
a concept of being able to re-order items within the folder (which is
good too), you end up with not being able to move items between
'batches'.

Troublesome. There's nothing obvious that you can do aside from
disabling your browser's JavaScript and using the manual buttons. Nope:
not feasible.

Try making your folder view ``/folder_contents?show_all=true``. Batching
is disabled temporarily for the change to be made.

Apparently that's a legitimate fix for a significant problem. Not
terribly elegant, but I'm struggling to think of a better solution.
