ImportError: No module named BeautifulSoup
##########################################
:date: 2011-08-26 12:02
:author: davidjb
:category: Python
:tags: egg, error, import, packages, python
:slug: importerror-no-module-named-beautifulsoup

Had this issue when you've been trying to run something like
`Funnelweb`_, and you hit an ImportError for BeautifulSoup?  You're
definitely not alone, because I just hit the same issue.  The answer is
simple -- just ensure that you don't use BeautifulSoup 4 or above (this
is still beta) -- it uses a different namespace, specifically bs4. 
Thus, whilst you might have the BeautifulSoup egg satisfying your
dependencies, any imports of this package are going to fail.

For me, I'm using buildout, so I just pinned my version of BeautifulSoup
thusly:

.. code:: cfg 

    [buildout]
    ...
    versions = versions

    [versions]
    BeautifulSoup = 3.2.0

Now, we stop using BeautifulSoup 4.0 and everything works again.

.. _Funnelweb: http://pypi.python.org/pypi/funnelweb
