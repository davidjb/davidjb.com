Linux: Make time with faketime
##############################
:date: 2010-07-12 12:02
:author: davidjb
:category: Linux
:tags: faketime, fix, linux, shp2svg, time, wine
:slug: linux-make-time-with-faketime

So you, like me, have hit a situation where you've got a time-sensitive
application that won't run? Maybe you've downloaded one of those apps
(like a demo) that won't run after a certain date and time because it's
"expired". Or else, maybe some other arbitrary time constraint is
keeping you from running a Linux (or even Windows) program. On Linux
(Ubuntu for me), there's ``faketime`` to the rescue - a very handy tool
that does what it says on the box, changes the system time for given
command.

After installing faketime by something like:

.. code:: bash

    sudo apt-get install faketime

you can run your program like this, and see the results:

.. code:: bash

    faketime 'last Friday 5 pm' /bin/date
    faketime '2008-12-24 08:15:42' /bin/date

Sweet as. Now, if you're running a Windows app in Wine (or any other app
with arguments), you can do that too. In my specific use-case, I was
trying to use `shp2kml`_. Ignoring the fact their website fails at
actually letting me download the file (I had to get my version
elsewhere; copied here for posterity: `Shp2kml.zip <|filename|files/Shp2kml.zip>`_), their program fails
at running due to it being "expired". Noting other posts about people
turning back their clocks to 2006, I did the same thing with faketime,
so as not to stuff around with my system clock.

.. code:: bash

    faketime '2006-09-20' wine Shp2kml.exe

and voila, it works. Seems like the change affects Wine's start-up a
little when first starting with the new date, but it does work just
fine. Yay for Linux!

.. _shp2kml: http://www.zonums.com/shp2kml.html
