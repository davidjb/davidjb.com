DavidJB Blog
============

See https://davidjb.com for the live site!

Building
--------

::

    virtualenv . -p python3.6
    . bin/activate
    pip install -r requirements.txt
    make html

Updating
--------

Netlify automatically builds this for us on push to GitHub.  So, just commit
your changes and push.
