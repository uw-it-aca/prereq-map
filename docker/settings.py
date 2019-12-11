from .base_settings import *

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'webpack_loader',
    'prereq_map'
]

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'prereq_map/bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'prereq_map', 'static', 'webpack-stats.json'),
    }
}

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

DATA_ROOT = os.path.join(BASE_DIR, "prereq_map/data")

GOOGLE_ANALYTICS_KEY = os.getenv("GOOGLE_ANALYTICS_KEY", default=" ")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'debug':  True,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'prereq_map.context_processors.google_analytics',
                'prereq_map.context_processors.django_debug',
            ],
        }
    }
]

if os.getenv("ENV") == "localdev":
    DEBUG = True

if os.getenv("ENV") == "prod" or os.getenv("ENV") == "eval":
    USE_CACHE = True
