Python eggs and missing files (like 'docs')
###########################################
:date: 2011-01-06 11:57
:author: davidjb
:category: Python 
:tags: build, docs, egg, file, install, missing, problem, python
:slug: python-eggs-and-missing-files-like-docs

This is pretty trivial (and trivial to fix), but I'm chronicling it for
my knowledge as much as anyone else's.  The issue is that a given Python
egg is missing some form of files, most commonly the 'docs' directory in
my experience, because the build wasn't configured correctly.

The error goes somewhat like this:

.. code:: pytb

    Getting distribution for 'my.theme'.
    error: docs/HISTORY.txt: No such file or directory
    An error occured when trying to install my.theme 1.5.0. Look above this message for any errors that were output by easy_install.

The solution is simple: just add the relevant missing directories or
similar into your ``my.theme/MANIFEST.in`` file, so the end results
looks like so:

.. code:: ini

    recursive-include docs *
    recursive-include my *
    global-exclude *py[co], *mo

where ``my`` and ``docs`` are the top-level packages I need.

Just rebuild the Python egg and away we go. As I said, simple fix. Now
just have to get it stuck in my head to remember.
