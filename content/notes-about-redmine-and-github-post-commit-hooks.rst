Notes about Redmine and GitHub Post-commit Hooks
################################################
:date: 2011-12-14 10:50
:author: davidjb
:category: GitHub 
:tags: code, commit, dvcs, git, github, redmine, vcs
:slug: notes-about-redmine-and-github-post-commit-hooks

We're currently using Redmine for our project tracking and recently have
wanted to have our GitHub projects automatically get updated within
Redmine. A post-commit hook to the rescue!

#. Download and install this super plugin:
   https://github.com/koppen/redmine_github_hook and restart your
   Redmine instance.
#. Set up your local Git instance for your repository.  This is simple,
   but you need to follow these steps or else pulling your changes down
   won't work:

   .. code:: bash

       git clone --bare git://github.com/davidjb/123.git
       cd 123.git
       git remote add origin git://github.com/davidjb/123.git

#. Configure your Redmine project's Repository to be this Git directory.
   (This is a given, but just so you know.)
#. Configure your GitHub repository to have a 'Post-Receive URL' service
   hook and point that at your Redmine URL like so:

   .. code:: bash

       https://davidjb.com/redmine/github_hook?project_id=myproject

   where ``myproject`` is your Redmine project ID. You can ignore the
   ``?project_id=myproject`` if your GitHub repository name is the same
   as your Redmine project ID.

Beware the pre-existing Redmine service hook in the current iteration of
GitHub (circa 2011) - it effectively doesn't do anything. This may
change in the future, but until then, this works fantastically.

