AttributeError: 'NoneType' object has no attribute 'items': Can't upgrade Plone 3 to 4.x
########################################################################################
:date: 2011-09-14 08:57
:author: davidjb
:category: Plone
:tags: 4.1, plone, plone 4, traceback, upgrade
:slug: attributeerror-nonetype-object-has-no-attribute-items-cant-upgrade-plone-3-to-4-x

You may have seen an error like the one below when you've gone to
upgrade your Plone site to something in the Plone 4.x series from Plone
3:

.. code:: pytb

    2011-09-14 08:43:32 ERROR plone.app.upgrade Upgrade aborted. Error:
    Traceback (most recent call last):
      File "/home/david/.buildout/eggs/Products.CMFPlone-4.1-py2.6.egg/Products/CMFPlone/MigrationTool.py", line 175, in upgrade
        step['step'].doStep(setup)
      File "/home/david/.buildout/eggs/Products.GenericSetup-1.6.3-py2.6.egg/Products/GenericSetup/upgrade.py", line 142, in doStep
        self.handler(tool)
      File "/home/david/.buildout/eggs/plone.app.upgrade-1.1-py2.6.egg/plone/app/upgrade/v41/alphas.py", line 105, in add_siteadmin_role
        for permission_id, roles in state.permission_roles.items():
    AttributeError: 'NoneType' object has no attribute 'items'
    2011-09-14 08:43:32 INFO plone.app.upgrade End of upgrade path, migration has finished
    2011-09-14 08:43:32 ERROR plone.app.upgrade The upgrade path did NOT reach current version
    2011-09-14 08:43:32 ERROR plone.app.upgrade Migration has failed


If you've hit this, this means that you have a **workflow state**
somewhere on your portal that has no specific permissions associated
with it (or otherwise has all permissions set as ``Acquire``). An easy way
around this is to go find that workflow state (look in custom
workflows!) in portal\_workflow in the ZMI and temporarily change the
state or states so they have a permission.

Then, go ahead and upgrade your portal to Plone 4.x and you can change
your permission back.
