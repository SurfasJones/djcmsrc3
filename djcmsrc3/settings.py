import os
gettext = lambda s: s
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
"""
Django settings for djcmsrc3 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0=g!mtoxqxj@dm@4abk3u+6ex^hmhx+w6_p4==dm*651ox5@_$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition





ROOT_URLCONF = 'djcmsrc3.urls'

WSGI_APPLICATION = 'djcmsrc3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

SITE_ID = 1

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.csrf',
    'django.core.context_processors.tz',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    'django.core.context_processors.static'
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, "templates"),
)

INSTALLED_APPS = (
    'djangocms_admin_style',
    'djangocms_text_ckeditor',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',
    'djangocms_style',
    'djangocms_column',
    'djangocms_file',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'reversion'
)

LANGUAGES = (
    ## Customize this
    ('en', gettext('en')),
    ('de', gettext('de')),
    ('es', gettext('es')),
    ('fr', gettext('fr')),
)

CMS_LANGUAGES = {
    ## Customize this
    'default': {
        'hide_untranslated': False,
        'redirect_on_fallback': True,
        'public': True,
    },
    1: [
        {
            'redirect_on_fallback': True,
            'code': 'en',
            'hide_untranslated': False,
            'name': gettext('en'),
            'public': True,
        },
        {
            'redirect_on_fallback': True,
            'code': 'de',
            'hide_untranslated': False,
            'name': gettext('de'),
            'public': True,
        },
        {
            'redirect_on_fallback': True,
            'code': 'es',
            'hide_untranslated': False,
            'name': gettext('es'),
            'public': True,
        },
        {
            'redirect_on_fallback': True,
            'code': 'fr',
            'hide_untranslated': False,
            'name': gettext('fr'),
            'public': True,
        },
    ],
}

CMS_TEMPLATES = (
    ## Customize this
    ('page.html', 'Page'),
    ('feature.html', 'Page with Feature')
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

DATABASES = {
    'default':
        {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'project.db', 'HOST': 'locahost', 'USER': '', 'PASSWORD': '', 'PORT': ''}
}