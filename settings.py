# Django settings for repos project.
import os
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS



# Django 1.2+
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': 'dev.db',                      # Or path to database file if using sqlite3.
#         'USER': '',                      # Not used with sqlite3.
#         'PASSWORD': '',                  # Not used with sqlite3.
#         'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#         'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#     }
# }


# Ye Olde Django

DATABASE_ENGINE = 'django.db.backends.sqlite3'
DATABASE_NAME = 'dev.db'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'qw(l8_%pzwg=!8tb1=zeh2o-c4e*4j(h0lllu9j&v=vbzts5s1'

# Auth
LOGIN_URL = '/login/'
AUTH_PROFILE_MODULE = 'extendedauth.Profile'


# GOPLAN STUFF - Should create a credentials app?
# ------------------------------------------------------------
# Platform46 offices
# OAUTH_KEY = 'd0JT0WPHsFZKoiUJx2IOg'
# OAUTH_SECRET = 'kmvcSnUzb83ilBGW018dR36vPmm1jvp0wnxGnJHtaeA'

# Baker St
OAUTH_KEY = 'hVZdf3xkzLS9aYwMMdBXw'
OAUTH_SECRET = 'fuxf1A6IN7pL8ue55UZ9u2bU9FT5XG6HWQfmHfnvgY'

GOPLAN_COMPANY_ALIAS = 'twp'

OAUTH_URL_REQUEST_TOKEN = 'http://goplanapp.com/oauth/request_token'
OAUTH_URL_ACCESS_TOKEN = 'http://goplanapp.com/oauth/access_token'
OAUTH_URL_AUTHORIZE = 'http://twp.goplanapp.com/oauth/authorize'

# BEANSTALK STUFF - Get this out of here?
# ------------------------------------------------------------
BEANSTALK_SUBDOMAIN = 'twp'
BEANSTALK_USERNAME = 'atkinsonr'
BEANSTALK_PASSWORD = 'belvarde'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source', #old skool django
    #'django.template.loaders.filesystem.Loader',
    #'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT,'templates')
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'extendedauth',
    'goplan',
)

try:
    import django_extensions
    INSTALLED_APPS += ('django_extensions',)
except ImportError:
    pass

