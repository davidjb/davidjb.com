ffmpeg and FLV on Ubuntu
########################
:date: 2009-09-22 10:21
:author: davidjb
:category: Linux
:tags: ffmpeg, flv, linux, multimedia, ubuntu
:slug: ffmpeg-and-flv-on-ubuntu

Wow, ffmpeg is really great for converting multimedia.  Unfortunately,
the support for MP3 audio doesn't appear available by default.  Sure, it
can decode MP3 audio and write to an MP3 container, but what about
having an actual MP3 codec available?

.. code:: bash

    sudo apt-get purge ffmpeg
    sudo apt-get install libavcodec-unstripped-52 libavdevice-unstripped-52 libavformat-unstripped-52 libavutil-unstripped-49 libpostproc-unstripped-51 libswscale-unstripped-0 ffmpeg

As a little bonus, there's a number of other codecs that come along with
it too (xvid etc).  I'm not too fussed on them but now I can use
``-acodec libmp3lame`` as my audio codec and have the FLV outputted with
MP3 audio.  There's a problem with either the default FLV encoder or VLC
not being able to playback the audio with default settings, but this
seems to work.

That said, it remains to be seen if this'll cause any problems with FLV
playback, but the players I've used so far (web-based) seem happy
enough.
