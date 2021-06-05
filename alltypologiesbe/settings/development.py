from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'alltypologies',
        'HOST': 'postgres',
        'USER': 'doccano',
        'PASSWORD': 'doccano'
    }
}

INSTALLED_APPS = INSTALLED_APPS + [
    'corsheaders',
]

MIDDLEWARE = MIDDLEWARE + [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

# DA NON METTERE IN PRODUZIONE
CORS_ALLOW_ALL_ORIGINS = True

ALLOWED_HOSTS = ['*', ]
