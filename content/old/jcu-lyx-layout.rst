JCU LyX Layout
##############
:date: 2008-11-09 11:25
:author: davidjb
:category: Study 
:slug: jcu-lyx-layout


.. note Update: this is now available on GitHub at 
       https://github.com/davidjb/JCU-Thesis-LyX-Layout for you to fork and
       improve.  Feel free to drop me a line if you're using it!

What might be interesting to all you `James Cook
University`_ or **JCU** folk out there (yeah, you know who you are!), is
the attached zip file to this post. It's a `LyX`_ layout that
automagically inserts the required details into your thesis (Honours or
PhD), assuming that you give the correct details to LyX. Just so you
know, **LyX** is a WYSIWYM (what-you-see-is-what-you-mean) editor for
**LaTeX**, which makes things very easy to make great looking documents.
It's free, it's more powerful and easier than M$ Word, and if you're not
using it, it should be because you just found about it.

Unzip the files, place them in your .lyx document directory and tell LyX
to use that layout. See the Document menu and then Settings, then
Document Class and choose 'Local Layout'. LyX might warn you about
something, but just make sure all the unzipped files are in the same
folder as your original document itself.

Now, generally near the start of the document, use the available
document layouts to create a:

-  Title
-  Author (with your name)
-  Degree (with something like 'Bachelor Of Information Technology with
   Honours')
-  School (something like 'Information Technology')
-  University (with 'James Cook University'), and
-  Crest Filename with 'jcucrestcolour.jpg', the name of the JCU logo
   you have (it's in the zip file, but if you've got a specific JCU
   school pic then you can change it.  EDIT: It's the old logo, but see
   below for the new one).

You can add Acknowledgements and an Abstract if you want, and then
everything else like Table of Contents and Figures etc.

When you start your document, insert this ERT code::

    \pagenumbering{arabic}

to start the document numbering correctly.

That's it! Render the document as PDF using LyX and see what happens. If
you find errors, it's because you're missing some LaTeX packages.
Configure your typeset program (MikTeX if you're on Windows) to
automatically download missing packages, then run Reconfigure on LyX,
restart it, and go again. Make sure you're on the net first!

Hopefully you guys from JCU can get some use out of this. Otherwise, if
someone (or anyone!) wants to let JCU staff know about this thesis
template go ahead. I hear that some people are (still!) using Microsoft
Word and having pain. Free yourself and get LyX and LaTeX, it's the best
move you'll make for your work. Not to mention they're all free..forget
paying real money to Micro$oft.

Files
-----

#. `JCU LyX Layout (2008) <|filename|../files/jcu_lyx_layout_2008.zip>`_
#. `JCU Logo (New, SVG) <|filename|../files/jcu_logo.zip>`_

.. _James Cook University: http://www.jcu.edu.au/
.. _LyX: http://www.lyx.org/
