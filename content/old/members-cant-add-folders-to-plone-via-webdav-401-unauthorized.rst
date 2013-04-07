Members can't add folders to Plone via WebDAV (401 Unauthorized)
################################################################
:date: 2012-06-22 11:20
:author: davidjb
:category: Plone 
:tags: folder, http, plone, upload, webdav
:slug: members-cant-add-folders-to-plone-via-webdav-401-unauthorized

This is a mirror of the (excellent) documentation at
http://plone.org/documentation/error/unable-to-create-a-folder-through-webdav/,
but just a short editorial to also highlight that this is still very
applicable to Plone 4.x. Effectively, the symptom is that users will
report seeing a "401 Unauthorized" error when trying to create folders
within areas they have access to as an Owner.  Without further ado, the
documentation:

Using a WebDAV client on a Plone site, site users are unable to create
newfolders directories where they have Owner role.

Problem:
~~~~~~~~

The WebDAV "make folder" method, MKCOL, requires the "Add Folders"
permission. This is not normally granted to Members or Owners on the
site.

Workaround:
~~~~~~~~~~~

In the Zope Management Interface, under the "Security" tab for
the Plone root, check the "Owners" box for the "Add Folders" permission
setting.

