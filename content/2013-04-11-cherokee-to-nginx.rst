Switching to Nginx from Cherokee: Why
#####################################

:category: Web
:tags: Nginx, Cherokee, web, web servers

After a switching away from Apache some time ago, our primary web server
had been running `Cherokee <http://cherokee.github.io/>`_ for quite a while
- since September 2011, in fact, looking back at the configuration history.
More recently, however, I've switched us again.  This time to `Nginx
<http://nginx.org>`_ - with impressive improvements in performance and
configurability (10x for some static files) -- and reliability.

.. note::
   See my `technical guide
   <|filename|2013-04-12-cherokee-to-nginx-technical.rst>`_ for technical
   info about switching.

Background
~~~~~~~~~~

Originally, the selection of Cherokee as web server software looked
promising - the Cherokee project had been around for a while, was gathering
support, had a reasonable level of uptake, and consistent, active
development.  All promising signs.  It also had a variety of novel features
at the time - flexible conditional rules, an app marketplace (something it
no longer has, but I'll come to this shortly), a GUI for configuration, and
was very *shiny* for want of a better word.  In terms of performance, it
had outdone the other options, so I went through the rather tedious process
of rebuilding the configuration from Apache into Cherokee.  Something that
took a rather long time. That set up served us well, despite a few issues -
ongoing or otherwise - for the last 18 months.

However, as with many software projects, times do change.  I began to be
somewhat concerned with the project when its lead developer (and copyright
holder) decided to pursue other interests, leaving the project in somewhat
of a state of flux. Community support has wavered through this time, bug
reports left to be ignored, and development slowed to a near stand-still.
Hoping to not give up Cherokee just yet, I even contributed a number of
significant fixes (well, I'd define them such) for things like correcting
HTTP method handling, correcting timeout handling, fixing tests, and more.
I suppose needing to do this probably should have been a concern in itself,
but I enjoy open source development -- and someone needs to fix those
issues.  Other things like lacking an official release process, complete
lack of interest from package maintainers in Debian/Ubuntu/EPEL, and more,
fuelled my concerns further.

More recently, there's been a bit of renewed interest from several
developers, but with the number of issues present in the 100s, a disjointed
experience from website to release process to issue tracking, and little
uptake across the web these days (see
http://w3techs.com/technologies/overview/web_server/all), I foresee a lot
of work needed by a lot of people.  I'm sure some out there that are still
using Cherokee may disagree with what I write - yes, the project still has
some interest about it - but I believe my concerns are valid.  I'm also not
trying to disparage the Cherokee project itself either - it's had a tough
life and I can appreciate that - but after my experiences, I don't feel
that it is a good fit any longer, and I can't devote any more of my time to
it.

Why Nginx
~~~~~~~~~

Technical issues aside for now, looking at a page like
http://nginx.com/company.html, it makes me a little more comfortable in the
fact those companies are surely contributing back to the development.  Even
if not from the perspective of money, but by simply running Nginx in
production, they'll be identifying basic issues well, well before I even
know about them.  According to those statistics above, almost 16% of the
web uses Nginx.  That's a bigger user base, support base, better security,
*money* and given overall usage - this is possibly most important - a
guarantee of needing to keep up with new web technologies.  I just don't
see Cherokee being able to keep up in any of these aspects, so hence the
switch to Nginx was a logical one.

In addition, from my dev-ops perspective, Cherokee and Nginx are very
similar, so it's not like I'm stepping back to Apache.  They work - to the
best of my knowledge - on a very similar event-driven set of principles and
during my configuration conversion, found they're configured almost
identically in some cases. Nginx does what I've come to like of Cherokee
(speed, certain modules, functionality, and so forth), but with benefit of
a wider community behind it.  It doesn't have a shiny GUI, but the
simplicity of its configuration means it doesn't need one in my opinion.
Separately, Nginx isn't nearly as long lived as Apache, but I'm sure it
won't have trouble sticking around for that long. 

Conclusion
~~~~~~~~~~

In short, in running a production-grade system, you want to be focused on
actually being able to deliver a service, and not having to watch over your
shoulder every moment out of fear that your service will fall over.  An
issue like this: https://github.com/cherokee/webserver/issues/952 is *not*
something I want to have to think about again, if I can at all help it.

So farewell Cherokee, and hello Nginx.

**Note**: My next post will be the technical side of the configuration
changeover.
