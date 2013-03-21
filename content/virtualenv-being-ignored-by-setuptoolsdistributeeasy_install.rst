Virtualenv being ignored by setuptools/Distribute/easy_install
##############################################################
:date: 2012-08-24 13:41
:author: davidjb
:category: Python
:tags: distribute, easy_install, virtualenv
:slug: virtualenv-being-ignored-by-setuptoolsdistributeeasy_install

This one couldn't be simpler, but it's worth noting all the same.  I've just
experienced a situation where a `virtualenv`_  was being completely ignored by
all tools even though it was absolutely activated via ``source bin/activate``. 

The answer was to blow away the ``lib`` directory within the virtualenv and
blow away the local Python interpreter at ``bin/python`` and re-create the
virtualenv. After deactivating and re-activating, everything works correctly
again.

I guess something in the environment (or env variables) got messed up.
Who knows; it works now.

.. _virtualenv: http://www.virtualenv.org/en/latest/index.html
