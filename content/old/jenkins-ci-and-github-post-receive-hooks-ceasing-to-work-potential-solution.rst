Jenkins CI and GitHub post-receive hooks ceasing to work (+ potential solution)
###############################################################################
:date: 2012-06-19 09:11
:author: davidjb
:category: GitHub 
:tags: ci, git, github, jenkins
:slug: jenkins-ci-and-github-post-receive-hooks-ceasing-to-work-potential-solution

All projects fail
-----------------

Recently our Jenkins CI system began having issues with failing to
correctly accept post-receive hook POST requests from GitHub, even
though it was working fine. Without thorough testing, I can only really
see that the issue was related to upgrading Jenkins and/or the relevant
Git and GitHub plugins. Thankfully, with even newer versions of the
above, it has started working again. So, to those with issues, I offer
this KGS (Known Good Set) of versions for your help:

-  Jenkins 1.470
-  Jenkins GIT plugin 1.1.19
-  github-api 1.28
-  GitHub plugin 1.4

Some projects work
------------------

On a separate note, if you're having trouble with just one of your
Jenkins projects not accepting post-receive hooks when others are
working fine, then check the your repository URL. I found that one of my
projects had the URL::

    git@github.com:davidjb/my.project

which is notably missing the the ".git" from the end. Whilst Git accepts this
as a valid URL for cloning a repo, the Jenkins integration doesn't match the
hooks when coming in. This one is worthwhile checking too if you're just having
issues with individual projects.

Debugging
---------

For both of the above issues, debugging can help a bit -- `follow
instructions`_ for adding a logger and examine the output. In my case
for when some projects were working and some weren't, the one that
wasn't working didn't get 'poked' in the logs. If you don't see this,
but you do see the POST request coming into Jenkins, then check your
project/job configuration.

.. _follow instructions: https://wiki.jenkins-ci.org/display/JENKINS/Github+Plugin#GithubPlugin-Troubleshootinghooks
