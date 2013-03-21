DateTime in Python/Zope/Plone is painful
########################################
:date: 2009-06-19 13:50
:author: davidjb
:category: Python
:tags: comparison, date, plone, problem, python, time, zope
:slug: datetime-in-pythonzopeplone-is-painful

Alright, now for today's problem:  why do two dates that look different
when outputted actually end up being the same date?

**Answer:** I'm not sure, but I'm pretty sure it's got something to do
with the wacky support the above-mentioned 3 products have for
timezones.

**The background:** Plone stores a DateTime object to record a user's
last login time.  It doesn't really matter what's purpose is, because
Plone (this time) isn't at fault.  The DateTime gets stored, no
worries.  The problem arises when you try to put that value back into a
DateTime object.  Now, I'd have thought it'd be as simple as doing this:

.. code:: python

    dt = DateTime(member.getProperty('login_time'))[/sourcecode]

And realistically, it is.  Except that printing/using that value - at
least for me - results in a time that appears as UTC, but is reported as
being in my timezone (aka a time that's 10 hours behind since I'm
GMT+10).

**The fix:** the time still knows its timezone correctly, so just give
it a kick:

.. code:: python

    dt = DateTime(member.getProperty('login_time'))
    dt = dt.toZone(dt.timezone())

Amazingly, doing a comparison (using cmp) between the original DateTime
object and it's 'corrected' version actually shows that they're the
same.  Uhuh.
