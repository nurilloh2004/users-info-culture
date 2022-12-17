
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z@z9fp68_8lmnd+z0fy_n54lj+9$59h$rhy2g1!c6!welwf$1v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'multi_captcha_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'adminrestrict.middleware.AdminPagesRestrictMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'uz'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Changed settings
# Static
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Template dirs and etc.
INSTALLED_APPS += [
    'django.contrib.humanize'
]
TEMPLATES[0]['DIRS'] += [os.path.join(BASE_DIR, 'templates')]
TEMPLATES[0]["OPTIONS"]["context_processors"] += ['main.context.site_settings_context']


# TZ
del TIME_ZONE
TIME_ZONE = 'Asia/Tashkent'


# Parler
MIDDLEWARE += [
    'django.middleware.locale.LocaleMiddleware'
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

INSTALLED_APPS += [
    'parler'
]

LANGUAGES = (
    ('uz', u"O'zbekcha"),
    ('ru', u"Русский"),
    ('en', u"English"),
)

PARLER_DEFAULT_LANGUAGE_CODE ='uz'

PARLER_LANGUAGES = {
    None: (
        {'code': 'uz', },
        {'code': 'ru', },
        {'code': 'en', },

    ),
    'default': {
        'fallbacks': ['uz'],
        'hide_untranslated': False,
    }
}

PARLER_ENABLE_CACHING = False


# Django admin sortable
INSTALLED_APPS += [
    'adminsortable2'
]


# Django MPTT
INSTALLED_APPS += [
    'mptt'
]

# Django CKEditor
INSTALLED_APPS += [
    'ckeditor',
    'ckeditor_uploader'
]

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/ckeditor/"
CKEDITOR_ALLOW_NONIMAGE_FILES = True
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Extended',
        'disallowedContent': 'img{width,height}',
        'extraPlugins': 'embed',
    },
    'basic': {
        'toolbar': "Basic"
    }
}


# Django Rosetta. Translations For Django Panel
INSTALLED_APPS += [
    'rosetta'
]
ROSETTA_WSGI_AUTO_RELOAD = True
ROSETTA_UWSGI_AUTO_RELOAD = True

# Django cleanup - Remove old file from ImageField and FileField on model instance update
INSTALLED_APPS += [
    'django_cleanup.apps.CleanupConfig',
]


INSTALLED_APPS += [
    'geoposition',
]

GEOPOSITION_BACKEND = 'leaflet'


INSTALLED_APPS += [
    'snowpenguin.django.recaptcha3',
]

RECAPTCHA_PUBLIC_KEY = '6LcQF9MaAAAAAGPmp7PbbX-zSZoDe7vwEjAsgj_a'
RECAPTCHA_PRIVATE_KEY = '6LcQF9MaAAAAAAlUmOlqv3vr0zmHIGFkg4bfMVF7'
RECAPTCHA_DEFAULT_ACTION = 'generic'
RECAPTCHA_SCORE_THRESHOLD = 0.5


INSTALLED_APPS += [
    'poll',
]
TEMPLATES[0]['DIRS'] += [os.path.join(BASE_DIR, 'poll/templates')]

# App
ALLOWED_HOSTS += ["*"]
INSTALLED_APPS += [
    'main',
    'adminrestrict',
]


#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_USE_TLS = True
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'testemailsend3@gmail.com'
#EMAIL_HOST_PASSWORD = 'Testemail24'

#EMAIL_HOST = 'mail.madaniyat.uz'
#EMAIL_USE_SSL = True
#EMAIL_PORT = 25
#EMAIL_HOST_USER = 'saytinfo@madaniyat.uz'
#EMAIL_HOST_PASSWORD = '1saytinfo!'

EMAIL_HOST = 'mail.madaniyat.uz'
EMAIL_USE_SSL = True
EMAIL_PORT = 465
EMAIL_HOST_USER = 'saytinfo@madaniyat.uz'
EMAIL_HOST_PASSWORD = '1saytinfo!'


GEOPOSITION_GOOGLE_MAPS_API_KEY = ""

ADMINRESTRICT_BLOCK_GET = True

MULTI_CAPTCHA_ADMIN = {
    'engine': 'simple-captcha',
}

RECAPTCHA_PUBLIC_KEY = '6LdqLDYfAAAAAGjO4sdpwqUMCOdc_oOA_DuCL92U'
RECAPTCHA_PRIVATE_KEY = '6LdqLDYfAAAAAPVvigukAO30R-vJhBF8fb0d8vMI'
