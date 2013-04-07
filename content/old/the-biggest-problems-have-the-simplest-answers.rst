Buildout: the biggest problems have the simplest answers...
###########################################################
:date: 2009-09-03 15:57
:author: davidjb
:category: Buildout
:tags: buildout, centos, eggs, linux, plone, ubuntu, zope
:slug: the-biggest-problems-have-the-simplest-answers

..and how true that is.  Today's time consumer is directly related to
just 1 misplaced line of a buildout configuration (and presumably
something that's changed somewhere else).

The result
~~~~~~~~~~

After much hunting and hunting, it turns out my Zope2 Fake Eggs weren't
being generated.

On my long quest I had to go through downloading new packages and trying
to find something that had changed and even trying to establish new
virtual environments on different VMs.  Nothing would fix the problem. 
To rub salt in the wound, my desktop Ubuntu ran the buildout fine, so
methinks the underlying reason for the pain is something OS-related.

After many hours of debugging buildout output and trying to go through
the packages that seemed to be the cause (poor things, they were merely
bystanders, asking for dependencies), a few carefully-placed print
messages in the plone.recipe.zope2install package helped.

The cause
~~~~~~~~~

"Oh? what do you mean the install() function isn't being run?", I found
myself saying after the print messages showed what was happening.  The
fake eggs didn't exist because the Zope2 recipe, whilst being initiated,
hadn't yet actually been run.

So, thanks to the 'zope2' entry in the parts section of my buildout
being run after a whole lot of other sections, the other products never
had a chance.  Result: lesson learned -- put the zope2 section first,
and order matters!

Oddly enough though, it's never caused trouble before and obviously
there's a difference between Centos and Ubuntu.  Hmmm.
