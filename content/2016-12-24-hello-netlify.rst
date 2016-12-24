Static sites, continuous deployment and HTTPS with Netlify
##########################################################

:category: Tech
:tags: web, security, blog

I've been doing a variety of things pertaining to web security in recent weeks
and one thing that's been gnawing at my brain is the fact that my blog could
*still* only use insecure ``http://`` because of GitHub Pages.  My blog's
content was using GitHub Pages for its serving and ``gh-pages`` really hasn't
been seeing a lot of love - that I know of - since its inception a few years
back, especially since the development of concepts like Let's Encrypt with
free SSL certs for the web.

I felt I probably should have taken a more active role, perhaps running my own
server and all that, but I really don't want one more vector to have to
secure.  So, I asked around.  Turns out the fantastic (not paid to say it)
`Netlify <https://www.netlify.com/>`_ offers hosting for static sites, with
continuous deployment support and HTTPS from Let's Encrypt...for free.

After a short stint stabbing around in the documentation, I set about
rewriting my blog installation setup to use ``requirements.txt`` for Python
over using Buildout, thus greatly simplifying my blog setup.  The significant
upshot of having continuous deployment is now I can edit content on GitHub
from any platform and have my blog auto-rebuild itself through the magic of
webhooks.  GitHub notifies Netlify and they rebuild and publish. That's great
-- I no longer need to be the man-in-the-middle, rebuilding and shuttling my
blog's HTML to different places -- I just push reStructuredText and that's
that.

The blog and site are now HTTPS-only after a couple of quick corrections to
the naive HTTP-only blog theme I was running.  Easily solved with
find-and-replace.

If you're still running a HTTP website, it's time to make the switch.
