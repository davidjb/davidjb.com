CSS: Internet Explorer and Self-Imposed Limitations (+ Plone)
#############################################################
:date: 2010-01-28 11:52
:author: davidjb
:category: Web
:tags: bug, css, IE, issue, limitation, plone, problem, styles, stylesheets
:slug: css-internet-explorer-and-self-imposed-limitations-plone

Microsoft and IE are insane.  Yes, we all knew this, but
here's the proof::

    IE won't accept more than 30 style sheets to be loaded via <style> tags within a single page.  

Insanity?  Yes.  It's made even worse by the fact they openly admit this
lunacy!  See the relevant `support article`_ from MS as proof.

Good gosh.  I can just imagine the staff (managers, probably) from
Microsoft thinking "30 style sheets?  Who needs more than 30 style
sheets?  Just kill off anything after that and those sites that use that
many can *BURN*."

I mean, really, who does need 30 style sheets?  Never mind that a lot of
CMSes (like Plone, or Drupal) have CSS debug modes that can be turned on
in order -- you guessed it -- debug the styles.  Add this to the fact
that IE gives two middle fingers to standards compliance and not only
can you not have it understand your CSS correctly, but you can't even
**debug** it normally when IE screws up!  So, this solves the issue of
my ploneCustom.css file wouldn't load -- it's the last CSS import being
brought in from portal\_css in Plone.

This issue is admitted by them and has been around since\ **Internet
Explorer 4**.  Yes, that's right, back from when the dinosaurs roamed
the earth and array indices only went to 30.  Get real IE developers and
Microsoft.

And to anyone who's reading this on IE:  get a `real`_ browser.

.. _support article: http://support.microsoft.com/default.aspx?scid=kb;en-us;262161
.. _real: http://getfirefox.com
