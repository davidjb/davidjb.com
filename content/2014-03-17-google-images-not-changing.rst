Gmail avatar/photo always reverts after being changed
#####################################################

:category: Google

Got an unsightly image associated with your Gmail messages, your
Google Groups posts, Google Drive activity or somewhere else obscure
within Google's domain?  Tried changing that image several times
and it won't budge - or it does and reverts itself right back?
Your main Google+ avatar just doesn't want to sync up with other Google
services?  Sure, I hear you - you're not alone.  Your issue is probably
intermittent too - you change the image on Gmail and your old image
comes bounding back, possibly several days later.

It's an annoying issue and I feel for you.  So, hopefully this might be the
answer to your issues:  it turns out the image is coming from a
setting in my chat client (Pidgin using XMPP). Upon me changing this image
within my client, the image in Gmail, Google Groups and Google Drive
immediately reflected the change.  Hooray!

On a technical level, it was I've got Pidign configured to talk to my domain
(previously set up as Google Apps for your Domain), which in turn is configured
to talk to Google's XMPP servers. 

The reason the issue was intermittent is because the computer/OS this is
installed on is only used every so often -- every time it was logged in, the
image was pushed back to Google. Simple once you know!

For anyone else out there, check your XMPP clients (Google Talk, Pidgin,
Epiphany and so on).  For Pidgin, the image wasn't my main image but explicitly
set on my XMPP account,  set in::

    Manage Accounts -> my XMPP account -> Buddy Icon.

Hence, it wasn't obvious at all.

Happy hunting.

FYI: previously asked on the forums at
https://productforums.google.com/forum/#!msg/gmail/CIOEmX3cmnA/yhd5whY0x58J.


