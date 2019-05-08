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

if os.getenv("ENV") == "localdev":
    DEBUG = True
