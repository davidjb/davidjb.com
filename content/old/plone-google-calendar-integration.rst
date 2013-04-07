Plone: Google Calendar Integration
##################################
:date: 2009-02-19 08:55
:author: davidjb
:category: Plone 
:tags: add to, calendar, event, google, integration, plone
:slug: plone-google-calendar-integration

Wouldn't it be great if you could somehow add your Event content item
within the Plone CMS onto your Google Calendar with just a click? (it'd
be better with fewer, but 1 click is pretty good - give me a break!)

Try this placed inside the ``event_view`` page template (customise it in
the ZMI) after the vCal and iCal links:

.. code:: html

    <a href="#"
    tal:attributes="href python:'http://www.google.com/calendar/event?action=TEMPLATE'
    +'&text='+here.title
    +'&dates='+here.start().toZone('UTC').ISO8601().replace('-','').replace(':','').split('+')[0]+'Z/'
    +here.end().toZone('UTC').ISO8601().replace('-','').replace(':','').split('+')[0]+'Z'
    +'&location='+here.location
    +'&details='+here.getRawDescription()+'<br />'+here.getRawText()
    +'&trp=true'
    +'&sprop=website:'+here.event_url()
    +'&sprop=name:'+here.contact_name();"
    title="Add this event to Google Calendar"
    target="_blank"
    style="background-image: none; padding: 0px;"
    >
        <img src="https://www.google.com/calendar/images/ext/gc_button1.gif" alt="Add to Google Calendar" width="50" height="13"  />
    </a>

So, it's clear as mud, right? It does some magic and completes a link
for you to use to add your given event and it's details into Google
Calendar from Plone.

For those of you really paying attention, the date conversion is nasty
(why doesn't Google accept an immediately accessible format?) and this
*won't* work unless all fields are filled out. I'm still working on a
field-friendly solution.

Either way, I didn't find anything on the web about doing this, so here
it is. Use as you will.
