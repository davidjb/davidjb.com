Configuring pulseaudio-equalizer defaults
#########################################
:date: 2011-12-16 11:26
:author: davidjb
:category: Ubuntu
:tags: audio, equalizer, linux, pulseaudio, settings, tip, ubuntu, volume
:slug: configuring-pulseaudio-equalizer-defaults

I've recently been using the Logitech G930 headset with my Ubuntu 11.10
install and I've found that the default configuration offers nothing in
terms of decent sound (tinny, no bass, etc). Thankfully, I've been able
to turn to pulseaudio-equalizer for help with turning down the treble
and up the bass. However, using pulseaudio-equalizer-gtk wasn't an
entirely satisfying experience as the default volume for my headset kept
being set to 100% upon restart. Now, if you recall my `previous post on
this headset`_, having the volume for the device set at 100% leads to
static being audible and this is a very bad thing.

Thankfully, pulseaudio-equalizer offers configuration in the form of
``~/.pulse/equalizerrc``.  It's not well documented (read: I had to go
dissect the source code) but essentially, you can control the output
device's volume by changing the 4th item within the configuration file. 
So the start of my config looks like this:

.. code:: ini

    mbeq\_1197
    mbeq
    Multiband EQ
    1
    Laptop
    < ...snip...>

and that number 1 is the volume percentage (eg 1 = 100%) that will end
up landing in ``~/.pulse/default.pa`` as the default volume for the device
being equalized. Change this number, then run:

.. code:: bash

    pulseaudio-equalizer disable-config
    pulseaudio-equalizer enable-config
    pulseaudio -k

and wait for PA to be restarted for you. Take notice that the default
volume is now set correctly.

I should mention that if you want to know what the other options relate
to, inspect the source of ``/usr/bin/pulseaudio-equalizer``, around line
54 onwards.

.. _previous post on this headset: http://davidjb.com/blog/2011/10/logitech-g930-headphones-audio-quality-under-ubuntu
