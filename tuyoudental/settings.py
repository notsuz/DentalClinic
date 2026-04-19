"""
Django settings for tuyoudental project.
"""

from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-@hv&r&35v_1b$-5@2-r+c%$jd3^(yx_&cefq&7gw9zta%05*vm')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'cloudinary_storage',       # MUST be #1
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'cloudinary',
    
    'website.apps.WebsiteConfig', # ONLY keep this one, delete 'website' below it
]
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dvrf56dpr',
    'API_KEY': '419491894414183',
    'API_SECRET': 'CmNDCBKlwvQFTwEfUSSQSrXr17Q',
    'STATICFILES_STORAGE': None,
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# CLOUDINARY_URL=cloudinary://<your_api_key>:<your_api_secret>@dvrf56dpr

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Required for Vercel static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tuyoudental.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'website.context_processors.site_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'tuyoudental.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

# Default to local SQLite for development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Use Neon/Vercel Postgres if the environment variable exists
# Using ALL CAPS to match Vercel and Terminal standards
db_from_env = os.environ.get('DATABASE_URL') or os.environ.get('STORAGE_URL')

if db_from_env:
    DATABASES['default'] = dj_database_url.config(
        default=db_from_env,
        conn_max_age=600,
        ssl_require=True
    )


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Where Django looks for static files in development
STATICFILES_DIRS = [BASE_DIR / 'static']

# Where Vercel gathers static files for production
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Modern Storage configuration for Django 4.2+ and WhiteNoise
STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        # Ensure there is no typo in this path
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}


# Media files (Uploaded images for Dental Services)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'