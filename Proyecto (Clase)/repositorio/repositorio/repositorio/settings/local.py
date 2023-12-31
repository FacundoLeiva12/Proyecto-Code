from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


"""# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases """

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Proyecto (Clase)',
        'USER': 'root',
        'PASSWORD': '023680',
        'HOST': 'localhost',
    }
}"""

STATICFILES_DIRS=(os.path.join(os.path.dirname(BASE_DIR),'static'),)