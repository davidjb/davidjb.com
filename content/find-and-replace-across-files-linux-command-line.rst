Find and replace across files - Linux command line
##################################################
:date: 2009-07-06 11:21
:author: davidjb
:category: Linux
:tags: command, find, linux, replace, text, useful
:slug: find-and-replace-across-files-linux-command-line

Today's interesting post concerns finding and replacing terms across
multiple files via a simple command.  Thanks to `this great blog post`_,
it all comes down to one single line.  I had found a previously-useful
line of code, but the problem with that one was the fact that it used
the **find** command.  The problem with that is that if you do a
wildcard search for \* in a directory, it'll give you back '.' as a
result.  Trying to work with that just wasn't happening.

So, without further ado, the command (replacing 'search' with your
search term and 'target' with your replacement term'):

.. code:: bash

    grep -lr -e 'search' * | xargs sed -i 's/search/target/g'

Just remember, the first **grep** command is doing Regex, so escape
anything Regex-y (dots, slashes, etc) or otherwise "prepare for
unforseen consequences" when running **sed**.

.. _this great blog post: http://www.64bitjungle.com/ubuntu/recursively-search-and-replace-terms-in-multiple-files-with-grep-xargs-and-sed/
