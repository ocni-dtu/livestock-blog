
AUTHOR = 'Christian Kongsgaard'
SITENAME = 'Christian Kongsgaard'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Paths
STATIC_PATHS = ['/content/images', '/content/authors', '/content/posts', '/content/pages']
THEME = "themes/minimalX"

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 70
TAG_CLOUD = False

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud"]
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
