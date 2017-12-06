#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

PLUGINS = PLUGINS + ['optimize_images']

SITEURL = 'https://davidjb.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Append the full URL for search results
ARTICLE_URL = SITEURL + '/' + ARTICLE_URL

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
