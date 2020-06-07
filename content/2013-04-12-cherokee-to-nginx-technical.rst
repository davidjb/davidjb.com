Switching to Nginx from Cherokee: Techincal Guide
#################################################

:category: Web
:tags: Nginx, Cherokee, web, web servers

This is a follow up to a previous post on 
`Switching to Nginx from Cherokee <{filename}2013-04-11-cherokee-to-nginx.rst>`_.  Read that in case you're here and haven't already.

All information here on a server level is related to RHEL 6.  You will
need to change some instructions for Debian based systems.  CentOS
should be fine and needs only a minor URL change in the repo configuration.

#. Edit ``/etc/yum.repos.d/nginx.repo`` and add this::

       [nginx]
       name=nginx repo
       baseurl=http://nginx.org/packages/rhel/$releasever/$basearch/
       gpgcheck=0
       enabled=1

#. Run ``yum install nginx`` to install Nginx.

#. Start rebuilding your configuration files in Ngnix format. I achieved
   this by starting ``cherokee-admin`` (the Cherokee GUI interface)
   and stepping through the configuration one server, and one behaviour
   at a time until I was finished. Refer to `Configuration changeover`_
   below for helpful hints and configuration matching.

   This will take you some time.  It took me 2 days for about 15 servers,
   which isn't bad considering!  I think it's a testament to how similar
   the configuration between the two happens to be.

#. Stop Cherokee and start Ngnix once your configuration is ready:

   .. code:: bash

       service cherokee stop
       service nginx start

Configuration changeover
~~~~~~~~~~~~~~~~~~~~~~~~

Note that the following is a rough mapping of what you can use to convert
Cherokee configuration to Ngnix.  In the interests of not reproducing
information that's already on Ngnix's site, I've just linked to their
wiki.  Keep in mind this list isn't complete as it's just what I used for
converting my configuration.  Your requirements may be more complex.
The good news is that most things have a counter-part in both applications.

It's worth remembering that a lot of these aspects, whilst locking in place
within Cherokee, don't have to be configured at the same *level* within
Ngnix.  For instance, whils Cherokee requires you to specify ports to 
listen to at the server-configuration level (top), Nginx applies this
at a server_ level.

Also keep in mind that everything in Ngnix is inherited based upon the
nesting of the various http_, server_, location_ blocks within the
configuration.  This is particularly nice and helps reduce duplication
that you might have had originally with Cherokee.  So, if you find yourself
doing something like ``gzip on`` within Ngnix everywhere, maybe just
enable it server_-wide or http_-wide at that level, and just use 
``gzip off`` wherever you need it turned off.  Easy.

Some things like
listen_ might seem a little more verbose to start, since you may find
yourself repeating it a few times, but once you realise how it all works,
it's a lot more flexible across multiple host names or IP addresses.

If you've got more to add to this, feel free to fork my blog on GitHub
and submit a pull request.

Server-level
~~~~~~~~~~~~

===============         ===================================================
Cherokee option         Nginx option
===============         ===================================================
Ports to listen         listen_
Timeout                 client_body_timeout_, client_header_timeout_,
                        other \*_connect_timeout or \*_read_timeout options
Server Tokens           server_tokens_
User                    user_
Mime Types              Refer to ``/etc/ngnix/mime.types``
===============         ===================================================

vServer-level
~~~~~~~~~~~~~

======================= =========================================
Virtual server option   Nginx option
======================= =========================================
Virtual Server          server_ block
Virtual Server nickname server_name_
Document Root           root_
Directory Indexes       index_
Match nickname          server_name_
Virtual Server matching server_name_ (Use ``\~`` to specify regex)
Error logging           error_log_
Access Logging          access_log_
SSL Certificate         ssl_certificate_
SSL Certificate key     ssl_certificate_key_
======================= =========================================

Behaviour-level
~~~~~~~~~~~~~~~

================        ===================================================
Behaviour option        Nginx option
================        ===================================================
Behaviour               location_ block, if_ condition

Matching rule           Depends. location_ is a good start for matching URI
                        strings, regex, directory names and paths. Watch 
                        out for if_ statements within location_.

                         * Directory: location_
                         * Extensions: location_
                         * Regular Expression: location_
                         * Header: if_ (in server_ or location_)
                         * Exists: try_files_ or if_
                         * HTTP Method: if_ against $request_method_
                         * Incoming IP/Port: None. Use correct server_ 
                           block
                         * SSL/TLS: Use specific server_ block (fastest),
                           or if_ against $server_port_
                         * Full Path: location_
                         * Connected from: if_ against $remote_addr_
                         * URL Argument: location_ or if_ against $args_
                         * GeoIP: See geo_ module

                        Try and simplify rules down. Odds are your rules
                        aren't complicated and don't need to be. Avoid
                        unnecessary regular expressions and use strings
                        only if possible.  Note that location_ blocks in
                        Ngnix will match on initial substrings by default.

                        Many things that you might have had to use
                        conditional *if*, *and*, *not* and *or* in Cherokee
                        can be done either by using regex instead or using
                        built-in logic in Ngnix.  For instance, use a
                        dedicated server_ blocks to handle HTTP and HTTPS
                        differently and avoid needing tonnes of if_
                        statements.

Handler                 Configuration (typically) within location_.
                        May move to server_ block if appropriate.

                         * None:  ``{}`` (empty brackets)
                         * List & Send: alias_ or root_
                         * Static Content: alias_ or root_
                         * Only Listing: Unknown.
                         * Redirection: return_ or rewrite_
                         * FastCGI: fastcgi_pass_ and fastcgi options
                         * SCGI: scgi_pass_ and scgi options
                         * uWSGI: uwsgi_pass_ and uwsgi options
                         * HTTP Reverse Proxy: proxy_pass and proxy options
                         * Upload Reporting: Unknown
                         * CGI: Not directly supported. Use uWSGI to wrap.
                         * Server Side Includes: ssi_
                         * Hidden Downloads: See 3rd party modules.
                         * Server Info: Unknown.
                         * MySQL Bridge: Not applicable.
                         * HTTP Error: return_
                         * Remote Administration: Not applicable.
                         * 1x1 Transparent GIF: empty_gif_
                         * Drop Connection: ``return 444`` (special code)

Transforms              gzip_, gzip_comp_level_ (more options here!)

Caching                 expires_, various ``_cache`` directives

Security                allow_, deny_

Restrictions            client_body_timeout_, client_header_timeout_,
                        other \*_connect_timeout or \*_read_timeout options

================        ===================================================


That's about it.  It's mostly a manual process to step through the
configuration and sort each rule out.  It's not quick so bring a cut lunch.
The good news though is that most things map almost exactly. Even regex.


.. _$request_method: http://wiki.nginx.org/HttpCoreModule#Variables
.. _$args: http://wiki.nginx.org/HttpCoreModule#Variables
.. _$remote_addr: http://wiki.nginx.org/HttpCoreModule#Variables
.. _$server_port: http://wiki.nginx.org/HttpCoreModule#Variables
.. _allow: http://wiki.nginx.org/HttpAccessModule#allow
.. _deny: http://wiki.nginx.org/HttpAccessModule#deny
.. _expires: http://wiki.nginx.org/HttpHeadersModule#expires
.. _gzip: http://wiki.nginx.org/HttpGzipModule#gzip
.. _gzip_comp_level: http://wiki.nginx.org/HttpGzipModule#gzip_comp_level
.. _ssi: http://wiki.nginx.org/HttpSsiModule#ssi
.. _empty_gif: http://wiki.nginx.org/HttpEmptyGifModule#empty_gif
.. _geo: http://wiki.nginx.org/HttpGeoModule
.. _alias: http://wiki.nginx.org/HttpCoreModule#alias
.. _return: http://wiki.nginx.org/HttpRewriteModule#return
.. _rewrite: http://wiki.nginx.org/HttpRewriteModule#rewrite
.. _fastcgi_pass: http://wiki.nginx.org/HttpFcgiModule#fastcgi_pass
.. _scgi_pass: http://wiki.nginx.org/HttpScgiModule#scgi_pass
.. _uwsgi_pass: http://wiki.nginx.org/HttpUwsgiModule#uwsgi_pass
.. _try_files: http://wiki.nginx.org/HttpCoreModule#try_files
.. _http: http://wiki.nginx.org/NginxHttpCoreModule#http
.. _server: http://wiki.nginx.org/HttpCoreModule#server
.. _if: http://wiki.nginx.org/HttpRewriteModule#if
.. _location: http://wiki.nginx.org/HttpCoreModule#location
.. _ssi: http://wiki.nginx.org/HttpSsiModule#ssi
.. _ssl_certificate: http://wiki.nginx.org/HttpSslModule#ssl_certificate
.. _ssl_certificate_key: http://wiki.nginx.org/HttpSslModule#ssl_certificate_key
.. _user: http://wiki.nginx.org/CoreModule#user
.. _listen: http://wiki.nginx.org/HttpCoreModule#listen
.. _access_log: http://wiki.nginx.org/HttpLogModule#access_log
.. _error_log: http://wiki.nginx.org/NginxCoreModule#error_log
.. _server_name: http://wiki.nginx.org/HttpCoreModule#server_name
.. _root: http://wiki.nginx.org/HttpCoreModule#root
.. _index: http://wiki.nginx.org/HttpCoreModule#index
.. _server_tokens: http://wiki.nginx.org/HttpCoreModule#server_tokens
.. _client_body_timeout: http://wiki.nginx.org/HttpCoreModule#client_body_timeout
.. _client_header_timeout: http://wiki.nginx.org/HttpCoreModule#client_header_timeout
