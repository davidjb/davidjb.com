Serving TileStache (or another app) using uWSGI against a web sub-directory
###########################################################################
:date: 2012-06-01 12:41
:author: davidjb
:category: Python 
:tags: application, python, serving, uwsgi, web, wsgi
:slug: serving-tilestache-or-another-app-using-uwsgi-against-a-web-sub-directory

`uWSGI`_ is extremely promising as an application server given its huge
range of options and supported platforms.  For me, however, just getting
something seemingly simple up and running successfully was relatively
confusing. I'd like to contribute to the documentation when I can, but
thought a dedicated page about `TileStache`_ as a specific application
(and associated configuration) was warranted. It does make more sense
now, thankfully.

I want to serve my TileStache application at http://mydomain.com/tiles
(taking careful note of the sub-directory present). I've chosen an
INI-style configuration for my instance and here's what the final result
looks like (loads using ``uwsgi --ini my_uwsgi.ini``):

.. code:: ini

    [uwsgi]
    processes = 8
    vacuum = true
    master = true
    socket = %(home)/var/uwsgi.sock
    home = /opt/tilestache
    mount = /tiles=app.py
    need-app = true

The available options for uWSGI are extremely comprehensive and fairly
bewildering for someone just starting off. The main issue I faced was
the fact the *--module* option doesn't support argument passing. This
was a big one because documentation like `this`_ shows empty rounded
brackets and the programmer in me instinctively thought of this as an
Python object call. Not so. In order to pass arguments, you either need
*--eval* or to do what I did and create a separate file and mount that.
Where I have *app.py* specified above, this is the definition for said
file:

.. code:: python

    import TileStache
    application = TileStache.WSGITileServer('tilestache.cfg')

So that's uWSGI serving TileStache. The final issue to solve is that of
serving against a sub-directory. Once you have your application mounted
against the relevant mount point (in my case */tiles*), then it's just a
case of telling uWSGI to use this as its **SCRIPT\_NAME** environment
variable.

For me, this was telling our webserver (Cherokee) to provide the
**UWSGI\_SCRIPT\_NAME**, ensuring the **UWSGI\_** is prepended, as a custom
environment variable against the relevant Directory behaviour. Once
Cherokee was pointed at the relevant socket and restarted, everything
'just worked'. In the case of other web servers like Nginx, it would be
a case of configuring a location with:

.. code:: ini

    uwsgi_param SCRIPT_NAME /tiles;

And there you have it.

.. _uWSGI: http://projects.unbit.it/uwsgi/
.. _TileStache: http://tilestache.org
.. _this: http://projects.unbit.it/uwsgi/wiki/Quickstart
