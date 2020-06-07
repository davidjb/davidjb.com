Setting up a Shibboleth SP with FastCGI support
###############################################

:category: Web
:tags: Shibboleth, FastCGI

Good news!  The Shibboleth SP software features FastCGI authorizer and
responder applications for use with your favourite non-Apache and non-IIS
web server.  Unfortunately, the default distributions don't come with it
built by default.  I'm looking into why this is the case, but for now
here's how to rebuild the RPMs yourself.

**Note**: if you're just looking to download something that works and don't
want to rebuild things yourself, we have RHEL 6, x86_64 packages available
in a Yum repo at https://www.hpc.jcu.edu.au/rpm/.  You'll also need to trust
my RPM building skills.

For starters, download the latest Shibboleth SP package and recompile it
with FastCGI support.  Instructions below are for RHEL 6 or CentOS 6,
64 bit. Feel free to contribute how to rebuild for your platform and where
your FastCGI applications live.

#. Use the Vagrant configuration at
   https://github.com/jcu-eresearch/shibboleth-fastcgi/ to easily spin up a
   temporary VM to build the packages, or else run the underlying script
   https://github.com/jcu-eresearch/shibboleth-fastcgi/blob/master/rebuild.sh
   on a EL 6 machine.

#. Install the resulting package onto your target machine.

#. Test the FastCGI applications by running the following:

   .. code:: console

       /usr/lib64/shibboleth/shibauthorizer
       /usr/lib64/shibboleth/shibresponder

   They will run and then end immediately.  This is normal when running them
   on the command line and not under FastCGI.

#. Configure something (`Supervisor <http://supervisord.org>`_, ``spawn-fcgi``,
   or similar) to run both of the above FastCGI applications and start them
   running.  My Supervisor configuration looks like this:

   .. code:: ini

       [fcgi-program:shibauthorizer]
       command=/usr/lib64/shibboleth/shibauthorizer
       socket=unix:///opt/shibboleth/shibauthorizer.sock
       socket_owner=shibd:shibd
       socket_mode=0660
       user=shibd
       stdout_logfile=/var/log/supervisor/shibauthorizer.log
       stderr_logfile=/var/log/supervisor/shibauthorizer.error.log

       [fcgi-program:shibresponder]
       command=/usr/lib64/shibboleth/shibresponder
       socket=unix:///opt/shibboleth/shibresponder.sock
       socket_owner=shibd:shibd
       socket_mode=0660
       user=shibd
       stdout_logfile=/var/log/supervisor/shibresponder.log
       stderr_logfile=/var/log/supervisor/shibresponder.error.log

#. Note the ``socket_*`` options above. I went ahead and put the ``nginx``
   user into the ``shibd`` group to allow group access to the given sockets:

   .. code:: console

       usermod -G shibd -a nginx
       service supervisord restart
       service nginx restart

   If you want, you could configure them to run on a TCP socket instead,
   but then you'll need to think about firewall considerations rather than
   Unix permissions.  Fun either way.
 
#. Start the FastCGI applications.  In the case of using Supervisor, then
   this is what you should start; it will then automatically start the
   processes for you as per the above configuration.

#. Configure your front-end webserver to talk to these FastCGI applications.

If you're an Nginx user, then you'll probably be interested in the post
that I've written about `Nginx and Shibboleth <{filename}2013-04-22-nginx-shibboleth-fastcgi.rst>`_.
