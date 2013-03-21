Plone/Zope: Using LDAPUserFolder with posixGroups
#################################################
:date: 2010-06-03 16:03
:author: davidjb
:category: Plone 
:tags: groups, ldap, ldapuserfolder, openldap, patch, plone, python, zope
:slug: plonezope-using-ldapuserfolder-with-posixgroups

Due to various reasons, the Products.LDAPUserFolder package available
for Plone and Zope doesn't support POSIX groups.  The 'official' (ish)
reason for this is because of the fact that these groups don't store
full distinguished names (DNs) for members.  It makes some degree of
sense, because a user ID like 'david.test' isn't strictly unique.  On
the other hand, these types of groups are quite common in LDAP
implementations; not supporting them without giving it at least half a
shot to find the user seems a bit strange.

Here's where a quick patch steps in. Thanks to Weblion's infinity of
Plone resources (specifically, their article on `Plone LDAP`_), I
patched part of my Products.LDAPUserFolder.

Now, what they've got wasn't infallible. Whilst the patch they have on
their site took care of enumerating the groups, and the groups a user is
in, it didn't ensure looking a group showed its users. Whether this was
a change in LDAPUserFolder recently (since version 2.12) or not, I'm not
sure.

In any case, the reason for the issue is that deep down, the code
attempts to query group members by DN. Obviously our POSIX groups don't
have full DNs, so with a quick bit of string manipulation (read:
hacking), I assume that the *user base* you specify will have your user.
**Note:** this won't do one iota if your user isn't at the user base,
but if it is -- like all the LDAPs I've used -- you're golden. Here's
the patch for Products.LDAPUserFolder 2.17.


.. code:: diff
    
    diff --git a/Products/LDAPUserFolder/LDAPUserFolder.py b/Products/LDAPUserFolder/LDAPUserFolder.py
    index 0e61396..a235e74 100644
    --- a/Products/LDAPUserFolder/LDAPUserFolder.py
    +++ b/Products/LDAPUserFolder/LDAPUserFolder.py
    @@ -950,6 +950,7 @@ class LDAPUserFolder(BasicUserFolder):

    for dn in all_dns.keys():
    try:
    +                if 'uid=' not in dn: dn = ('uid='+dn+','+self.users_base)
    user = self.getUserByDN(dn)
    except:
    user = None
    @@ -1216,6 +1217,8 @@ class LDAPUserFolder(BasicUserFolder):
    f_template = '(&amp;amp;(objectClass=%s)(%s=%s))'
    group_filter = '(|'

    +                dn = dn.replace('uid=','').replace(','+self.users_base,'')
    +
    for g_name, m_name in GROUP_MEMBER_MAP.items():
    fltr = filter_format(f_template, (g_name, m_name, dn))
    group_filter += fltr
    diff --git a/Products/LDAPUserFolder/utils.py b/Products/LDAPUserFolder/utils.py
    index 4a88cd7..26b73bc 100644
    --- a/Products/LDAPUserFolder/utils.py
    +++ b/Products/LDAPUserFolder/utils.py
    @@ -48,6 +48,7 @@ GROUP_MEMBER_MAP = { 'groupOfUniqueNames' : 'uniqueMember'
    , 'accessGroup' : 'member'
    , 'group' : 'member'
    , 'univentionGroup' : 'uniqueMember'
    +                  , 'posixGroup' : 'memberUid'
    }

    VALID_GROUP_ATTRIBUTES = Set(list(GROUP_MEMBER_MAP.values()) +

.. _Plone LDAP: https://weblion.psu.edu/trac/weblion/wiki/LDAPWithPlone
