Integrating Nginx and a Shibboleth SP with FastCGI
##################################################

:category: Web
:tags: Nginx, Shibboleth, FastCGI

New location!
~~~~~~~~~~~~~

The canonical place for this documentation is now the
`nginx-http-shibboleth
<https://github.com/nginx-shib/nginx-http-shibboleth>`_ custom Nginx module
GitHub repository.  All updates will be reflected there, and as a result,
this page **has** become **severely** outdated.  Please contribute to that
repository!

Original post
~~~~~~~~~~~~~

.. note::

   With changes in Nginx after version 1.5.4, the auth request module is now
   built in.  This means the following instruction have changed, yet again.


**tl;dr**:  You can have Nginx with Shibboleth. Rebuild Shibboleth with 
FastCGI support, and recompile Nginx with a custom module.  You can now
run the Shibboleth FastCGI authorizer and responder applications and
successfully authenticate!

.. contents::
   :local:
   :backlinks: none


Background
~~~~~~~~~~

There's a **lot** of posts around the web asking about integrating
Shibboleth and Nginx, and so far as I can ascertain, the responses have
been fairly empty and a resounding "NO".  Here's what I've gathered so far.

Shibboleth supports Apache and IIS by default, but not Nginx.  The closest one
gets to support is via FastCGI, which Shibboleth `does have
<https://wiki.shibboleth.net/confluence/display/SHIB2/NativeSPFastCGIConfig>`_
but the default distribution needs to be rebuilt to support it.  Nginx has
support for FastCGI responders, but not for `FastCGI authorizers
<http://www.fastcgi.com/drupal/node/22#S6.3>`_.  This is where things get
interesting (and eventually change).

So, that said, Nginx does have support for sub-requests for allowing access,
and the `Auth Request <http://mdounin.ru/hg/ngx_http_auth_request_module/>`_
gets very close in terms of providing the functionality we need for a FastCGI
authorizer.  However, that module only allow(ed) for the sub-request to
respond with an *allow* or *deny* response.  But, some minor changes I was
able to make to my fork that Auth Request module allows the auth request to
follow the specification.

Cautionary note
^^^^^^^^^^^^^^^

I should note that my custom Auth Request module for Nginx doesn't 
presently feature support for sending the FastCGI authorizer the original
request body, and likewise, doesn't support sending the authorizer's response
body back to the client.  For Shibboleth authorisation, however, these two
are inconsequential as only HTTP redirections and HTTP headers (cookies)
are used for authentication to succeed.

Contributions are welcome at the above repository.  I'm currently looking to
have my improvements merged back into the main plugin, too.


Install the Shibboleth SP with FastCGI support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Check out my post regarding `Shibboleth and FastCGI <{filename}2013-04-22-shibboleth-fastcgi.rst>`_.  It will step you though either how to install or build
the Shibboleth SP for your system and get the FastCGI applications up and
running.

Once you're done, make a note of the socket where the applications can be
accessed. We'll use this information next.


Nginx with FastCGI Authorizer support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The next step is sorting out Nginx with suitable support for FastCGI
authorizers.  As mentioned above, I was able to delve into Nginx and make my
fork of that Auth Request module allows the auth request to follow the
specification (see caveat above about request/response bodies).

#. Compile Nginx with the custom Auth request module and the
   `Headers More <http://wiki.nginx.org/HttpHeadersMoreModule>`_ module 

#. Once you've successfully got Nginx compiled with my custom auth request
   module, then you're ready to configure it all up.

#. Configure one or more servers within your Nginx configuration like so.
   You'll need the socket information for your FastCGI Shibboleth SP
   applications.

   The ``proxy_pass http://localhost:8080`` can be replaced
   with whatever application or configuration should be receiving the
   Shibboleth attributes as headers.  In my case, port 8080 is running Plone,
   a Python-based CMS, but you might anything (PHP, FastCGI, etc) here.
   Essentially, this is what would normally be the backend configured against
   ``AuthType shibboleth`` in Apache.

   .. code:: nginx

      server {
          listen 443 ssl;
          ...

          #FastCGI authorizer for Auth Request module
          location = /shibauthorizer {
              internal;
              include fastcgi_params;
              fastcgi_pass unix:/opt/shibboleth/shibauthorizer.sock;
          }

          #FastCGI responder for SSO
          location /Shibboleth.sso {
              include fastcgi_params;
              fastcgi_pass unix:/opt/shibboleth/shibresponder.sock;
          }

          #Resources for the Shibboleth error pages. This can be customised.
          location /shibboleth-sp {
              alias /usr/share/shibboleth/;
          }

          #A secured location.  Here all incoming requests query the
          #FastCGI authorizer.  Watch out for performance issues and spoofing.
          location /secure {
              more_clear_input_headers 'Variable-*' 'Shib-*' 'Remote-User' 'REMOTE_USER' 'Auth-Type' 'AUTH_TYPE';

              #Add your attributes here. They get introduced as headers
              #by the FastCGI authorizer so we must prevent spoofing.
              more_clear_input_headers 'displayName' 'mail' 'persistent-id';
              auth_request /shibauthorizer authorizer=on;
              proxy_pass http://localhost:8080; 
          }

          #A secured location, but only a specific sub-path causes Shibboleth
          #authentication.
          location /secure2 {
              proxy_pass http://localhost:8080; 

              location = /secure2/shibboleth {
                  more_clear_input_headers 'Variable-*' 'Shib-*' 'Remote-User' 'REMOTE_USER' 'Auth-Type' 'AUTH_TYPE';
                  #Add your attributes here. They get introduced as headers
                  #by the FastCGI authorizer so we must prevent spoofing.
                  more_clear_input_headers 'displayName' 'mail' 'persistent-id';
                  auth_request /shibauthorizer authorizer=on;
                  proxy_pass http://localhost:8080; 
              }
          }
      }

   An explanation about the above is provided in the comments.  I should note
   that:

   * The first 3 locations are pure boilerplate for any host that requires
     Shibboleth authentication, so you can (and should!) put these into an
     ``include``-able configuration file and reuse them.

   * The ``/shibboleth-sp`` location is purely there to help your default
     install.  If you customise your error pages, feel free to change or delete
     this location.

   * Take note of the ``more_clear_input_headers`` calls. As the Shibboleth
     authorizer will inject headers into the request before passing the
     request onto the final upstream endpoint, you **must**
     use these directives to protect from spoofing.  You should expand the 
     second call to this directive when you have more incoming attributes 
     from the Shibboleth authorizer.  Or else beware...

   * The ``/secure`` location will ask the FastCGI authorizer for attributes
     for **every** request that comes in. This may or may not be what you
     want.  Keep in mind this means that each request will have Shibboleth
     attributes dropped into the request for sending onto backend services,
     and this will happen every time.  Did I mention for **every request**?

   * The ``/secure2`` location only asks the FastCGI authorizer for auth
     on a (very) specific sub-path.  Only upon the user hitting this specific
     URL will the authentication process be triggered. This is a smarter
     authentication technique to avoid extra overhead -- set the upstream
     for the specific sub-path to be somewhere an application session is
     created, and have that application session capture the Shibboleth
     attributes.

     Notice how the rest of the application doesn't refer to the authorizer.
     This means the application can be used anonymously, too. Alternatively,
     you can configure the ``requireSession`` option to be fa

   * Adding the ``auth_request`` line into a location isn't all you need to
     do to get the FastCGI authorizer to recognise your path as Shibboleth
     protected.  You need to follow the instructions below and take care.

#. Save the configuration and follow the next section.  You're almost done.


Configuring Shibboleth to recognise secured paths
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Typically, within Apache, you can tell Shibboleth which paths to secure by
using something like:

.. code:: apache

   <Location /secure>
       ShibRequestSetting authType shibboleth
       ShibRequestSetting requireSession false
   </Location>

However, the FastCGI authorizer for Shibboleth operates without such directives
and thus path protection needs to be configured like it would be for IIS,
using the ``<RequestMapper>`` configuration.  The same options are accepted
within this section of the ``shibboleth2.xml`` configuration file, it's just
that you need to know where to put them.  So let's do that.

  
#. Configure your ``shibboleth2.xml`` file like so.  Find the ``RequestMapper``
   element and replace it with something like the following:

   .. code:: xml

       <RequestMapper type="XML">
           <RequestMap>
               <Host name="example.com"
                     authType="shibboleth"
                     requireSession="true"
                     redirectToSSL="443">
                   <Path name="/secure" />
                   <Path name="/secure2/shibboleth" />
                   ...
               </Host>
               ...
           </RequestMap>
       </RequestMapper>

   Some notes:

   * The Shibboleth FastCGI authorizer needs to see ``authType`` **and**
     ``requireSession`` configured for the resultant path.  If they are not
     present, then the authorizer will ignore the path it is passed and
     the user will not be prompted for authentication (and you **will**
     tear your hair out because no logging takes place!).

   * ``<Path>`` names are **case sensitive** here.  You have hereby been warned!
     -- although this shouldn't be too surprising to you hopefully.

   * You can use other configuration items like ``<HostRegex>`` and
     ``<PathRegex>`` and ``<AccessControl``> to configure what happens to 
     requests.  Check out the documentation below - there's lots to learn. 

   * An interesting aspect here is that configuration is inherited downwards
     in the XML tree.  So, you could configure something like the ``authType``
     on a ``<Host>`` and have it apply to all paths beneath it.

     You don't need to do this, though.  You may put all the configuration
     attributes onto the ``<Path>`` element, or even move them up to
     higher levels in the tree if you want to reduce duplication.

   * Nested ``<Path>`` elements will see their path segments being greedy.
     So putting a path with ``name="shibboleth"`` within a path with
     ``name="secure"`` really translates to a path with 
     ``name="secure/shibboleth"``.  Whatever takes your fancy here.

#. Once you're done, then restart the Shibboleth daemon, ensure that you
   restart the Shibboleth FastCGI applications, and hard restart Nginx
   just to make sure it finds those sockets::

       service shibd restart
       supervisorctl restart shibauthorizer shibresponder
       service nginx restart

   Assuming, of course, that you're using Supervisor to run your applications.
   You should.  It's easy to work with and fun.  

#. Try loading up your Shibboleth protected URL.  If all goes well, then you
   should get a complete authentication cycle.  If not, check carefully through
   everything above.

Take a look at 
https://wiki.shibboleth.net/confluence/display/SHIB2/NativeSPRequestMapper
and
https://wiki.shibboleth.net/confluence/display/SHIB2/NativeSPRequestMap
for more information.

Warning
~~~~~~~

In order to stop yourself from tearing your hair out (very important to me
as I'm male), remember these things:

* The Shibboleth authorizer requires a ``<Path>`` to be correctly configured
  with ``authType`` and ``requireSession`` for auth to take place.  If you
  don't (or you do and forget to restart ``shibd``), then the authorizer will
  blindly return a ``200 OK`` status response, which equates to blindly 
  allowing access.  

* No logs will get issued anywhere by the way for anything related to the
  FastCGI applications (standard ``shibd`` logging does apply, however) so if
  you're testing for why the redirect cycle doesn't start, try killing your
  FastCGI authorizer and make sure you see a ``502`` error come back.  If you
  still get a ``200``, then your ``auth_request`` configuration in Nginx is
  probably wrong and the authorizer isn't being contacted.

* When in doubt, hard restart the entire stack, and use something like ``curl``
  to avoid browser caching.

Ahh, I feel calmer already.

Conclusion
~~~~~~~~~~

Phew.  That was an effort, wasn't it.  Please feel for me as I've had to type
all this up.  Feel free to help out with this documentation (my blog is open
source) or else feel free to shout links about it far and wide.

If you're skilled in the ways of Nginx, or else would (could) like to learn,
I'd like to improve on the work I've done with the auth request module.
If you're keen on saying thank you, your help participating on this would
be greatly appreciated.

So that's it.  Shibboleth and Nginx using the FastCGI Authorizer and Responder
specifications.  It works and can be done.  

Look ma, no Apache!
