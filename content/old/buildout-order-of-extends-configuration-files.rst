Buildout: order of 'extends' configuration files
################################################
:date: 2011-01-06 15:00
:author: davidjb
:category: Python 
:tags: buildout, config, dexterity, extends, ordering, plone
:slug: buildout-order-of-extends-configuration-files

Yet another word to the wise: take care of your ordering of the
'extends' configuration files within your buildout.  It makes complete
sense, and especially so with respect to version pinning: the later
configuration's versions will be the last one applied.

So, it makes a lot of sense (in hindsight!) that this configuration, and
the fact I have version pins in my base.cfg, isn't going to end well:

.. code:: ini

    [buildout]
    extends = 
        base.cfg
        http://good-py.appspot.com/release/dexterity/1.0b2

The Dexterity version pins are going to override the ones I have in my
base.cfg.  This ends up meaning that Plone 4's version pins get applied
first (Plone's main cfg is included in my base.cfg), then my 'custom'
pins in base.cfg, then Dexterity's over the top.  Any custom pins I had
for packages used in Dexterity's KGS just got squashed.

Essentially, if it looks like Buildout isn't paying attention to your
package pins, it's not because it's being disobedient, it's likely
because something's overriding your settings.
