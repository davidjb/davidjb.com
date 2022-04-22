Deliveroo watches you while you eat
###################################

:date: 2022-04-22
:category: Tech
:tags: Food, Technology, Privacy, Surveillance

**tl;dr** Deliveroo sends your browser `movie titles with food puns
<#movie-titles>`_ as it tracks your activity.

----

The online food ordering platform `Deliveroo`_, like many (most?) online
platforms, monitors you as you interact with their website.  It's not really a
secret that `behavioural analytics`_ (or "big data analytics") get gathered
from our time online, but is rather what we've come to expect of online
companies who seek to extract, leverage and monetise the data generated from
our interactions with their services.

It won't surprise anyone to know that Amazon `actively uses
<https://www.amazon.jobs/en/teams/customer-behavior-analytics>`_ customer
behaviours in real-time to affect the results and recommendations you see on
the site - browse for a cable, see 100 more cables recommended forever. If you
look carefully at effectively any link Amazon shows you, you'll see its URL is
littered with tracking parameters. Similarly, if you scroll or browse, you'll
notice multitudes of HTTP requests being fired off in succession, indicating
what you're doing and helping Amazon (try to) understand what you are or
aren't looking at.

Likewise, it would probably be of little surprise that Airbnb, a hip, modern
sharing-economy company, is also highly active in this space.  Airbnb's
business is based around data - and apparently connecting guests to hosts'
accommodation - through its online platforms. However, in order to achieve this,
you'll find Airbnb sending several behaviour tracking events per *second* when
you're on their site, occurring as you move your cursor, type, interact with the UI
across listings or are just sitting idle. A short browsing session (or a
background tab left open) can easily end up sending off thousands or tens of
thousands of tracking events.

Being of the same ilk, Deliveroo also tracks you as you use their system.  As
you browse pages, click elements on a page or scroll up or down, Deliveroo
fires off dozens requests with an event payload describing what you just did.
For example, the following is sent every time your viewport scrolls to or
past a category on a restaurant's menu:

.. code-block:: text

   POST https://api.au.deliveroo.com/orderapp/v1/events
   User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0 (deliveroo/consumer-web-app; browser)
   X-Roo-Client: consumer-web-app
   X-Roo-Country: au
   X-Roo-Guid: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
   X-Roo-Session-Guid: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
   X-Roo-Sticky-Guid: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX

.. code-block:: json

   {
     "events": [
       {
         "name": "Menu Scroll to Category",
         "properties": {
           "category_id": "12345678",
           "restaurant_id": "999999",
           "served_menu_request_uuid": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
           "user_agent": {
             "family": "Firefox",
             "major": "98",
             "minor": "0",
             "patch": null
           },
           "white_label_brand": "core"
         },
         "time": 1650524885
       }
     ]
   }

.. _movie-titles:

The specifics of the event data are hardly surprising, but what's really fun
is a header that gets returned from the response to the API call – the
developers at Deliveroo clearly have a sense of humour, all while they
play `Big Brother`_, spending your bandwidth and Internet quota in the
process. This header comes back in the HTTP response::

    x-watch-while-you-eat: Guardians of the Garlic: Vol. 2

It appears this gets sent for any API calls made in the ``/orderapp``
namespace, even those that error. Try it yourself with a ``GET`` request to
https://api.au.deliveroo.com/orderapp/v1.

To save you the effort, here's the listing of all the movie titles you'll get
served, subjectively ordered by level of humour or cringeworthiness::

    V for Vienetta
    The Prawn Identity
    12 Hangry Men
    The Silence of the Lamb Chops
    The Lamb Shank Redemption
    Scone in Sixty Seconds
    Hack-slaw Fridge
    Guardians of the Garlic: Vol. 2
    Kung Pow Panda
    Soy Story
    Beauty and the Feast
    The Inedibles
    Despicable Meat
    A Clockwork Orange Juice
    Reservoir Hotdogs
    Power Radishs
    Much Ado About Muffin
    Full Metal Jacket Potato
    Mango Unchained
    The Big Shortcrust
    The Great Escalope
    Dial M for Murgh
    Mad Max: Fury Roast
    Planet of the Canapes
    Return to the Planet of the 'Shakes
    War for the Planet of the Grapes
    Top Bun
    Fill Bill
    Life of Pies
    Spoonlight
    Manchester by the Pea
    No Curry for Old Men
    Justice Peach
    I, Daniel Cake
    Plump Fiction
    Pi Za Za Land
    Hell or High Tea

Someone is clearly a fan of the Planet of the Apes series (ahem, *Canapés*).

One might be inclined to wonder exactly how much money this Easter Egg itself
is costing the company to send those extra bits over the wire; I appreciate a
joke as much as the next person but this adds up, especially when *I'm* paying
for the cellular data connection.  For the whole tracking experience overall
on Deliveroo, much like Amazon or Airbnb, a lot of data can be consumed in a
session – just scrolling down to the bottom of one example page costs ~150KB
to send and receive all these events, however funny the hidden headers happen
to be. This quickly adds up to megabytes.

In fairness, some of these titles did make me chuckle for the briefest of
seconds, but your average user isn't going to find this. Maybe it's some light
relief for the the security professionals doing pentesting. At any rate, my
laugh was before realising what the API was doing and that it wasn't already
being blocked in my browser.  In response, I wrote browser rules for `uBlock
Origin`_ (or Adblock Plus, etc) to block these requests::

    ||deliveroo.com^*/events
    ||events-tracker.deliveroo.net^

This works for any Deliveroo site worldwide (and probably its white-labelled
solution, Deliveroo Signature, as well). These `have been submitted
<https://github.com/easylist/easylist/issues/11758>`_ for inclusion in
`EasyPrivacy`_, which is something worth using in this case too because when
an error occurs sending a tracking event, Deliveroo will attempt to send a
crash report off to Sentry; EasyPrivacy has a rule for handling this already.

Whilst on the topic of privacy, it's worth noting that Deliveroo does a
`Privacy Policy <https://deliveroo.com.au/privacy>`_ which supposedly
protects your data.  However, I'm really curious to know what they mean by:

    Unless you have elected to remain anonymous through your device and/or
    platform settings, this information may be collected and use [sic] by us
    automatically [...]

and what settings they consider for someone to choosing to remain anonymous.

Maybe they're good netizens and apply the settings supplied in Do Not Track
(DNT) or Global Privacy Control (GPC) headers on the server-side *after*
you've sent your data to them. Or maybe it's just another perfunctory attempt
to appease anyone who might challenge it. 🤷‍♂️

It's dinner time — I'm off to get some takeaway and watch a movie…  

.. _Deliveroo: https://deliveroo.com.au
.. _behavioural analytics: https://en.wikipedia.org/wiki/Behavioral_analytics
.. _Big Brother: https://en.wikipedia.org/wiki/Big_Brother_(Nineteen_Eighty-Four)
.. _uBlock Origin: https://github.com/gorhill/uBlock
.. _EasyPrivacy: https://easylist.to
