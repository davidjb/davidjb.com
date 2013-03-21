Plone: Clamping down on categories
##################################
:date: 2009-04-21 09:11
:author: davidjb
:category: Plone 
:tags: categories, enforce, plone
:slug: plone-clamping-down-on-categories

Probably my last blog entry here because I'll be moving to the AWESOME
WordPress very soon @ http://davidjb.com/blog (with a nice new site design,
too)  (EDIT: Migrated from my old blog 8-) ) .  (**2013 edit**: Goodbye
Wordpress, I really hate PHP and its security issues. I'm a Python developer
and I really should be eating my own dogfood).

Anyway, how to prevent the addition of new categories to the Plone
listing (the inline comments aren't mine, they're copied):

    It's a bit hidden and probably undocumented but here we go: ZMI ->
    portal\_metadata -> schema tab (should be the default view of the
    tool in ZMI) -> click DCMI in the Metadata Schemas section (why do
    so many people not know that the plural form of 'schema' is
    'schemata' - but I digress …) -> click 'Subject' within the
    'Element' row -> add terms to the vocabulary field - in the upper
    part if this should apply to all portal types (don't forget to press
    'Update') or in the lower part to define a portal type specific
    policy.

Something that wasn't mentioned was the 'Enforce vocabulary?' box. If
you go and tick that, and save the changes, then any additional
categories that someone adds are only localised to that one content item
- they're not entered into the overall listing. Doesn't stop someone who
misses a category from entering a new one locally, but it's a good
start.

