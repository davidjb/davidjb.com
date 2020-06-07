PloneFormGen (Plone) & Google Calendar Integration
##################################################
:date: 2009-09-22 10:40
:author: davidjb
:category: Plone 
:tags: calendar, form, gen, google, mash, pfg, plone, product, python, script
:slug: ploneformgen-plone-google-calendar-integration

It's a little bit of a different mash-up, but it's still nonetheless
useful to have, given types of booking forms and so forth that could
utilise it.  The easiest way I found (to avoid security issues with
Python scripts in Plone) was to create an external method and just
import it within a PFG Custom Adapter.

Parts
~~~~~

-  My `GoogleCalendar.py`_ external method.  I've had to add this into a
   policy product I have.  The function should be generalised enough to
   work with any Google account, hosted or not.  In short:

   -  It takes in a variety of arguments (email, password,
      calendar\_url, start\_time, end\_time, title, location, content).

      -  Email/password are your auth details
      -  calendar\_url is where you're putting the event,
      -  and the rest of the args are related to the event itself.

   -  It builds the XML-based request to create the event.  I tried
      going for the gdata API, but it's just over the top for a simple
      exercise like this.
   -  Send the request to Google (twice, as required), and create the
      event in the process.

-  A custom PFG script adapter like this:

   .. code:: python

        from DateTime import DateTime
        from my.theme.Extensions.GoogleCalendar import createGoogleCalendarEvent
        calendar_url = 'http://www.google.com/...'
        email = '<span class="mh-email">myu<a href="http://www.google.com/recaptcha/mailhide/d?k=01y8BLyDqFl2lR8hms6kYeaw==&c=WDOrJledyL7Tzo9unwfHPwgE0TrIw31nHDxcUFu_QIY=" onclick="window.open('http://www.google.com/recaptcha/mailhide/d?k=01y8BLyDqFl2lR8hms6kYeaw==&c=WDOrJledyL7Tzo9unwfHPwgE0TrIw31nHDxcUFu_QIY=', '', 'toolbar=0,scrollbars=0,location=0,statusbar=0,menubar=0,resizable=0,width=500,height=300'); return false;" title="Reveal this e-mail address">...</a>@google.com</span>'
        password = 'shhhhhsecret'
        startDateTime = (DateTime(str(fields['start-date-time']))).HTML4()
        endDateTime = (DateTime(str(fields['end-date-time']))).HTML4()
        eventTitle = str(fields['purpose'])
        eventLocation = str(fields['rooms-to-book'])
        eventContent = 'Booked for:  '+ str(fields['booking-name'])
        createGoogleCalendarEvent(context, email, password, calendar_url, startDateTime, endDateTime, eventTitle, eventLocation, eventContent)

And that should be that.  As long as all your URLs, emails, passwords,
and fields in your form are suitable, this should work a treat.  Note
that the start-date-time and end-date-time fields are date/time fields
in your Form Folder and converting to HTML4() makes them into Google's
format.  Additional info can be added in the eventContent variable, and
that'll turn up in the Description in Google Calendar.

For added spice...
~~~~~~~~~~~~~~~~~~

Just add a web interface to your Google Calendar to your Plone site (eg
in a normal Plone page; watch out for iframe filtering) and let people
book themselves into things.  Would be great to see PFG know when a
Google Calendar event was on (and stop people submitting) but it's a bit
much just for now.

.. _GoogleCalendar.py: {static}/files/GoogleCalendar.py
