Putting a NASA Human Space Flight Sightings RSS feed into your calendar program
###############################################################################
:date: 2011-05-14 07:34
:author: davidjb
:category: Programming
:tags: nasa, pipes, sightings, space, yahoo, yahoo pipes
:slug: putting-a-nasa-human-space-flight-sightings-rss-feed-into-your-calendar-program

I stumbled upon `NASA's space sightings page`_ a little while ago. For
those of you that don't know, it's a great site that lists opportunities
to view satellites that will be visible in your location and when/where
to look to see them. Amongst the fact this service exists and is free, I
was amazed (and thankful!) that it actually lists lots of different
locations, one of which is where I like in regional Australia.

It's a great setup and they offer an RSS feed for each location which
keeps you updated. That's great, but if I'm trying to manage my time, I
don't really want to have be porting information between my Google
Reader and my Google Calendar manually. This wasn't a problem when I
wanted to insert one or two records into my calendar, but since this
feed always gets updated, it's clogging my Reader and less useful this
way.

Never to let a good thing go, I decided to resolve this issue by using
my new favourite tool, `Yahoo Pipes`_. Read on for how to access.

If you've not heard of Yahoo Pipes, I encourage you to go and take a
look. It's not exactly the easiest tool to use, granted, but it is
extremely powerful for as they say "rewiring the web" (oh, it's FREE so
you don't need to use your own computing resources!). There are a number
of oddities in how it does business, but the end result is extremely
useful.

So back to what I've built, check out
`http://pipes.yahoo.com/pipes/pipe.info?\_id=853d413076c16a20cc0c219188158033`_
for the Pipe. Here's the instructions:

#. Go to `http://spaceflight.nasa.gov/realdata/sightings/`_ and locate
   the RSS feed for your location
#. Make note of your location's time offset, plus or minus hour many
   hours GMT.

#. Once you have these, go to my Pipe at
   `http://pipes.yahoo.com/pipes/pipe.info?\_id=853d413076c16a20cc0c219188158033`_
   and input the URL and time offset in the relevant boxes
#. Click 'Run Pipe'. If successful, you should see a list of sightings
   (assuming they exist for your location and time!).
#. Click onto 'More options' on the left-hand side and choose 'Get as
   iCal'. Copy this URL into your calendaring product, like Google
   Calendar, and enjoy!

Note that you'll need to update your time offset when/if you change into
or out of daylight saving time - you can just go back to my Pipe and do
that to get your new calendar URL. I might see what I can do in the
future about this, but since my location doesn't have daylight saving,
you can understand why auto-changing isn't a feature :)

Enjoy this creation! As long as I stay interested, I'll keep it running
as best I can. However, given the nature of people's websites to change
formatting, I can't guarantee that NASA won't break my Pipe. Also, I
give no guarantees that this will work for anything but the one location
I live in because I don't test anything but this one RSS feed as an
input.

.. _NASA's space sightings page: http://spaceflight.nasa.gov/realdata/sightings/index.html
.. _Yahoo Pipes: http://pipes.yahoo.com/pipes/
.. _`http://pipes.yahoo.com/pipes/pipe.info?\_id=853d413076c16a20cc0c219188158033`: http://pipes.yahoo.com/pipes/pipe.info?_id=853d413076c16a20cc0c219188158033
.. _`http://spaceflight.nasa.gov/realdata/sightings/`: http://spaceflight.nasa.gov/realdata/sightings/
