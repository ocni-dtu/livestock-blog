
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
PLUGIN_PATHS = ['plugins', ]
PAGE_PATHS = ['pages', ]
ARTICLE_PATHS = ['posts', ]
THEME = "themes/minimalX"

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/christian-kongsgaard-33825b78/'),
          ('github', 'https://github.com/ocni-dtu'),)

SHARE_BUTTONS = ('linkedin', 'mail')

DEFAULT_PAGINATION = 8
SUMMARY_MAX_LENGTH = 70
TAG_CLOUD = False

# Plugins
PLUGINS = ["tag_cloud", ]


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Author Information
AUTHOR_INFO_SHORT_FABIAN_KEITEL = "I am an architectural engineer focused on computational environmental design and " \
                                  "building performance simulations.\nI aim to give more people access to complex " \
                                  "environmental information to promote innovative, evidence based, holistic and " \
                                  "sustainable building designs."

AUTHOR_INFO_FABIAN_KEITEL = "I am an architectural engineer focused on computational environmental design and " \
                            "building performance simulations.\nI founded Kongsgaard Engineering in order to do " \
                            "consulting and developing my software library called Livestock. My key goal is always " \
                            "to automate analyses workflows, enabling faster and easier availability to analysis " \
                            "results.\nI aim to give more people access to complex environmental information to " \
                            "promote innovative, evidence based, holistic and sustainable building designs.\n" \
                            "My toolbox consists of engineering knowledge; visual and proper programming mixed " \
                            "with architectural and design skills.\n " \
                            "All my projects are open source and are available on Github (follow the icon below).\n" \
                            "For a full resumé go to my LinkedIn profile (also through the icon below)."
