uWSGI and libxml2 conflicts (aka Installing uWSGI with a custom libxml2)
########################################################################

:category: Web
:tags: uWSGI, libxml2, xml-config
    
If you're using uWSGI with XML support (this is its default), then it will
be requiring you to have ``libxml2`` installed -- or something similar that 
provides ``xml-config``.  What you'll find is some erratic behaviour (or
complete failure) when attempting to serve an application that is also 
relying on ``libxml2``, but a different version.  

In my case, my original uWSGI was built with CentOS 5's stock ``libxml2``
library, but my Python application was using ``lxml``, built with a custom
version of ``libxml2`` (via Buildout with the `z3c.recipe.staticlxml
<https://pypi.python.org/pypi/z3c.recipe.staticlxml>`_ recipe, in case you
were curious).  Because of these two versions being different, some odd 
errors took place when ``lxml`` was being imported within my application.

Unfortunately, I don't have the full details of these errors, but suffice
to say that ``lxml``'s XSLT functionality couldn't be imported or else 
used successfully without errors like ``lxml.etree.XSLTApplyError``,
``undefined symbol: xmlXPathCompiledEvalToBoolean``, or::

    File "xslt.pxi", line 596, in lxml.etree.XSLT.__call__ (src/lxml/lxml.etree.c:139974)
    lxml.etree.XSLTApplyError: Unregistered function

The errors were strange, and inconsistent as I tried to switch between
different versions of ``libxml2``.

Installing uWSGI with the same libxml2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Good news!  It's easy to ensure that your uWSGI gets compiled using the same
``libxml2``.  You just need to ensure that your ``PATH`` environment variable
is configured correctly before installing -- so, you'll need to ensure that
your custom ``xml-config`` is found before any others.  

.. code:: bash

    export PATH=/opt/buildout/parts/lxml/libxml2/bin:$PATH
    #Do your uWSGI install
    pip install uWSGI
    #or
    ./bin/buildout
    #etc

In my case, I'm using Buildout, so whilst the above path didn't initially
exist, it gets created and installed during the Buildout process.
Alternatively, it is possible to use something like
``collective.recipe.environment`` for Buildout to do this environment setting
for you, in case you are using Buildout.

I'm looking into getting the way I'm installing uWSGI with Buildout,
``buildout.recipe.uwsgi``, to accept customisation for a build option like
this.  Stay tuned for more.

