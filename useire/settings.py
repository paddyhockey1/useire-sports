"""
Django settings for useire project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Pondacenter#_1993'

# SECURITY WARNING: don't run with debug turned on in production!


# DEBUG = 'DEVELOPMENT' in os.environ
DEBUG = True


ALLOWED_HOSTS = [
     '8000-paddyhockey-useiresport-0luhaxh10q5.ws-eu116.gitpod.io',
     'https://useire-sports-b029765775db.herokuapp.com',
    
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'home',
    'products',
    'bag',
    'checkout',
    'profiles',
    'crispy_forms',
]

MIDDLEWARE = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",

    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
)

CRISPY_TEMPLATE_PACK = 'bootstrap4'

ROOT_URLCONF = 'useire.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # required by allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'bag.contexts.bag_contents',
            ],

             'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
            ]
        },
    },
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',

]

SITE_ID = 1

CSRF_TRUSTED_ORIGINS = [
    'https://8000-paddyhockey-useiresport-0luhaxh10q5.ws-eu116.gitpod.io',
    'https://useire-sports-b029765775db.herokuapp.com/',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'useire.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('postgres://uj0y2uh5h5j:NUwBKmEzjdGb@ep-gentle-mountain-a23bxz6h-pooler.eu-central-1.aws.neon.tech/urban_scuba_skier_712833'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }






# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Stripe
FREE_DELIVERY_THRESHOLD = 50
STANDARD_DELIVERY_PERCENTAGE = 10
STRIPE_CURRENCY = 'eur'
STRIPE_PUBLIC_KEY = 'pk_test_51QCGuODyLxdlHT8TwyywDVVBc6qtaFM7k4UNOFcXKxX2QwARnfswIVNOtPe1FQwTMWJcYOaGpyBpKJtUNxP8g3zq00aToXunsW'
STRIPE_SECRET_KEY = 'sk_test_51QCGuODyLxdlHT8TakKFovAop3V2hL2I7lF7hwTDNh2l7iWRGU7PcOSwcyIEyueZQjQ6d67DaHz4OoSzephyrDYc00mWLZWKBy'
STRIPE_WH_KEY = 'whsec_hOUEAa21ja4NwaNIvyLQ7tv1XEw1E8lR'
DEFAULT_FROM_EMAIL = 'useiresports@example.com'

# FREE_DELIVERY_THRESHOLD = 50
# STANDARD_DELIVERY_PERCENTAGE = 10
# STRIPE_CURRENCY = 'eur'
# STRIPE_PUBLIC_KEY = ''
# STRIPE_SECRET_KEY = ''
# STRIPE_WH_KEY = ''
# DEFAULT_FROM_EMAIL = 'useiresports@example.com'
