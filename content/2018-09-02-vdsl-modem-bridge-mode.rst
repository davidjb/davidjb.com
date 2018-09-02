VDSL Modem in Bridge Mode: How does it work?
############################################

:category: Tech
:tags: Networking, Modem, Internet, OpenWrt

In networking terms, a *Bridge* is a way in which multiple networking
interfaces (physical or virtual) can be made to function as as if they were a
single network interface.  In general terms, this is how clients associated
with a router on both wired Ethernet and wireless can communicate together.
In my specific case, I have a VDSL modem which is configured in *bridged mode*
and plugging into my Turris Omnia router to enable the Turris to connect to
the Internet.

With details scarce online about exactly *how* this black magic works to allow
my Ethernet-only router to connect to a VDSL telephone line, I went
investigating and here's what I found.  The tl;dr of this is that the "black
magic" isn't too hard to understand, it just operates at layer 2 (data link
layer).  Likewise, a key takeaway for those with similar hardware is that
*yes*, the Turris Omnia router can connect to both IPoE and PPPoE networks,
provided you have a bridge modem present and configured correctly.

Firstly, some terminology:

* **ATM** - Asynchronous Transfer Mode
* **PTM** - Packet Transfer Mode
* **IPoE** - `IP over Ethernet <https://en.wikipedia.org/wiki/IPoE>`_
  (typically seen as just ``DHCP`` as a router's WAN options)
* **PPPoE** - `Point-to-Point Protocol over Ethernet <https://en.wikipedia.org/wiki/Point-to-Point_Protocol_over_Ethernet>`_

So in my case, I have my router configured to use DHCP to connect to the
Internet and it is connected to my modem via an Ethernet cable
and the modem is set up in bridge mode.  What this mean, at least in my
modem's OpenWrt configuration, is that *all* the physical interfaces are
bridged together like so::

    bridge name     bridge id               STP enabled     interfaces
    br-lan          0fff.b8dfe319fa2c       no              eth0
                                                            eth1
                                                            eth2
                                                            eth3
                                                            eth4
                                                            wl0
                                                            wl1
                                                            atm_8_35
                                                            ptm0

This includes the Ethernet ports, wireless LAN and the ATM/PTM xDSL
connections.  So this means that I can technically plug the router into any of
the ports at all and it'll work (though in my case, I'm plugged into ``eth0``).

So my ISP uses ``IPoE`` (called just ``DHCP`` in my OpenWrt router's
configuration) to connect, which more or less boils down to the router sending
DHCP messages and getting a response from the ISP (over the modem's bridge
``br-lan`` to the PTM interface ``ptm0``).  The way in which the modem knows how
to magically forward these frames/packets is by maintaining a forwarding table
of MAC addresses of devices attached to the bridge. You can see this inaction
by running the command::

    brctl show
    brctl showmacs br-lan

where ``br-lan`` is the name of your bridge interface in the modem.

So, the process goes like so:

1. The router sends DHCP discovery message out of its WAN port, which is
   connected to the bridge modem. This message contains its MAC address as the
   source.
2. The bridge modem considers what to do with DHCP discovery, which has a
   broadcast destination.  In this case, the bridge's forwarding table
   has no specific port for a broadcast and so broadcasts to all ports on the
   bridge. The modem records the router's MAC address and port in the
   forwarding table for later usage.
3. The DHCP discovery message crosses my ``ptm0`` link and arrives at the ISP.
   The ISP's DHCP server then sends back a DHCP offer with a destination of
   the router's MAC address.
4. The bridge modem receives the DHCP offer and consults its bridge forwarding
   table to determine what to with the message.  Upon finding the router's MAC
   and port in its forwarding table, forwards the message onto ``eth0``.
5. The router receives the DHCP offer and then continues to complete the DHCP
   process, with messages being forwarded across the bridge in the manner
   mentioned in steps 1 through 4.  Further data flows the same way out of or
   into my home network, effectively equating to the router being plugged
   transparently into the ISP's networking equipment."
6. The router now has now established an IP address and determined its default
   gateway, allowing an Internet connection.

There you have it, that's how an IPoE or DHCP connection is made across a
bridged VDSL modem.  Once the bridge's forwarding table is established, then
that's more or less that.

I was unsure originally because I didn't know *which* port I had
to plug into on the modem - anecdotal evidence online said it had to be port 1
(``eth0``) - but now I know it can be any port (even Wi-Fi if you could get
that happening).  Likewise, I wasn't sure about how the communication should
take place because my previous setup used PPPoE; in this case, the bridge was
just the same, it's just that now DHCP packets are being passed around to
set up the connection compared to PPPoE discovery and PPP session data.
It's my understanding IPoE/DHCP has a lower overhead than PPPoE because of the
PPP overhead imposed by the latter so that's one benefit, as well as not
needing to maintain credentials in the modem for PPPoE.

For further reading, check out `Using PPPoE and IPoE in Ethernet Broadband
Networks <|filename|files/using_pppoe_and_ipoe.pdf>`_, a white paper prepared
by Juniper Networks, which more or less covers all the ins and outs of IPoE
and PPPoE, and now you know how the bridge modem fits into that mix.

