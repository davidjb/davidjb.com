Logitech G930 Headphones audio quality under Ubuntu
###################################################
:date: 2011-10-24 09:28
:author: davidjb
:category: Linux 
:tags: g930, headphones, linux, logitech, pulseaudio, ubuntu
:slug: logitech-g930-headphones-audio-quality-under-ubuntu

So I recently purchased a new set of Logitech G930 headphones and am
currently using them with the latest version of Ubuntu, 11.10.  Set up
was a breeze - just plug, check your PulseAudio config, and play.  For
those of you, like me originally, who were wondering whether the G930
works on Linux, it certain does on Ubuntu.

Now, it wasn't all peaches and cream because of two things.  Firstly,
the audio output with the default configuration was completely lacking
any depth and 'substance' to the sound being produced.  I'm not an
audiophile and I have slight hearing problems, but the sound was
entirely lacking anything in the form of bass, and overall, just very
tinny and washed out.  Praying it's not the headset itself, I went and
obtained ``pulseaudio-equalizer`` from `this PPA`_ (and it comes with
its GTK counterpart, ``pulseaudio-equalizer-gtk``).  Running the latter
of these two commands brings you up the interface, and I selected the
'Laptop' preset and enabled this.  I had to re-jig around a little with
clicking the 'EQ enabled' checkbox and the 'Apply Settings' button
whilst listening to music but this preset makes things 100% better. 
First hurdle solved.

The second issue was the constant static being introduced in my audio. 
Only when sound was being played mind you, not just when the headset was
sitting turned on in silence, so this lead me to think it must
(hopefully) be something I could configure and not an interference issue
or something hardware related.  Thankfully, I was right.  Firing up
``pavucontrol``, my much-preferred application over the default Ubuntu
sound panel, I found the static was being introduced when my headphone
output device was set at 100% volume (the Output Device, not anything
else). The static is gone after I dropped the device output back (I'm
using 33%). If I need more amplification, then I can simply use the
Equalizer virtual output device to increase the volume (and/or amplify
the applications behind the output).

Now, the headset works fantastically.

.. _this PPA: https://launchpad.net/~nilarimogard/+archive/webupd8
