Plone: Archetypes With Paster
#############################
:date: 2008-12-17 11:42
:author: davidjb
:category: Work
:tags: content, paster, plone, types, zopeskel
:slug: plone-archetypes-with-paster

From
http://www.koansys.com/tech/create-plone-3-archetype-product-with-zopeskel-and-buildout:

ZopeSkel can create Archetype-based products for Plone 3. Wire it up in
Buildout.

After creating a Plone 3 instance (e.g., with Unified Installer) go into
the src/ directory and create a development product with ZopeSkel::

    > paster create -t archetype
    Enter title (The title of the project) ['Plone Example']: Koansys Newproduct
    Enter namespace_package (Namespace package (like plone)) ['plone']: koansys
    Enter package (The package contained namespace package (like example)) ['example']: newproduct
    Enter zope2product (Are you creating a Zope 2 Product?) [False]: True
    Enter version (Version) ['0.1']:
    Enter description (One-line description of the package) ['']:
    Enter long_description (Multi-line description (in reST)) ['']:
    Enter author (Author name) ['Plone Foundation']:
    Enter author_email (Author email) ['<span class="mh-email">plon<a href="http://www.google.com/recaptcha/mailhide/d?k=01y8BLyDqFl2lR8hms6kYeaw==&c=dWZpn-kF-kBBpxKfk95rjiTb1Ew_D4R2wQXotn8J5EOipnAJf_DdjfsAvsl4fVO3" onclick="window.open('http://www.google.com/recaptcha/mailhide/d?k=01y8BLyDqFl2lR8hms6kYeaw==&c=dWZpn-kF-kBBpxKfk95rjiTb1Ew_D4R2wQXotn8J5EOipnAJf_DdjfsAvsl4fVO3', '', 'toolbar=0,scrollbars=0,location=0,statusbar=0,menubar=0,resizable=0,width=500,height=300'); return false;" title="Reveal this e-mail address">...</a>@lists.sourceforge.net</span>']:
    Enter keywords (Space-separated keywords/tags) ['']:
    Enter url (URL of homepage) ['http://svn.plone.org/svn/plone/plone.example']:
    Enter license_name (License name) ['GPL']:
    Enter zip_safe (True/False: if the package can be distributed as a .zip file) [False]:

then go into that directory (koansys.newproduct) and add a content type::

    > paster addcontent contenttype
    Enter contenttype_name (Content type name ) ['Example Type']: Recipe
    Enter contenttype_description (Content type description ) ['Description of the Example Type']: Recipe with ingredients, procedure, metadata
    Enter folderish (True/False: Content type is Folderish ) [False]: True
    Enter global_allow (True/False: Globally addable ) [True]:
    Enter allow_discussion (True/False: Allow discussion ) [False]: True

Modify your buildout.cfg to use these as development eggs and tell each
instance about it's ZCML (otherwise it won't show up in the Quick
Installer):

.. code:: cfg

    [buildout]
    ...
    eggs =
    ...
    #name of the actual egg folder
    NRBCLiterature
    develop =
    #path to egg folder
    src/NRBCLiterature

    [instance]
    recipe = plone.recipe.zope2instance
    eggs =
    ${plone:eggs}
    ${buildout:eggs}
    zcml =
    #name of the egg itself
    nrbc.literature

Re-run buildout and restart your "instance" instance and you should see it in the Quick Installer.

