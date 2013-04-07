Ubuntu: Crackling audio noises on a Dell M1530 (or HDA cards)
#############################################################
:date: 2010-01-16 12:18
:author: davidjb
:category: Linux
:tags: 9.10, audio, computer, crackling, dell, intel, karmic, laptop, m1530, popping, sound, ubuntu
:slug: ubuntu-crackling-audio-noises-on-a-dell-m1530-or-hda-cards

The problem I found (so did everyone else) when updating to Ubuntu 9.10
Karmic was static/popping noises when your sound card is silent (aka
goes into power-save mode). It applies to my Dell XPS M1530 laptop's
on-board sound and probably to the same chipset elsewhere.

The fix couldn't be simpler! Simply edit this file (as root)::

    /etc/modprobe.d/alsa-base.conf

and comment out the last line. Then, restart ALSA to save you having to
do a reboot to check it worked:

    sudo /etc/init.d/alsa-utils stop
    sudo alsa force-reload
    sudo /etc/init.d/alsa-utils start

Thanks to Ubuntu Geek `here`_.

.. _here: http://www.ubuntugeek.com/ubuntu-tip-how-to-fix-crackling-noise-on-hda-audio-cards-in-ubuntu-9-10.html
