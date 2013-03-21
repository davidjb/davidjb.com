User-selectable Themes In Plone
###############################
:date: 2009-06-25 13:10
:author: davidjb
:category: Plone 
:tags: plone, skin, theme, zmi
:slug: user-selectable-themes-in-plone

It's something I came across a while ago, but wasn't exactly something
that stayed in the fore-front of my mind: how to let users choose or
select a theme (arbitrarily) on a Plone site.  Normally, I stick to
having one theme per site for continuity but a new theme-test site for
clients is an exception.

If you were to search Google for the right terms, you'll find out how to
let this happen, but I ended up having to go hunt it down myself. 
Hopefully this entry will help people (if I go and include as many terms
as I think I or someone else might look for!).

How
~~~

Head to the ZMI as an administrative user (/manage), and then to
portal\_skins.  Under the Properties tab, you'll find a Boolean option
called "Allow arbitrary skins to be selected".  You guessed it; turn to
it on and save.

Your users now have a drop-down menu in their personal preferences for
changing the theme.  Install some additional themes and away you go.

**Note:** seems like this feature doesn't work well or I'm not using it
right.  Changing the theme for one user changes it for everyone..hmm. 
Probably the reason the option's hiding in the ZMI!
