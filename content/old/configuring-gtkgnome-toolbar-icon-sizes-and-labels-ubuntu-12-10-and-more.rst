Configuring GTK/Gnome toolbar icon sizes and labels (Ubuntu 12.10+ and more)
############################################################################
:date: 2012-10-24 16:28
:author: davidjb
:category: Ubuntu
:tags: buttons, gnome, gtk, icons, toolbar, ubuntu
:slug: configuring-gtkgnome-toolbar-icon-sizes-and-labels-ubuntu-12-10-and-more

One major annoyance (first-world, clearly) for me having upgraded to
Ubuntu 12.10 is that my GTK toolbar icons are very large (32x32 pixels)
and have labels on them. This takes up a decent amount of screen real
estate in applications like gedit, Rhythmbox, and many others --
effectively anything that's using GTK. What's worse, it looks like the
latest Ubuntu (Quantal Quetzal) now is adding visual padding/spacing
around the buttons. I don't like this at all and prefer my buttons to be
tiny and without labels.

As per the post at http://ubuntuforums.org/showthread.php?t=1859526,
the issue was previously solved by configuring the setting within a
dconf setting, however this hasn't applied since 11.10.

However, it is possible to include the following in your
``/etc/gtk-3.0/settings.ini`` file to make your icons small and
beautiful again:

.. code:: ini

    [Settings]
    gtk-icon-sizes = panel-menu=16,16:gtk-large-toolbar=16,16

Start a GTK application like gedit and notice the difference.

To change the 'style' of the buttons on the toolbars (labels and icons
appearance), you'll need to launch (and install, if necessary)
``dconf-editor`` and modify the ``org.gnome.desktop.interface.toolbar-style``
setting. 

Once the editor is open, then traverse the settings schema tree on the
left-hand side until you find the setting. Once you've found it, click onto its
value and choose another option -- if you've left your GTK application open,
the style will change immediately. Pick the best one that suits you. I prefer
'icons' to just have the icons themselves, without labels (note that text
appears in a tooltip anyway).

Note that not all GTK applications will adhere to these options -- it is
possible for them to override the global settings (sigh, yes Rhythmbox,
that's seemingly you).

