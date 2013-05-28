Attributes not released to new Shibboleth Service Provider (SP)
###############################################################

:category: Web

Just created a new Shibboleth Service Provider (SP) instance and found an
Identity Providers (IdPs) is not releasing attributes to you?  Don't
worry, you're not alone.  In fact, the issue is far more common than you think,
despite a lack of documentation on the web.

Confirming the problem
~~~~~~~~~~~~~~~~~~~~~~

Firstly, make sure that your Shibboleth SP configuration is, as best you can
tell, correct.  Also, make sure that your ``shibd`` daemon has been
restarted after any configuration changes you've made (and your 
FastCGI ``shibauthorizer`` and ``shibresponder`` applications too, if you're
using those).  

If you're sure about the above, or just roughly sure that your SP configuration
is correct, then try to access your Shibboleth protected resource.  If you 
receive one of a variety of different intermediate errors - such as those
from an IdP page about missing metadata, or similar - then your SP's security
information hasn't yet been propagated within your Federation (or not yet to
that specific IdP).

If you don't receive an error message from an IdP or your Shibboleth SP, you
will likely end up at your application, assuming your web server configuration
is correct.  

Once you're here, then you may find, as I did, that the only Shibboleth user
attribute that was being sent through from ``shibd`` to the application was the
``TransientId``.  If you enable debug logging on your Shibboleth SP, then
you'll see in the logs that no attributes are actually being released from that
given IdP. It's worth noting that this is almost certainly going to be an
intermittent issue for you -- some IdPs will release attributes and others
flatly refuse. **If you're seeing this, then you've hit the same issue as me.**

About the issue
~~~~~~~~~~~~~~~

Some IdPs do not allow attributes to be released to new (arbitrary) SPs until
such point as the IdP administrator manually reconfigures the IdP's attribute
filter.  In some limited cases that I've been exposed to, this situation may
have been resolved by correcting the attributes being released by the IdP in
the first place, or correcting file system permission on files, but for the
most part, it's because some IdPs simply need to be manually configured first.

The IdPs that work with your SP straight out, however, will be those that
are allowing automated attribute release.  In the case of the `Australian 
Access Federation (AAF) <http://aaf.edu.au>`_, which my SPs are a part of,
a few - around 40% - of IdPs are using automated release.  The unfortunate 
situation is the rest of them.  

This problem means that your SP **will not** work with all those other IdPs
until someone tries to log into your application, and eventually complains to
you about it.  This situation represents an administrative nightmare, since 
a federation, such as the AAF, has 40+ identity providers, and trying to
contact each and every IdP to get them to check your SP and application is
untenable.  Imagine having to do the same for multiple SPs - the workload and
overhead just increased by factor of 2 or 3.

Alternatively, you could just let your application fail against those IdPs
that don't release attributes; being the good application developer I am,
I'm not comfortable building something I know will fail more than half of the 
time.

Conclusion & Future
~~~~~~~~~~~~~~~~~~~

My experience directly relates to my SP being part of the Australian Access
Federation (AAF), so other federation experiences may differ.  The reason 
the the issue exists is, so far as I've been made aware, because of the variety
of IdPs that are out there, the differences in their policies and 
configurations.

This issue will continue to persist until such time as automated
attribute release and configuration is allowed from all IdPs.  Given how much
control some IdPs feel they need, this will be a problem for a long time to 
come.  I am following this up with the AAF in this specific case, so we'll
see what comes of it.

Unfortunately, this represents a failure to trust the Federation that IdPs
have subscribed to be a part of.  In my opinion, that's a complete breakdown
of the nature of what the Federation should be -- cross-institution 
authentication for all that *'just works'*.  Realistically, it's down to the
end-user whether they release their attributes to a service anyway -- and 
that's exactly how other SSO providers like OpenID work.

