Resolving an NS_ERROR_FILE_CORRUPTED error in Mozilla Firefox
#############################################################

:category: Tech
:tags: firefox, web, html, javascript, error

I use Mozilla Firefox as my browser and occasionally I've found that certain
resources (typically JavaScript or CSS files) may fail to load because of an
error ``NS_ERROR_FILE_CORRUPTED``, which is displayed in the console.  For me,
this is rarely seen, though I've experienced the issue a few times on
Trello.com and another on our corporate website CMS.  This has the effect of
preventing whatever that resource was from loading, so in the case of CSS it
won't display and in the case of JS it won't run.  On Trello, this resulted in
a fully broken page -- nothing displayed except the header because the whole
thing is a JS app, and on our CMS, the left-hand navigation was broken because
that depends on JS too.

To solve this issue, at least for these sites, I opened my console and did the
following::

    localStorage.clear()
    sessionStorage.clear()

and reloaded the page.  Clearing my cache, my browser's local storage or
restarting the browser **was not enough** -- I expect because the local
storage for these specific sites had become corrupted at some point.
Occasionally, running the two commands above actually produces an
exception with ``NS_ERROR_FILE_CORRUPTED`` in the console output::

    [Exception... "File error: Corrupted" nsresult: "0x8052000b (NS_ERROR_FILE_CORRUPTED)" location: "JS frame :: debugger eval code :: <TOP_LEVEL> :: line 1" data: no]

In this case, re-running the commands again worked and resolved the issue.

Over time I've switched between stable to Developer Edition and eventually to
Nightly, and I also actively use tools to block cross-domain resources,
trackers and so forth.  I haven't looked into the specifics because the issue
is so sporadic and now easily solved, but I may if the issues persist.
