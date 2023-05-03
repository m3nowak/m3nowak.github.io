AUTHOR = 'Mikołaj Nowak'
SITENAME = 'Mikołaj Nowak - Blog'
SITEURL = ''
#SITEURL = "https://m3nowak.github.io"
SITENAME = "Mikołaj's Blog"
SITETITLE = "Mikołaj's Blog"
SITESUBTITLE = "I do things on a computer"
SITEDESCRIPTION = "Various notes on programming, devops and other things"

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True

BROWSER_COLOR = "#333"
ROBOTS = "index, follow"

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa"
}

COPYRIGHT_YEAR = 2023

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Github', 'https://github.com/m3nowak'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/m3nowak'),
          )

DEFAULT_PAGINATION = 10
THEME = 'themes/flex'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True