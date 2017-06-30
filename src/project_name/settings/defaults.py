"""Default settings for the project.

All the common settings to all the environments should be here,
like applications or general configurations.
"""

import os
import mimetypes


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
VERSION = '20170630'

####################################################
# Applications                                     #
####################################################

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
)

# Put your applications here
APPS = ()

THIRDPARTY_APPS = (
    'allauth',                                   # General AllAuth stuff
    'allauth.account',                           # Database authentication
    'allauth.socialaccount',                     # Social auth abilities
    # For extra authentication mechanisms please check the allauth docs
    # website: http://django-allauth.readthedocs.org/en/latest/
    # 'allauth.socialaccount.providers.facebook',  # Facebook auth
    # 'allauth.socialaccount.providers.google',    # Google auth
)

INSTALLED_APPS = DJANGO_APPS + THIRDPARTY_APPS + APPS


####################################################
# Middleware and handlers                          #
####################################################

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware'
)

FILE_UPLOAD_HANDLERS = (
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
)

FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10 MB in RAM for the uploads

####################################################
# HTML Minify                                      #
####################################################

HTML_MINIFY = True
KEEP_COMMENTS_ON_MINIFYING = False

####################################################
# Messaging (also know as django messages)         #
####################################################

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

####################################################
# Authentication                                   #
####################################################

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # this is default
    "allauth.account.auth_backends.AuthenticationBackend",  # Allauth
)

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_DOMAIN = None

####################################################
# Templating                                       #
####################################################

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",

                # Allauth
                # "allauth.account.context_processors.account",
                # "allauth.socialaccount.context_processors.socialaccount",
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                # 'django.template.loaders.eggs.Loader',
            ],
        },
    },
]


####################################################
# Internationalization                             #
####################################################

USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = (
    ('en_US', 'English'),
)

LOCALE_PATHS = (
    BASE_DIR + '/locale',
)

#######################################################
# Webfont mime type fix for firefox and safari
#######################################################

mimetypes.add_type("application/font-woff", ".woff", True)

####################################################
# Static and uploads urls and paths                #
####################################################

STATIC_URL = '/static/'
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../../../htdocs/static'))
MEDIA_URL = ''
MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../../../htdocs/media'))

BUILD_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../../../htdocs/build_output'))

STATICFILES_DIRS = (
    BUILD_ROOT,
)

####################################################
# Other settings                                   #
####################################################

ROOT_URLCONF = '{{ project_name }}.urls'
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'
SITE_ID = 1

##########################################################
# Allauth settings                                       #
# Docs: http://django-allauth.readthedocs.org/en/latest/ #
##########################################################

ACCOUNT_ADAPTER = 'allauth.account.adapter.DefaultAccountAdapter'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True  # Must be true if auth is with email
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True
ACCOUNT_USERNAME_MIN_LENGTH = 3
ACCOUNT_USERNAME_BLACKLIST = ['root', 'administrator', 'superuser']
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_PASSWORD_MIN_LENGTH = 8
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
# This setting will try to get the data directly from the social account to
# bypass the signup form. If there is some error the form still will appear
SOCIALACCOUNT_AUTO_SIGNUP = True
# Specific settings for the social authentication if required
SOCIALACCOUNT_PROVIDERS = {}

SOCIALACCOUNT_PROVIDERS = \
    {'facebook': {
        'VERIFIED_EMAIL': True}}  # Prevent allauth of asking to confirm email

####################################################
# Logging                                          #
####################################################

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },

    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },

    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR + "/django.log",
            'maxBytes': 2097152,  # 2MB per file
            'backupCount': 2,  # Store up to three files
            'formatter': 'standard',
        },
    },

    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        # Log all the things!
        '': {
            'handlers': ["logfile", ],
            'level': 'DEBUG',
        },
    }
}


####################################################
# Testing                                          #
####################################################

TEST_RUNNER = 'django.test.runner.DiscoverRunner'
