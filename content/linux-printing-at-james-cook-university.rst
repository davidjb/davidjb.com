Linux: Printing at James Cook University
########################################
:date: 2010-10-04 15:57
:author: davidjb
:category: Linux
:slug: linux-printing-at-james-cook-university

Printing at JCU is difficult on Linux, given JCU exists as a Windows
environment. The fact that Xerox Postscript drivers for Linux aren't
exactly straight forward to install doesn't help either - they require
custom filter applications to be compiled.

Setting up the drivers
----------------------

#. To make sure you have the right drivers, get this file:
   `fxlinuxprint-src-1.0.1.tar.gz`_, which is the drive source kindly
   obtained from the `Japanese Xerox site`_.
#. Extract the archive somewhere on your hard drive:

   .. code:: bash

       tar -xf fxlinuxprint-src-1.0.1.tar.gz

#. Make sure you've got **build-essential** and **libcups2-dev**
   packages installed (if on Debian/Ubuntu). Other systems (Red Hat,
   CentOS) will require equivalent packages; post if you've done it.

   .. code:: bash 

       sudo apt-get install build-essential libcups2-dev

#. CMMI:

   .. code:: bash

       ./configure
       make
       sudo make install

#. Select this as your PPD when adding your printer as this file:

   .. code:: bash

       /usr/share/cups/model/FujiXerox/en/fxlinuxprint.ppd[/sourcecode]


Setting up the printer
----------------------

#. Add a new ``Windows printer via SAMBA``
#. Specify the printer address as
   ``smb://AD/137.219.9.111/DB017-51-Colour``, where 'DB017-51-Colour'
   is your printer name (you'll probably need to ask someone or browse
   the machine at 137.219.9.111 to find out; on Linux you can use
   ``smbclient -L [hostname]``)
#. Set your authentication details (JC number and password)
#. Press Verify to make sure it works, and then click Forward
#. Under "Choose Driver" (or when selecting a Make and Model), make sure
   you choose to "Provide PPD file", and use the one that you've just
   installed using the instructions above.
   (``/usr/share/cups/model/FujiXerox/en/fxlinuxprint.ppd``). Click
   'Forward' when done.
#. Add the rest of your printer's details and click Apply.

Try and print something and it should be good now.

.. _fxlinuxprint-src-1.0.1.tar.gz: http://davidjb.com/wp-content/uploads/2008/12/fxlinuxprint-src-1.0.1.tar.gz
.. _Japanese Xerox site: http://www.fujixerox.co.jp/download/apeosport/download/c4300series/linux_module.html
