iMessage and Google Talk not working on macOS High Sierra (10.13)
#################################################################

:category: Tech
:tags: mac, accounts, messages, imessage, Google Talk

I recently upgraded my computer to macOS 10.13 and found that my iMessage (in
Messages.app) wasn't working entirely and that Google Talk in the same app
would only receive messages and not send.

Starting with the Google Talk issue, that's an easy one.  Apple has removed
"official" support for Google Talk from Messages.app but they've clearly left
the code in place that allows your old account to login, connect and actually
receive messages, but helpfully added a dialog that says "Your message could
not be sent.  Support for the targeted service Google Talk has been
discontinued".  It looks like this:

.. image:: https://i.imgur.com/Hte2K7f.png

Very helpful, Apple, thank you.  Unfortunately, they also took away the
ability for me to sign out of my Google account in Messages (these accounts
were separate from Internet Accounts in macOS 10.12 and below); again, very
helpful indeed.

Now, as for iMessage, Messages.app initially claimed I was logged in (in
Accounts) but logged out in the main messages UI.  Trying to log out in the
Accounts settings appeared to work, but wouldn't let me log back in, no matter
how I tried. Several minutes after trying the username/password combination, a
red error stated "problem with authentication" (or similar) and that was it.

To get out of this mess, I ended up removing my Google and iCloud accounts
entirely from Internet Accounts (in System Preferences).  At this point,
Messages.app then identified that I had been signed out of Google and stopped
showing me as logged in, prompting me to log in with iMessage instead.  At
that point, iMessage wouldn't login either (with no error message, but logging
in with a fake username and password showed auth was working as that got
rejected!).

In a last dith effort, I then restarted my computer.  Something finalised its
installation on reboot (taking around 5-10 minutes to "finish") and then on
finishing boot, all is well again.  I was able to successfully log into iCloud
again and then into iMessage and have it work.  Google Talk is gone from
Messages.app (though the Accounts preferences occasionally have the entry show
up again, albeit unfunctional, weird!) and we can all move on.
