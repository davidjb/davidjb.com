mr.scripty - my new best friend
###############################
:date: 2012-02-24 08:34
:author: davidjb
:category: Python 
:tags: awesome, buildout, python, recipe
:slug: mr-scripty-my-new-best-friend

If you're working with Buildout, then check out `mr.scripty`_, a
fantastic Buildout recipe that allows you to use Python code in
functions within its options.  This means that - in the few instances
I've used it so far - have conditional statements regarding effectively
anything.  

In the two examples I added to the `source documentation`_, I go and
configure download links based upon architecture and separately,
configure some (Java) environment variables based upon which directories
exist (eg to handle different Linux distributions that might be
running). This is only the start, but it's a fantastic one.

Amazing I hadn't gone looking for this earlier. Anyone know of any other
Buildout awesomeness out there?

.. _mr.scripty: http://github.com/collective/mr.scripty
.. _source documentation: https://github.com/collective/mr.scripty/blob/master/mr/scripty/README.txt
