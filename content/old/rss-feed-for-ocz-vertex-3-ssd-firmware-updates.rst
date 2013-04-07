RSS Feed for OCZ Vertex 3 SSD firmware updates
##############################################
:date: 2011-10-20 18:04
:author: davidjb
:category: Hardware 
:tags: hack, ocz, pipes, regex, ssd, version, yahoo
:slug: rss-feed-for-ocz-vertex-3-ssd-firmware-updates

Here's a quick and dirty solution to me not being able to keep updated
with OCZ firmware updates for my Vertex 3 SSD.  For whatever reason, OCZ
doesn't provide a news feed of firmware updates (that I know of, correct
me if I'm wrong!) so I've sorted a screen scraping Yahoo Pipes pipe to
do it for me:

`http://pipes.yahoo.com/pipes/pipe.run?\_id=a1f15d7ead0122567ad6537b2de484a3&\_render=rss`_

This RSS feed will (or should) only ever feature just 1 item - the
latest version information for the firmware.  So, it won't handle
keeping track of history, but if you (or I) add the feed to something
like Google Reader, that will keep track of changes to the RSS feed for
us/me.  So, when the target page on `OCZ's site`_\ changes its version
information, the feed will update, and Google Reader knows
automagically.

Yahoo Pipes and Google Reader strike again.

Oh and apparently this firmware isn't just for the Vertex 3, but also
for the OCZ Vertex 3, Vertex 3 Max IOPS, Agility 3, Solid 3, RevoDrive 3
and RevoDrive 3 X2, so anyone using those other drives should be good
too.

.. _`http://pipes.yahoo.com/pipes/pipe.run?\_id=a1f15d7ead0122567ad6537b2de484a3&\_render=rss`: http://pipes.yahoo.com/pipes/pipe.run?_id=a1f15d7ead0122567ad6537b2de484a3&_render=rss
.. _OCZ's site: http://www.ocztechnology.com/ssd_tools/OCZ_Vertex_3,_Vertex_3_Max_IOPS,_Agility_3,_Solid_3,_RevoDrive_3_and_RevoDrive_3_X2/
