Configuring L2TP over IPSec VPN for iOS on Billion 7800DOX Router
#################################################################

:category: Tech

This will almost certainly be my last Billion router. They have awful support
and refuse to respond to simple questions about failing hardware, but for now,
I'm persevering with the Billion 7800VDOX modem/router because that's what I
have.

The *O* series of routers comes with a VPN server built in (either PPTP or
L2TP), but since PPTP is inherently insecure now, I'm setting up L2TP over
IPSec and having this work with my iOS device.  I'd managed to find a PDF
provided by Billion about this a while back, but could no longer find it
online and the configuration UI is unclear.

Thankfully, I've kept a copy of the PDF, and you can find it here: `7800X
L2TP-IPSec_iPhone.pdf
<https://drive.google.com/a/davidjb.com/file/d/0B5CAsXBD5-mAa1hJMnIwangzaU0/view>`_.

In summary, the tricks to this are:

* Adding an IPSec tunnel mode connection with a pre-shared key (the ``secret``
  you'll use on your connecting device)
* Ensuring that ``Tunnel Authentication`` isn't enabled when configuring the
  L2TP Server.
* Selecting ``L2TP`` as the VPN type on your iOS device (and not ``IPSec``).

Assuming your Billion device supports similar configuration options, this
should work for you as well.  I've now tested this on the 2.32e firmware
(latest at time of writing) on the 7800VDOX router with iOS 9.0.2.

