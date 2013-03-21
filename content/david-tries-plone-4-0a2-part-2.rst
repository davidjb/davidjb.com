David tries Plone 4.0a2 (Part 2)
################################
:date: 2009-12-08 16:21
:author: davidjb
:category: Plone
:tags: alpha, demo, new, plone, sunburst, test, theme, ubuntu
:slug: david-tries-plone-4-0a2-part-2

Rightio!  So we've got Plone 4.0a2 installed and up and running.  Boy,
she looks sweet:

-  The new Plone site setup is flawlessly simple.  No more ZMI for those
   of us that don't want to use it.  It'll always still be useful, but
   having Plone throw up a simple, no no-nonsense front-end installer is
   just what it needed.  Other PHP based CMSes always had it too easy
   ;-)
-  Editing view:  clearer tabs at the top (no idea how many clients miss
   those, me included to start!) and resizable editing fields.  Great. 
   TinyMCE as the editor -- just what the doctor ordered as Kupu just
   wasn't quite up to task.  (Note that I'm using Wordpress with
   TinyMCE, so I could be a little biased).  Still needs work with the
   Image insert page, but anyway, in good time.

   -  Also, it seems like the "auto-link text from Plone content title"
      feature is gone.  I've opened a ticket, hopefully it'll get fixed:
      https://dev.plone.org/plone/ticket/9908
   -  Good to see the Resource Types for TinyMCE are simpler than Kupu. 
      Wow it was it a mission to add a new type of Folder-ish content
      and not de-select the rest of everything in the process in its
      multi-select box widget.

-  Pop-up overlays inside Plone: very cool.  Saves an entire page reload
   (I would hope so...) so a thumbs up from me!
-  Better search options and collapsed options on the form.  I saw the
   latter as an add-on from ages ago and thought it'd be a good thing to
   have.  Nice to see it (or similar) included by default.  Those search
   options were daunting.
-  Email addresses as logins!  Another feature that users keep asking
   about that's included.
-  User rego fields -- something very promising as I've been
   looking/hoping to move to a less-fixed way of managing user profile
   attributes in Plone.  Goodo.

That's about a wrap from me.  Looking good so far; a lot of smaller
issues are getting sorted.  Cheers to all those developers for all the
hard work so far.  If I knew more, I'd be helping out more than I am
now.
