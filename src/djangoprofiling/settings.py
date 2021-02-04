import logging
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.conf import settings
from sentry_sdk.integrations.logging import LoggingIntegration
from constance import config
import environ

env = environ.Env()

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))  # 'djangoprofiling/'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 'src/'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c+9t0ulzqbdm7u1))v_7%sas0*d%)_+a4lrg&)d7t)fl0)=+-hi_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'constance',
    'constance.backends.database',
    'health_check',
    'markdownify',
    # own apps
    'pages',
    'author',
    'article',
    'drf_yasg2',
    'silk',
    # 'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Profiling middleware
    'silk.middleware.SilkyMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'djangoprofiling.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
# ------------------------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')


WSGI_APPLICATION = 'djangoprofiling.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# ------------------------------------------------------------------
DB_USER = env.str("POSTGRES_USER", "postgres")
DB_PASSWORD = env.str("POSTGRES_PASSWORD", "root")
DB_HOST = env.str("POSTGRES_HOST", "127.0.0.1")
DB_NAME = env.str("POSTGRES_DB", "djangoprofiling")

DATABASES = {
    'default': env.db('DATABASE_URL', f'postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}'),
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': f'{DB_NAME}',
    #     'USER': f'{DB_USER}',
    #     'PASSWORD': f'{DB_PASSWORD}',
    #     'HOST': f'{DB_HOST}',
    #     'PORT': '5432',
    # },
    # Use Sqlite3
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
}
DATABASES['default']['ATOMIC_REQUESTS'] = True


# Cahce
# ------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    },
}


# Password validation
# ------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# LOGGING = {
#     'version': 1,
#     'formatters': {
#         'mosayc': {
#             'format': '%(asctime)-15s %(levelname)-7s %(message)s [%(funcName)s (%(filename)s:%(lineno)s)]',
#         }
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose'
#         }
#     },
#     'loggers': {
#         'silk': {
#             'handlers': ['console'],
#             'level': 'DEBUG'
#         }
#     },
# }


# Django-Silk
# ------------------------------------------------------------------
SILKY_META = True  # Sometimes its useful to be able to see what effect Silk is having on the request/response time.
SILKY_PYTHON_PROFILER = True
SILKY_PYTHON_PROFILER_BINARY = False
SILKY_PYTHON_PROFILER_RESULT_PATH = './djangoprofiling/profiles'
# SILKY_DYNAMIC_PROFILING = [
#     {'module': 'author.views', 'function': 'AuthorViewSet.get_authors'},
#     {'module': 'author.views', 'function': 'AuthorViewSet.get_author'},
#     {'module': 'author.views', 'function': 'AuthorViewSet.get'},
#     {'module': 'author.views', 'function': 'AuthorViewSet.post'},
#     {'module': 'author.views', 'function': 'AuthorViewSet.put'},
#     {'module': 'author.views', 'function': 'AuthorViewSet.delete'},
# ]


def my_custom_logic(request):
    # return 'record_requests' in request.session
    return config.DJANGO_SILK_PROFILER_ENABLED


# SILKY_INTERCEPT_PERCENT = 50  # log only 50% of requests (Use in Load Testing)
# SILKY_INTERCEPT_FUNC = my_custom_logic  # default: False
SILKY_INTERCEPT_FUNC = lambda r: settings.DEBUG  # Do not profile requests when DEBUG = False
# Do not garbage collect for tests
SILKY_MAX_RECORDED_REQUESTS_CHECK_PERCENT = 0
SILKY_MAX_RECORDED_REQUESTS = 10 ** 3  # To make sure silky garbage collects old request/response data, a config var can be set to limit the number of request/response rows it stores.


# DjangoDebugToolbar Configuration
# ------------------------------------------------------------------
# DEBUG_TOOLBAR_PANELS = [
#     'debug_toolbar.panels.history.HistoryPanel',
#     'debug_toolbar.panels.versions.VersionsPanel',
#     'debug_toolbar.panels.timer.TimerPanel',
#     'debug_toolbar.panels.settings.SettingsPanel',
#     'debug_toolbar.panels.headers.HeadersPanel',
#     'debug_toolbar.panels.request.RequestPanel',
#     'debug_toolbar.panels.sql.SQLPanel',
#     'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#     'debug_toolbar.panels.templates.TemplatesPanel',
#     'debug_toolbar.panels.cache.CachePanel',
#     'debug_toolbar.panels.signals.SignalsPanel',
#     'debug_toolbar.panels.logging.LoggingPanel',
#     'debug_toolbar.panels.redirects.RedirectsPanel',
#     'debug_toolbar.panels.profiling.ProfilingPanel',
# ]
# DEBUG_TOOLBAR_CONFIG = {
#     'DISABLE_PANELS': [
#         'debug_toolbar.panels.redirects.RedirectsPanel',
#     ],
#     'SHOW_TEMPLATE_CONTEXT': True,
# }
# INTERNAL_IPS = ['127.0.0.1', ]


# Constance
# ------------------------------------------------------------------
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_DATABASE_CACHE_BACKEND = 'default'

CONSTANCE_ADDITIONAL_FIELDS = {
    'true_or_false_select': ['django.forms.fields.ChoiceField', {
        'widget': 'django.forms.Select',
        'choices': ((None, "-----"), (True, "true"), (False, "false"))
    }],
}

CONSTANCE_CONFIG = {
    'SENTRY_TRACING_ENABLED': (False, 'select true or false', bool),
    'DJANGO_SILK_PROFILER_ENABLED': (False, 'select true or false', 'true_or_false_select'),
}


# Sentry
# ------------------------------------------------------------------
SENTRY_DNS = env.str("SENTRY_DNS", default="https://1d390e4b6ab34327800d124f2905b5c1@o497714.ingest.sentry.io/5574162")


def traces_sampler(sampling_context):
    return 1.0 if config.SENTRY_TRACING_ENABLED else 0


sentry_logging = LoggingIntegration(
    level=logging.INFO,        # Capture info and above as breadcrumbs
    event_level=logging.ERROR  # Send errors as events
)

sentry_sdk.init(
    dsn=f"{SENTRY_DNS}",
    integrations=[sentry_logging, DjangoIntegration()],
    debug=False,
    # traces_sample_rate=1.0,
    traces_sampler=traces_sampler,
    send_default_pii=False
)

