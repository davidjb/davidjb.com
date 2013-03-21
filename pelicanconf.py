#!/usr/bin/env python
# -*- coding: utf-8 -*- #

PLUGINS = ['pelican.plugins.gravatar']

AUTHOR = u'David Beitey'
AUTHOR_EMAIL = u'qnivq@qnivqwo.pbz'.decode('rot13')
SITENAME = u'DavidJB.com'
SITEURL = 'http://davidjb.com'
SITESUBTITLE = "Ramblings about Plone, Pyramid, Python, the web, Linux, roses and more."

DISQUS_SITENAME = 'davidjb'
#GITHUB_URL = "http://github.com/davidjb/"
GOOGLE_ANALYTICS = 'UA-24253455-1'
TWITTER_USERNAME = 'davidjb_'

PAGE_DIR = 'pages'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

STATIC_PATHS = ['images', 'files']

TIMEZONE = 'Australia/Queensland'

DEFAULT_LANG = u'en'

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}/index.html'

# Blogroll
LINKS =  (('Planet Plone', 'http://planet.plone.org'),
          ('', ''),
          ('', ''),
         )

# Social widget
SOCIAL = (('GitHub', 'http://git.io/djb'),
          ('Twitter', 'http://twitter.com/davidjb_'),
          ('LinkedIn', 'http://linkedin.com/in/davidbeitey'),
          ('Facebook', 'http://facebook.com/david.beitey'),
          ('Google+', 'https://plus.google.com/u/0/106527454335411502430'),
         )

DEFAULT_PAGINATION = 10
