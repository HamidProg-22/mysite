from mysite.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v*dw-q8r+)a6@2i(5961!@_aj&j!-touat4g$9@j+&kats_uy='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# INSTALLED_APPS = []

# site framework
# SITE_ID = 2
SITE_ID = 3

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

X_FRAME_OPTIONS = 'SAMEORIGIN'
# CSRF_COOKIE_SECURE = True