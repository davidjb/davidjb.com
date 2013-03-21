Creating & distributing a new Plone/PyPI product
################################################
:date: 2009-08-17 10:01
:author: davidjb
:category: Python
:tags: easy_install, open source, plone, product, python, release, Software
:slug: creating-distributing-a-new-plonepypi-product

It's amazing to see how technologies can be so smoothly integrated these
days.  I'm talking, at least in this instance, about how setuptools
works with PyPI (and then Plone.org's Products section) and allows you
to distribute your product(s) to the world.  So far, I've just got the
one -- collective.portlet.googleapps -- but I'm sure time will pass and
I'll have some more useful things to contribute. Here's a summary of
what I did:

#. Create the product.  ZopeSkel is a wonderful help here for Plone
   products. [I lie a little bit in my code example, because sadly, the
   plone3\_portlet template doesn't have nesting.  I cheated by using
   the Archetypes template and copied in my portlet code & repeated to
   create multiple portlets in one product]:

   .. code:: bash

       easy_install-2.4 ZopeSkel
       paster2.4 create --list-templates
       paster2.4 create -t plone3_portlet collective.portlet.googleapps

#. Upload it to some relevant code repository.  I've used the Plone
   collective SVN (and `this guide`_):

   .. code:: bash

       svn mkdir https://svn.plone.org/svn/collective/collective.portlet.googleapps -m 'Created new project'
       svn mkdir https://svn.plone.org/svn/collective/collective.portlet.googleapps/{trunk,branches,tags} -m 'Added base files'
       svn co https://svn.plone.org/svn/collective/collective.portlet.googleapps/trunk collective.portlet.googleapps
       [copy stuff into the folder]
       svn ci

#. Do some work.  When you're happy, make a tag for the relevant release
   version:

   .. code:: bash

       svn copy https://svn.plone.org/svn/collective/collective.portlet.googleapps/trunk https://svn.plone.org/svn/collective/collective.portlet.googleapps/tags/0.1

#. `Sign up for PyPI`_ (Python Package Index), `generate a GPG
   key`_, and add the key ID to your account profile page.  Your key ID
   can be found on this line after generation::

       gpg: key XXXXXXXX marked as ultimately trusted

   or otherwise through **gpg --list-keys**

#. `Sign up`_ for an account on Plone.org to allow you to upload your
   product here too.  Make sure you follow the URL you get emailed and
   change your password.
#. Edit your ~/.pypirc file to include the following details from `this
   page`_.  My file also needed the **server-login** section (something
   to do with differences between PyPI and Plone.org, I think).:

   .. code:: ini

       [server-login]
       username:XXX
       password:YYY

#. When ready, you can upload your work to PyPI and Plone.org:

   .. code:: bash

       easy_install-2.4 collective.dist
       python2.4 setup.py register sdist bdist_egg upload -s
       python2.4 setup.py mregister sdist mupload -r plone.org

#. If everything goes according to plan, then you should see 'Response
   200' back from the servers.  If not, then check the following:

   #. Your passwords and user names are correct in your ``~/.pypirc`` file
      (yes, it's true, they're plaintext...)
   #. Make sure your accounts on both PyPI and Plone.org are active and
      actually exist.
   #. You've followed any further instructions about troubleshooting on
      the links I've posted.

#. Once done, you should be able to see your package on PyPI (and
   administrate it once logged in), and see your product on Plone.org. 
   Keep in mind that Plone.org has an approval process that you'll have
   to wait for before your product is fully visible.


.. _this guide: http://plone.org/documentation/how-to/create-a-new-project-in-the-plone-collective
.. _Sign up for PyPI: http://pypi.python.org/pypi?%3Aaction=register_form
.. _generate a GPG key: http://www.dewinter.com/gnupg_howto/english/GPGMiniHowto-3.html
.. _Sign up: http://plone.org/join_form?came_from=http%3A//plone.org
.. _this page: http://plone.org/documentation/tutorial/how-to-upload-your-package-to-plone.org/tutorial-all-pages
