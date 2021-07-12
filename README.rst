DavidJB Blog
============

.. image:: https://api.netlify.com/api/v1/badges/b4dcacc7-106c-47ca-ae0b-4ffd2413873a/deploy-status
   :alt: Netlify Status
   :target: https://app.netlify.com/sites/davidjb/deploys

See https://davidjb.com for the live site!

Building
--------

::

    virtualenv . -p python3
    . bin/activate
    pip install -r requirements.txt
    make html

Updating
--------

Netlify automatically builds this for us on push to GitHub.  So, just commit
your changes and push.
