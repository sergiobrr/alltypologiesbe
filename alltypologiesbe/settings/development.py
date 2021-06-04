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
