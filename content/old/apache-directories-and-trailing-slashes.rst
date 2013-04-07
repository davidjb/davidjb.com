Apache: Directories and trailing slashes
########################################
:date: 2010-01-18 11:51
:author: davidjb
:category: IT
:tags: apache, directories, folder, http, httpd, problem, web, web server
:slug: apache-directories-and-trailing-slashes

Apache does something interesting (yes, I still
think it's logical) when you're accessing a directory that it's serving:
if you access it without a trailing slash, it'll add one by default.
This makes sense if you're going after some static content or a folder
index (or pretty much any sane usage) but it didn't fit my use case of
serving Plone using rewrite rules in a .htaccess file.

The issue that arises for myself with Plone is that my sites need to
have their access customised through that .htaccess file and that's been
placed within a ``public_html`` directory thus::

    /home/user/public_html/

Because this is a directory, Apache adds that trailing slash by default
when accessing an aliased URL like::

    http://mysite.org/user 

because it's actually pointing to ``/home/user/public_html/``.

I wasn't aware, but you can disable this functionality with just one
line:: 

    DirectorySlash Off

Pages like `this`_ don't help since it's outdated doco for Apache httpd;
they are annoying since it's what came up first in Google. It ended up
being the `latest version`_ of that same doco page that solved it for me
by chance.

As a side note, you apparently need Apache 2.0.51 or later to make this
happen for you.

.. _this: http://httpd.apache.org/docs/1.3/mod/mod_dir.html
.. _latest version: http://httpd.apache.org/docs/2.2/mod/mod_dir.html

