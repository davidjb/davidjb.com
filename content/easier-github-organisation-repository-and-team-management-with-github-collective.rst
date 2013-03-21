Easier GitHub organisation, repository and team management with github-collective
#################################################################################
:date: 2012-06-22 12:17
:author: davidjb
:category: IT
:tags: collective, github, ini, jenkins, management, organization, plone, script
:slug: easier-github-organisation-repository-and-team-management-with-github-collective

Have you ever felt that administering your GitHub organisation (or
organization, depending from where you hail), its repositories, teams,
and service hooks has become a tedious task and that you'd rather be
doing something else?  Maybe you're of the mindset that there should be
a better way of doing things - a way that involves specific,
version-controlled configuration and less repetition (less
clicky-clicky).  The good news is that there is -- `github-collective`_!

This is a script, written in Python, that utilises `GitHub's JSON-based
API`_ to allow you to construct an ini-style text-based configuration
representing your GitHub organisation and have this sync to create
repositories and service hooks for said repositories, teams, and
configure access rights.  At present, this works *from* your
configuration *to* GitHub (not vice versa at present). You may already
know this as what's powering the `GitHub Collective`_ to manage
repositories and teams, especially if you're in the Plone community.

An `example configuration`_ lives within its source code repository, and
similarly, the configuration that `powers the Collective`_ is available
also. Effectively, you define different types of sections ([team],
[hook], [repo]) and these will correspond to certain things being
created on GitHub via the API.

Our implementation
------------------

We at the James Cook University `eResearch Centre`_ have deployed this
for use against our `GitHub organisation`_ and our workflow looks like
this:

#. Users are able to fork a configuration repository and modify
   accordingly. For simplicity, since changes are frequently minor, I
   suggest using GitHub's "Edit this file" feature via the web.
#. User creates Pull Request for changes.
#. Administrator reviews and merges changes from Pull Request.
#. Configuration repository's service hook sends POST to Jenkins CI
   instance
#. Jenkins CI instance runs the *github-collective* script upon
   receiving this hook.
#. Changes to configuration get enacted on GitHub.

This process is similar to what happens for the Collective, except that
our service hook and Jenkins take care of making the changes happen,
rather than a periodical cron job.

Our Jenkins job uses the \ `Jenkins Text Finder`_ plugin to search for
the regex "Traceback \\(most recent call last\\)" in the output to
determine success or failure.  This isn't the most elegant solution in
the world, but it's good enough for now.

For what it's worth, we have a total of 25 repositories; a similar
number of teams; give or take 12 staff members in total; and the end
result is that running *github-collective* once cached takes only around
6 seconds, including Jenkins overhead.  Unfortunately I'm unable to
provide our exact configuration, but for everything we do, I've
'anonymised' the configuration and included it back in the public
repository as examples. Happy to answer questions about what we're doing
too!

Thanks
------

All credit to Rok Garbas and Alex Clark for their work on this - it
works fantastically. I can only take credit for coming in later with a
few things necessary our deployment. *Github-collective* now supports
all GitHub API settings for repositories (thus allowing you to create
private repos - something critical for us, and set other metadata) and
post-receive service hooks (so you can easily manage hooks on GitHub).
That, and a hearty dose of end-user documentation.

.. _github-collective: http://pypi.python.org/pypi/github-collective
.. _GitHub's JSON-based API: http://developer.github.com/
.. _GitHub Collective: http://git.io/collective
.. _example configuration: https://github.com/collective/github-collective/blob/master/example.cfg
.. _powers the Collective: https://github.com/collective/collective.github.com/blob/master/permissions.cfg
.. _eResearch Centre: http://eresearch.jcu.edu.au
.. _GitHub organisation: http://git.io/jcu
.. _Jenkins Text Finder: https://wiki.jenkins-ci.org/display/JENKINS/Text-finder+Plugin
