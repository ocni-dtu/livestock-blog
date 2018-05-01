
AUTHOR = 'Christian Kongsgaard'
SITENAME = 'Christian Kongsgaard'
SITEURL = 'http://localhost:8000'
SITEDESCRIPTION = "Hi, I'm Christian and welcome to my website!"

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
STATIC_PATHS = ['images', 'authors', 'data']
PLUGIN_PATHS = ["plugins"]
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']
THEME = "themes/minimalX"

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/christian-kongsgaard-33825b78/'),
          ('github', 'https://github.com/ocni-dtu'),)

SHARE_BUTTONS = ('facebook', 'linkedin', 'mail')

DEFAULT_PAGINATION = 8
SUMMARY_MAX_LENGTH = 70
TAG_CLOUD = False

# Plugins
PLUGINS = ["tag_cloud"]

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Author Information
AUTHOR_INFO_SHORT_FABIAN_KEITEL = "I'm an architectural engineer focused on sustainable parametric design and building performance simulations. I use Python and Grasshopper to simulate outdoor thermal comfort, building energy, and daylight."
AUTHOR_INFO_FABIAN_KEITEL = "I'm am an architectural engineer focused on sustainable parametric design and " \
                                   "building performance simulations. I have an Master in Architectural Engineering " \
                                   "from the Technical University of Denmark, where I graduted in 2018.\nI am interested" \
                                   "in how to use Python and Grasshopper in combination to create work flows for " \
                                   "sustainable parametric designs.\n All my projects are open source and are available " \
                                   "on Github (Follow the icon below). For a full resumé go to my LinkedIn profile (Also " \
                                   "through the icon below)"
