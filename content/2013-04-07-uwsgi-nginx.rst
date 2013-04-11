Serving uWSGI Apps on a Sub-directory with Nginx
################################################

:category: Web
:tags: web, nginx, uwsgi

Serving up uWSGI application using Nginx is super-simple and is configured
effectively like a standard reverse ``proxy_pass``.  However, the documentation
isn't entirely clear exactly how one can correctly serve an application
against a sub-directory -- and have the application know its correct path
such that it can create correct URLs.

Coming from a background of using the Cherokee webserver, uWSGI operated
slightly differently within its configuration.  This behaviour, as best I
know, must have modified the given uWSGI parameters to correctly handle the
sub-directory path.  I haven't looked into it, but it probably just does
the same thing that I configure Nginx to do explicitly.  Anyway, Nginx on 
the other hand operates slightly differently - so in order to have the 
parameters automatically modified, you pass the value ``30`` as ``modifier1``
to uWSGI like so:

.. code:: nginx 

    location /myapp {
        include uwsgi_params;
        uwsgi_pass unix:/opt/myapp.sock;
        uwsgi_param SCRIPT_NAME /myapp;
        uwsgi_modifier1 30;
    } 

(`Pygments`_ has an Ngnix lexer, who knew?)

From the documentation 
http://uwsgi-docs.readthedocs.org/en/latest/Nginx.html#dynamic-apps:

    The ``uwsgi_modifier1 30`` option sets the uWSGI modifier
    ``UWSGI_MODIFIER_MANAGE_PATH_INFO``.  This per-request modifier instructs 
    the uWSGI server to rewrite the PATH_INFO value removing the SCRIPT_NAME
    from it.

There's even more fun reading about the uwsgi protocol over at
http://uwsgi-docs.readthedocs.org/en/latest/Protocol.html but my eyes are
tending to glaze over a bit.  Maybe once I'm more awake.

Either way, just configure the ``SCRIPT_NAME`` correctly to match the 
location path, include the default ``uwsgi_params`` and configure the
``modifier1`` correctly as above.  Reload your configuration and be happy.

.. _Pygments: http://pygments.org/docs/lexers/
