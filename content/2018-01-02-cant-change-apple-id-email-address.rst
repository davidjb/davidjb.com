Can't change Apple ID email address? Try waiting 30 days
########################################################

:category: Tech
:tags: apple, web, error, email

Like it or not, Apple plays a critical part in the app-based economy these
days.  Part of this is having an Apple Developer account in order to release
apps to the App Store™️, and in order to get an Apple Developer account you
need an Apple ID.  In order for the Apple ID to be able to become an Apple
Developer account, it needs to be considered to be "over 18", even if it's a
company account and a Date of Birth makes no sense whatsoever.  This is where
I got stuck.

Let's say you don't realise this "18+" restriction and create an Apple ID with
an arbitrary date.  In my case, I made my company account a "minor" which
meant that requests to create an Apple Developer account fail with a
generic and non-sensical error message about how you can't proceed.  After
searching for the error, I figured out others had the same issue because they
were personally underage.

Okay, so trying to change the birthdate in the Apple ID is possible, but has
no effect on the Apple Developer system.  Now, we could try and contact Apple
to change the birthdate but that involves waiting for a call and so on and
they probably can't even fix it, so the next best option is to close the
original Apple ID and recreate it.  Sure, this works -- almost.  The secondary
issue that you'll find is that if you try and use the same *email address* as
your first Apple ID, you won't be able to use it, even if you *fully* closed
the first account.  Why?  According to Apple staff, their accounts system
keeps your account data for another 30 days "just in case you change your
mind" and need to re-open it.  Well, good to know, but I'm on a deadline.

Unfortunately, the only way forward here is to use another email address
temporarily and wait out the 30 days.  Then, you can log into your Apple ID
and change the email address to the one from the first account.

In short, some fun facts about Apple IDs:

* One per email address
* A closed Apple ID will stick around for 30 days after closure
* Closed Apple IDs can be retrieved within 30 days of closure
* Apple Developer accounts must have an age over 18 years (according to their
  birthdates)
* Apple Developer company accounts require a DUNS (Dun & Bradstreet) number
  that is correctly verified to proceed
* Changes in DUNS numbers require at least 14 days for D&B to update their
  database and might take another 14 days for Apple to get the new copy of the
  DUNS database.  Check the unofficial schedule at
  `<http://apple-duns.weebly.com/>`_.
