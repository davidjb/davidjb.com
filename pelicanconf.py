#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import itertools

PLUGINS = ['pelican.plugins.gravatar']

AUTHOR = u'davidjb'
AUTHOR_EMAIL = u'qnivq@qnivqwo.pbz'.decode('rot13')
SITENAME = u'DavidJB.com'
SITEURL = 'http://davidjb.com'
SITESUBTITLE = "Ramblings about Plone, Pyramid, Python, the web, Linux, roses and more."
THEME = 'notmyidea'

DISQUS_SITENAME = 'davidjb'
#GITHUB_URL = "http://github.com/davidjb/"
GOOGLE_ANALYTICS = 'UA-24253455-1'
TWITTER_USERNAME = 'davidjb_'

PAGE_DIR = 'pages'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_DATE = 'fs'
NEWEST_FIRST_ARCHIVES = True

STATIC_PATHS = ['images', 'files']
EXTRA_TEMPLATES_PATHS = ['templates']
FILES_TO_COPY = (('extras/CNAME', 'CNAME'),
                 ('extras/.nojekyll', '.nojekyll'))

TIMEZONE = 'Australia/Queensland'
TYPOGRIFY = True

DEFAULT_LANG = u'en'

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}/index.html'

#Save all pages exactly as they are recorded in their slug
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}'

# Blogroll
external = (('Planet Plone', 'http://planet.plone.org'),
            ('Apple Insider', 'http://appleinsider.com/'),
           )
professional = (('jcu.me Research Porfolio', 'http://jcu.me'),
                ('Latest coding activity', 'http://git.io/djb'),
               )
fun = (('XKCD', 'http://xckd.com'),
       ('OzBargain', 'http://www.ozbargain.com.au') 
      )
LINKS = list(itertools.chain(*itertools.izip(external, professional, fun))) 

# Social widget
SOCIAL = (('GitHub', 'http://git.io/djb'),
          ('Twitter', 'http://twitter.com/davidjb_'),
          ('LinkedIn', 'http://linkedin.com/in/davidbeitey'),
          ('Facebook', 'http://facebook.com/david.beitey'),
          ('Google+', 'https://plus.google.com/u/0/106527454335411502430'),
         )

DEFAULT_PAGINATION = 10
