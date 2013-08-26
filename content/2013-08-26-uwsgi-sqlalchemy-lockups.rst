uWSGI and Database Lockups with SQLAlchemy
##########################################

:category: Web

If you're running a Python-based web application and using SQLAlchemy as your
database integration layer (as an ORM or otherwise), you may also be using
uWSGI to act as the application container.  

If you try and fire up multiple processes to handle greater load coming in
with the uWSGI option ``--processes`` (or ``-p``, ``--workers``; or uWSGI's
various configuration mechanisms), then you'll probably find that after a
short time, your web application will lock up and refuse to serve requests.
For me, this was between 1 and 10 requests with using the ``cx_Oracle``
database adapter against an Oracle server backend.  So, extremely quickly.

Don't blame your database like I did. The issue is that this combination of
SQLAlchmey and cx_Oracle (I think I should blame this more), doesn't
work well with multi-process environments.  The documentation says multi-threading is supported, but I'm really not sure what the underlying issue is here.
If someone's got the time to investigate, please let me know.

The solution is easy: use the ``--lazy`` option with uWSGI 0.9.8+.  uWSGI
will create *independent* workers that only share the initial uWSGI socket,
thus keeping things entirely separate.  Because of this extra overhead, you
will find that extra memory, resources, and the like will be consumed, but
your application will work.  Resource overhead is probably acceptable, but
YMMV.  There are actually a number of other options detailed at
http://lists.unbit.it/pipermail/uwsgi/2011-May/002079.html but this one was
the simplest for me and completely avoids needing to mess with any internals
of any of my code.

uWSGI plug
~~~~~~~~~~

If you're not using uWSGI, maybe you should have a think about it -- it's
pretty easy to configure any existing application and not necessarily just
Python applications, and in my experience, just switching to `uWSGI <http://uwsgi-docs.readthedocs.org/>`_ will reduce the overhead between your web
server (Nginx, anyone?) and your backend application.  This means faster
responses versus perhaps running a HTTP reverse proxy - in some rough tests,
my applications improved 25%+ just from this simple change.

In-built load balancing, multi-process handling, multi-language serving,
improved performance, and support for hundreds of options makes it an excellent
tool.  You should definitely check it out.
