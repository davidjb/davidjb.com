Shibboleth SP logo.jpg missing from distributions
#################################################

:category: IT
:tags: Shibboleth


Have you recently installed the Shibboleth SP software and found that
the error pages the software is generating are missing the Shibboleth logo?
If so, it's because those error pages are attempting to display a logo
(typically ``/shibboleth-sp/logo.jpg`` by default) but the logo of the Griffin
that you may have been used to seeing is no longer distributed with the
software.  

Unfortunately, this change doesn't appear to be documented (yet),
but is highlighted in this discussion: http://shibboleth.1660669.n2.nabble.com/Shibboleth-logo-in-Red-Hat-RPM-tp7583386.html

More or less, the reasoning given is that the Shibboleth project doesn't
want default error pages out there in the wild making the project or
technology itself look bad.  Fair enough, but my suggestion is to make this
clear to users of the SP software so they don't need to go and hunt down
a mailing list post to see why.

At any rate, to make sure your error pages don't display a nasty broken
image, configure your ``shibboleth2.xml`` file like so:

.. code:: xml

    <ApplicationDefaults>
        ...
        <Errors supportContact="my.email@example.com"
                logoLocation="/shibboleth-sp/logo.png"
                styleSheet="/shibboleth-sp/main.css" />
        ...
    </ApplicationDefaults>

and make sure that your web server is serving that given location correctly and
that said logo file actually exists.  Alternatively, you can use a full URL to
a logo and stylesheet if you're so inclined.
