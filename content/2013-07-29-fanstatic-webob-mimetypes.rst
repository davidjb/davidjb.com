All Fanstatic resources being served with 'text/html' mimetype by WebOb/WSGI
############################################################################

:category: Web 

If you're finding that you're using `Fanstatic <http://fanstatic.org>`_ to
serve static resources within your Python-based server process, you may be left
scracthing your head if you suddenly find that resources aren't being served
correctly.  For me, this was manifesting as an incorrect ``Content-Type``
header, always being set to ``text/html`` for any type of static file being
served.  As a side effect, because I'm using `Diazo <http://diazo.org>`_ to
theme my backend Pyramid application, this was automatically seeing this
mimetype being returned to the browser and trying to "theme" the raw files.
The global picture looked like a whole bunch of web fonts that weren't loading
on my end application.

Whoops. There goes a morning.

Solution
~~~~~~~~

Good news - it's easy; it's just a difference between environments on two
different types of hosts.  Deep down under the hood, Fanstatic is serving
files using ``webob.static.FileApp`` and once you know this key piece of
information, it's easy to see that WebOb is using the Python ``mimetypes``
module and its ``mimetypes.guess_type(filename)`` function to lookup
what type a file is.

So, you just need to make sure that the ``mimetypes`` module is able to know
about the extensions you're serving. It uses ``mimetypes.knownfiles`` to look
up locations for finding mime types
(http://docs.python.org/2/library/mimetypes.html#mimetypes.knownfiles).
You'll notice that with the different file locations listed, a different
host with different services installed will know about different mimetypes.
For instance, if you're got Apache or Nginx installed on your host, you'll
probably see their ``mime.types`` file paths in the list, causing your
application to (inadvertently) know about a lot more file extensions.

In case your system is like mine and doesn't know about web fonts, here's what
I've taken to putting into ``/usr/local/etc/mime.types``:

.. code:: python

    image/svg+xml                         svg svgz
    application/vnd.ms-fontobject         eot
    application/x-font-ttf                tff
    font/opentype                         ott
    font/x-woff                           woff
    ... any other file types your system doesn't know about...

and restarting my Python process.  You can confirm if the above worked
by checking using::

    python -c 'import mimetypes; print(mimetypes.knownfiles)'

and also::

    >>> import mimetypes; print(mimetypes.guess_type('foo.woff'))
    ('font/x-woff', None)

to make sure something that isn't ``(None, None)`` returned. 

That's all.  
