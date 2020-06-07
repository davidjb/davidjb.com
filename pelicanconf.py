#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import codecs
import itertools
import os

PLUGIN_PATHS = ['src/pelican-plugins']
PLUGINS = ['gravatar', 'tipue_search']

AUTHOR = 'davidjb (David Beitey)'
AUTHOR_EMAIL = codecs.decode('qnivq@qnivqwo.pbz', encoding='rot13')
SITENAME = 'DavidJB.com'
SITEURL = 'https://davidjb.com'
RELATIVE_URLS = True
SITESUBTITLE = "Python, Technology, Web, Linux, and more, by David Beitey"
THEME = 'src/pure-single'

DISQUS_SITENAME = 'davidjb'
# GITHUB_URL = "https://github.com/davidjb/"
# GOOGLE_ANALYTICS = 'UA-24253455-1'
TWITTER_USERNAME = 'davidjb_'

PATH = 'content'
PAGE_PATHS = ['pages']
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-.*'
NEWEST_FIRST_ARCHIVES = True

STATIC_PATHS = ['images', 'files']
# All files in the `extras` directory get picked up.
# Base paths are relative to the ``content`` directory.
EXTRA_PATH_METADATA = {
    os.path.join('extras', filename): {'path': filename}
    for filename in os.listdir('content/extras')
}
STATIC_PATHS.extend(EXTRA_PATH_METADATA.keys())

TIMEZONE = 'Australia/Brisbane'
TYPOGRIFY = True

DEFAULT_LANG = 'en'

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}/index.html'

# Save all pages exactly as they are recorded in their slug
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}'

# Create archives of posts
YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# external = (('Planet Plone', 'http://planet.plone.org'),
#             ('Apple Insider', 'http://appleinsider.com/'))
# professional = (('jcu.me Research Porfolio', 'http://jcu.me'),
#                 ('Latest coding activity', 'http://git.io/djb'))
# fun = (('XKCD', 'http://xckd.com'),)
# LINKS = list(itertools.chain(*itertools.izip(external, professional, fun)))

# Social widget
SOCIAL = (('github-square', 'http://git.io/djb'),
          ('twitter-square', 'http://twitter.com/davidjb_'),
          ('linkedin-square', 'http://linkedin.com/in/davidbeitey'),
          ('facebook-square', 'http://facebook.com/david.beitey'),
          ('google-plus-square', 'http://google.com/+DavidBeitey'))

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 100

# Pure theme settings
COVER_IMG_URL = '/images/cover.jpg'
PROFILE_IMG_URL = '/images/me-square.png'
FAVICON_URL = '/favicon.ico'
TAGLINE = SITESUBTITLE
