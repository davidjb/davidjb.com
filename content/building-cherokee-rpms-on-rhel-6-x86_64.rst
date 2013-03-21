Building Cherokee RPMs on RHEL 6 (x86_64)
#########################################
:date: 2011-05-31 12:27
:author: davidjb
:category: IT
:tags: build, cherokee, el, red hat, rhel, rpm
:slug: building-cherokee-rpms-on-rhel-6-x86_64

`Cherokee`_ is a fast web server and something I'm looking
at using instead of my current Apache installs in order to squeeze a bit
(lot) more juice out of my web services.

You can easily install Cherokee via its automated scripting and that's
really useful.  Unfortunately, since I'm within a RedHat environment,
init scripts and other useful aspects that come packaged with Apache
don't get installed when installing from source. Now, there's a lot of
activity regarding installing the latest packages for Ubuntu, but not
much of anything recent for RHEL (current Cherokee is 1.2.98 and latest
RHEL packages are 1.2.1).  Since development of Cherokee appears to be
moving very fast, having the most recent version is always a good choice
for bug fixes and new features.

So, how about creating packages for RHEL 6?  The good news is that
Fedora does have a git repo for the RPM spec and relevant scripts, and
that repo has a branch for EL6.

That said, there's no guarantee this branch will continue to work for
future Cherokee or EL versions, so if there's a problem running the
following RPM build, then someone will have to fix whatever error takes
place. That said, for now, on version 1.2.98 of Cherokee, things work,
as far as I can tell for Cherokee (also, disclaimer: I'm not an RHEL/RPM
expert). That said, here's what I did:

.. code:: bash

    yum install rpm-build spectool pam-devel gettext
    cherokee\_version=1.2.98
    git clone git://pkgs.fedoraproject.org/cherokee.git -b el6
    cp cherokee/\* \`rpm --eval '%{\_sourcedir}'\`
    cd cherokee
    sed -i -r "s/(Version:\\s+)[0-9\\.]+/\\1\`echo $cherokee\_version\`/g" cherokee.spec
    spectool -g -R cherokee.spec
    rpmbuild -ba cherokee.spec
    cd \`rpm --eval '%{\_rpmdir}'\`
    cd x86\_64
    ls -lah
    yum install cherokee-\*

.. _Cherokee: http://www.cherokee-project.com/
