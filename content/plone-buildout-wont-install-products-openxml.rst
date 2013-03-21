Plone: Buildout Won't Install Products.OpenXml
##############################################
:date: 2008-12-22 14:59
:author: davidjb
:category: Plone
:tags: buildout, libxml, openxml, plone, problem, products, xml
:slug: plone-buildout-wont-install-products-openxml

**UPDATE:** Installation of Products.OpenXml appears to work happily
with buildout when I'm using z3c.recipe.staticlxml to build lxml
separately from having to easy\_install or install system-wide packages.

So it's almost Christmas time and I'm still slaving away working. It's
all about commitment.

Today in my life I've been trying to install the OpenXml product for
Plone (using buildout, of course)::

    david@computer:~/buildout/instance$ ./bin/buildout
    Uninstalling zopepy.
    Uninstalling instance.
    Updating plone.
    Updating zope2.
    Updating productdistros.
    Installing instance.
    Getting distribution for 'Products.OpenXml'.
    Got Products.OpenXml 1.0.1.
    Getting distribution for 'openxmllib'.
    Got openxmllib 1.0.3.
    Getting distribution for 'lxml>=1.3.0,&amp;lt;2.0.0dev'.
    Building lxml version 1.3.6
    ERROR: /bin/sh: xslt-config: not found
    ** make sure the development packages of libxml2 and libxslt are installed
    **ERROR: /bin/sh: xslt-config: not found
    ** make sure the development packages of libxml2 and libxslt are installed
    **ERROR: /bin/sh: xslt-config: not found

And then 50,000 errors follow, making this message hard to find. Either
way, the end result was that lxml wasn't able to install.

**Solution:** install libxslt and its dev counterpart plus the relevant
Python bindings on your system. In Ubuntu 8.10, that's libxslt1.1,
libxslt1-dev, and python-libxslt1.

All good now.

**Update:** Turns out Centos 5 (Red Hat) is has different package names.
Try ``yum install libxslt libxslt-devel libxslt-python`` as root for
Centos.

**Future response:** Just use `z3c.recipe.staticlxml
<https://pypi.python.org/pypi/z3c.recipe.staticlxml>`_ and be done with it all.
No need for system level packages and it all just works.
