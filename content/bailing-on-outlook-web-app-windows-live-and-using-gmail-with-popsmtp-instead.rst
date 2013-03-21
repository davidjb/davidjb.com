Bailing on Outlook Web App (Windows Live) and using Gmail with POP/SMTP instead
###############################################################################
:date: 2011-01-05 12:33
:author: davidjb
:category: IT
:tags: email, freedom, gmail, live, microsoft, outlook, pop3, smtp
:slug: bailing-on-outlook-web-app-windows-live-and-using-gmail-with-popsmtp-instead

I'm not a fan of Microsoft's solutions for mail (Exchange, Outlook,
Outlook Web Access, etc) because they simply aren't as smooth as other
alternatives. In my case, my weapon of choice is Gmail for all my mail.
Unless you really like the old-school style popup windows and Web 1.0
feel of Microsoft's options, you're probably opting for something else,
too. Now, there's no helping my institutional mail account as they've
disabled all standards-compliant forms of access (POP, IMAP, SMTP; short
of going down the route of `DavMail`_). But, that said, there **is**
hope to be had for my personal account, which is using "Outlook Web App"
or whatever the hosted version of Hotmail is really called. Here's how
you can connect via POP and SMTP.

This works for me on my tertiary institution's Microsoft-hosted Outlook
solution, so it may or may not work on yours (or work if you're not
using a 'hosted' option). Try it and see!  All settings and details I'm
providing here should work with any mail app, but I'm specifically using
Gmail.

Before we begin
~~~~~~~~~~~~~~~

Find your POP/SMTP server details by first logging into your Outlook Web
account as normal, and then clicking the drop-down arrow on the Help
icon (it's a "?" icon) on the right-hand side.  Click "About" and scroll
down until you find "External POP setting" and "External SMTP setting". 
Make a record of these details (or just keep this popup open while you
configure away).  Apparently the addresses can be different for users on
the same domain, so if your friends are trying this, make sure they
follow the same process.

As a side note, if you're using something that supports IMAP (like
Thunderbird), then you'll find the IMAP settings for Outlook Web under
the About settings too.  Gmail doesn't (yet), hence we're using
POP/SMTP.

POP3 - Downloading your mail
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Go into Gmail and find your account settings (Settings > Accounts)
   and click on 'Add a mail account you own'.
#. Enter your email address, and click 'Next Step'
#. Specify the following details:

   #. Username: your full email address
   #. Password: your institutional or other password
   #. POP Server: [what setting you found before]
   #. Port: [what setting you found before]
   #. Check "Always use a secure connection (SSL) when retrieving mail".
   #. Other options are up to you.

#. Click 'Save Changes' and Gmail should now start checking your mail
   via POP.  Look in the accounts listing to make sure everything is
   working.

SMTP - Sending your mail
~~~~~~~~~~~~~~~~~~~~~~~~

#. Go into Gmail and find your account settings (Settings > Accounts)
   and click on 'Add another email address you own'.
#. Enter your name and email address you'd like shown on the mail you
   send and click 'Next Step'  This should be the same as the email
   above.
#. Select "Sent through xxx.com SMTP servers (recommended for
   professional domains)", and enter these details:

   #. SMTP Server:  [what setting you found before]
   #. Port: [what setting you found before]
   #. Username: your full email address
   #. Password: your institutional or other password
   #. Check "Always use a secure connection (SSL) when sending mail".

#. Click the 'Add Account' button and Gmail will check your settings. 
   Everything should be fine unless your domain settings disallow you
   from this sort of access.
#. Try and send an email!  You should be able to do so successfully.

Wrapping up
~~~~~~~~~~~

Log out of Outlook Web App and forget it even exists.  Problem solved.

Now if only things were this easy for Microsoft's BPOS / Exchange for my
university...

.. _DavMail: http://davmail.sourceforge.net/
