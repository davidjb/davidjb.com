#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import itertools
import os

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
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-.*'
NEWEST_FIRST_ARCHIVES = True

STATIC_PATHS = ['images', 'files']
EXTRA_TEMPLATES_PATHS = ['templates']

#All files in the `extras` directory get picked up.
directory='content/extras'
FILES_TO_COPY = [(os.path.join('extras', filename), filename) for filename in os.listdir(directory)]

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
