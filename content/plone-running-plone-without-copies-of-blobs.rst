Plone: running Plone without copies of blobs
############################################
:date: 2010-07-13 16:30
:author: davidjb
:category: Plone
:tags: blob, blobs, files, patch, plone, problem, python
:slug: plone-running-plone-without-copies-of-blobs

Having a bad day? Just bombed your only copies of some files that you'd
been storing as blobs together with your Plone database? Maybe you had
the blobs stored incorrectly on your Zeo client, rather than the server,
and then in a hasty effort to free some space (due to an on-going issue
with blobs eating HDD space), deleted them. Whoops..they're gone and
their references are still in your Plone database. Or, in a less
disastrous situation, maybe you just want to be able to run your Plone
database without needing lost blobs? Read on.The suggestion, as
mentioned elsewhere on the Interwebs, is to catch the exception that
gets raised on accessing relevant blobs. The two locations to catch (as
of plone.app.blob 1.0b18) are:

**plone/app/blob/mixins.py**

.. code:: python

    def getScale(self, instance, scale=None, **kwargs):
        """ get scale by name or original """
        try:
            if scale is None:
                return self.getUnwrapped(instance, **kwargs)
            handler = IImageScaleHandler(self, None)
            if handler is not None:
                return handler.getScale(instance, scale)
        except:
            pass
        return None

**plone/app/blob/field.py**

.. code:: python

    def get_size(self):
        """ return the size of the blob """
        try:
            blob = openBlob(self.blob)
            size = fstat(blob.fileno()).st_size
            blob.close()
        except:
            size = 100
        return size

If you put these try/catch statements in, you'll stop your site from
dying when accessing the View and Edit pages for your content. This
means you can safely replace lost blobs with files again, or otherwise
just use your site without the files, like if your client sends you only
the database to save on size. Happy days.
